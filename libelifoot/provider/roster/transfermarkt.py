from bs4 import BeautifulSoup

from libelifoot.entity.player import Player
from libelifoot.provider.roster_provider import RosterProvider
#from libelifoot.util.date import get_work_days_in_season
from libelifoot.util.player_position import PlayerPosition


class TransfermarktProvider(RosterProvider):

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
        super().__init__('transfermarkt',
                         'https://www.transfermarkt.com.br/',
                         self._COUNTRIES,
                         10,
                         lambda p: int(p.value))

    def assemble_roster_uri(self, team_id: str, season: int) -> str:
        tid = team_id.format('startseite')

        return f'{self._base_url}{tid}/saison_id/{season}' if season else \
            f'{self._base_url}{team_id}'

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
