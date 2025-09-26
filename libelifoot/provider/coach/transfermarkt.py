from bs4 import BeautifulSoup

from libelifoot.provider.coach_provider import CoachProvider
from libelifoot.util.date import get_work_days_in_season


class TransfermarktProvider(CoachProvider):

    _USER_AGENT = 'libelifoot'
    _REQUEST_TIMEOUT = 30

    def __init__(self):
        super().__init__('transfermarkt', 'https://transfermarkt.com.br/', 5)

    def assemble_coach_uri(self, team_id: str) -> str:
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

                if (str(season) in start) and (end == ''):
                    coach = name
                    break

                days_in_season = get_work_days_in_season(season, start, end)
                if days_in_season > days:
                    coach = name
                    days = days_in_season
            except IndexError:
                continue

        return coach
