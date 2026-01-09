from bs4 import BeautifulSoup

from libelifoot.entity.player import Player
from libelifoot.provider.base_coach_provider import BaseCoachProvider
from libelifoot.provider.base_roster_provider import BaseRosterProvider
from libelifoot.util.date import get_work_days_in_season
from libelifoot.util.player_position import PlayerPosition


_PROVIDER_NAME = 'transfermarkt'
_PROVIDER_URL = f'https://www.{_PROVIDER_NAME}.com.br/'
_REQUEST_INTERVAL = 10  # seconds


class RosterProvider(BaseRosterProvider):

    # Cazaquistão, Curaçao, Eritreia, El salvador, Eswatini, French Guiana,
    # Gibraltar, Ilhas Caimão, Irã, Kosovo, Neocaledonia, Liechtenstein,
    # Palestina and Sant Martin  are not mapped by the game
    _COUNTRIES = {
        'Afeganistão': 'AFG',
        'África do Sul': 'AFS',
        'Arábia Saudita': 'ASA',
        'Azerbaijão': 'AZB',
        'Bangladeche': 'BGD',
        'Benim': 'BNI',
        'Bielorrússia': 'BLR',
        'Botsuana': 'BTW',
        'Cabo Verde': 'CAV',
        'Catar': 'QAT',
        'Chade': 'CHD',
        'Comores': 'CMR',
        'Congo': 'CNG',
        'Costa do Marfim': 'CMF',
        'Costa Rica': 'CRC',
        'Chile': 'CHL',
        'China': 'CHN',
        'China PR': 'CHN',
        'Chipre': 'CHP',
        'Coreia do Norte': 'CRN',
        'Coreia do Sul': 'CRS',
        'Egito': 'EGT',
        'Emirados Árabes Unidos': 'EAU',
        'Eslováquia': 'EVQ',
        'Eslovénia': 'EVN',
        'Gana': 'GNA',
        'Gâmbia': 'GMB',
        'Granada': 'GRN',
        'Haiti': 'HTI',
        'Ilha de Man': 'MAN',
        'Ilhas Faroe': 'FAR',
        'Iraque': 'IRQ',
        'Maurícias': 'MRC',
        'Mauritânia': 'MRT',
        'Namíbia': 'NMI',
        'Nova Zelândia': 'NZE',
        'País de Gales': 'WAL',
        'Santa Lúcia': 'SLU',
        'Trinidad e Tobago': 'TND',
        'USA': 'EUA',
        'Venezuela': 'VNZ',
        'Republic of Ireland': 'IRL',
        'República da Sérvia': 'SER',
        'República Checa': 'RCH',
        'República Democrática do Congo': 'CNG',
        'República Central Africana': 'RCA',
        'República Dominicana': 'RDO',
        'RD do Congo': 'CNG',
        'São Cristovão e Nevis': 'SKN',
        'São Tomé and Príncipe': 'STP',
        'São Vicente e Granadinas': 'SVG',
        'Vietname': 'VTM',
        'Zimbabué': 'ZBW'
    }

    def __init__(self):
        super().__init__(_PROVIDER_NAME, _PROVIDER_URL, self._COUNTRIES,
                         _REQUEST_INTERVAL, lambda p: int(p.value))

    def assemble_uri(self, team_id: str, season: int) -> str:
        tid = team_id.format('startseite')

        return f'{self._base_url}{tid}/saison_id/{season}' if season else \
            f'{self._base_url}{tid}'

    def parse_roster_data(self, reply: str) -> list[Player]:
        bs = BeautifulSoup(reply, 'html.parser')
        players = []

        even_players = bs.find_all('tr', class_='even')
        odd_players = bs.find_all('tr', class_='odd')

        for player in even_players + odd_players:
            try:
                p = player.find('table') \
                    .text \
                    .strip() \
                    .split('\n')

                if not p:
                    continue

                name = p[0].strip()
                pos = p[-1].strip()
                country = player.find_all('td', class_='zentriert')[2] \
                    .find('img') \
                    .get('title')

                if not country:
                    continue

                value = player.find_all('td', class_='rechts hauptlink')[0] \
                    .text

                players.append(
                    {
                        'name': name,
                        'position': pos,
                        'country': country,
                        'value': value
                    }
                )
            except IndexError:
                continue

        return self._parse_players(players)

    def _parse_players(self, data: list[dict]) -> list[Player]:
        players = []

        for player in data:
            if not player.get('country'): # ignore players with unknown country
                continue

            # TODO: discard players with unmaped countries

            players.append(
                Player(
                    name=self._get_name(player.get('name')),
                    position=self._get_position(player.get('position')),
                    country=self.get_country(player.get('country')),
                    value=self._get_value(player.get('value'))
                )
            )

        return players

    def _get_value(self, value: str) -> float:
        if value != '-':
            _, raw, mul = value.split(' ')

            match mul:
                case 'mi.': return float(raw) * 1000000
                case 'mil.': return float(raw) * 1000

        return 0.0

    def _get_name(self, name: str) -> str:
        if (len(name) <= self._MAX_NAME_SIZE) or (name.find(' ') == -1):
            return name

        ret = name.split(' ')
        initial = ret[0][0]
        second_name = ' '.join(ret[1:])

        return f'{initial} {second_name}'

    def _get_position(self, position: str) -> str:
        match position.split(' ')[0]:
            case 'Goleiro':
                return PlayerPosition.G.name
            case 'Zagueiro' | 'Lateral':
                return PlayerPosition.D.name
            case 'Volante' | 'Meia':
                return PlayerPosition.M.name
            case 'Ponta' | 'Seg.' | 'Centroavante':
                return PlayerPosition.A.name

        return ''


class CoachProvider(BaseCoachProvider):

    def __init__(self):
        super().__init__(_PROVIDER_NAME, _PROVIDER_URL, _REQUEST_INTERVAL)

    def assemble_uri(self, team_id: str, _) -> str:
        tid = team_id.format('mitarbeiterhistorie')

        return f'{self._base_url}{tid}/personalie_id/1'

    def parse_coach_data(self, reply: str, season: int) -> str:
        bs = BeautifulSoup(reply, 'html.parser')

        ret = bs.find_all('tbody')
        if len(ret) > 1:
            odd = ret[1].find_all('tr', class_='odd')
            even = ret[1].find_all('tr', class_='even')

            return self._select_coach(season, odd + even)

        return ''

    def _select_coach(self, season: int, coaches: list) -> str:
        coach = ''
        days = 0

        for entry in coaches:
            try:
                name = entry.tr.td.a.img.get('title')
                dates = entry.find_all('td', class_='zentriert')
                start = dates[1].text
                end = dates[2].text

                if not start:
                    continue

                start_year = int(start.split('/')[-1])

                if (season >= start_year) and (end == ''): # current coach
                    coach = name
                    break

                days_in_season = get_work_days_in_season(season, start, end)
                if days_in_season > days:
                    coach = name
                    days = days_in_season
            except IndexError:
                continue

        return coach
