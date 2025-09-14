from json import loads

from libelifoot.entity.player import Player
from libelifoot.provider.base_provider import BaseProvider


class EspnProvider(BaseProvider):

    # Cazaquistão, Curaçao, Eritreia, El salvador, French Guiana, Gibraltar,
    # Irã, Kosovo, Neocaledonia, Liechtenstein, Palestina and Saint Martin are
    # not mapped by the game
    _COUNTRIES = {
        'Afeganistão': 'AFG',
        'África do Sul': 'AFS',
        'Arábia Saudita': 'ASA',
        'Azerbaijão': 'AZB',
        'Bangladesh': 'BGD',
        'Benim': 'BNI',
        'Botsuana': 'BTW',
        'Cape Verde Islands': 'CAV',
        'Catar': 'QAT',
        'Chade': 'CHD',
        'Comoros Islands': 'CMR',
        'Congo (Brazavile)': 'CNG',
        'Costa do Marfim': 'CMF',
        'Costa Rica': 'CRC',
        'Chile': 'CHL',
        'China': 'CHN',
        'China PR': 'CHN',
        'Chipre': 'CHP',
        'Czechia': 'RCH',
        'Coreia do Sul': 'CRS',
        'Egito': 'EGT',
        'Emirados Árabes Unidos': 'EAU',
        'Eslováquia': 'EVQ',
        'Eslovênia': 'EVN',
        'Gana': 'GNA',
        'Gâmbia': 'GMB',
        'Granada': 'GRN',
        'Haiti': 'HTI',
        'Iraque': 'IRQ',
        'Mauritânia': 'MRT',
        'Maurício': 'MRC',
        'Namíbia': 'NMI',
        'Nova Zelândia': 'NZE',
        'País de Gales': 'WAL',
        'Trinidad e Tobago': 'TND',
        'USA': 'EUA',
        'Venezuela': 'VNZ',
        'Republic of Ireland': 'IRL',
        'República da Sérvia': 'SER',
        'República Democrática do Congo': 'CNG',
        'República Centro-Africana': 'RCA',
        'República Dominicana': 'RDO',
        'St Lucia': 'SLU',
        'St Kitts and Nevis': 'SKN',
        'Vietnã': 'VTM',
        'Zimbábue': 'ZBW'
    }

    # TODO: considerar o torneio
    def __init__(self):
        super().__init__('espn',
                         'https://www.espn.com.br/futebol/time/elenco/_/id/',
                         self._COUNTRIES,
                         lambda p: int(p.appearances))

    def assemble_team_data_uri(self, team_id: str, season: int) -> str:
        return f'{self._base_url}{team_id}/season/{season}' if season else \
            f'{self._base_url}{team_id}'

    def assemble_team_coach_uri(self, team_id: str) -> str:
        return ''

    def parse_coach_data(self, reply: str, season: int) -> str:
        return ''

    def parse_team_data(self, reply: str) -> list[Player]:
        start_str = ";window['__espnfitt__']="
        end_str = ";</script>"

        try:
            ret = loads(reply.split(start_str)[1].split(end_str)[0])
            groups = ret['page']['content']['squad']['groups']

            if not groups:
                return []

            goalkeepers = groups[0]['athletes']
            others = groups[1]['athletes']

            return self._parse_players(goalkeepers + others)
        except (IndexError, KeyError):
            return []

    def _get_player_name(self, player: dict) -> str:
        return player.get('name') \
            if len(player.get('name')) <= self._MAX_NAME_SIZE \
            else player.get('shortName')

    def _parse_players(self, data: list[dict]) -> list[Player]:
        players = []

        for player in data:
            if not player.get('ctz'): # ignore players with unknown country
                continue

            # TODO: discard players with unmaped countries

            players.append(
                Player(
                    name=self._get_player_name(player),
                    position=player.get('position'),
                    country=self.get_country(player.get('ctz')),
                    appearances=player.get('appearances', 0)
                )
            )

        return players
