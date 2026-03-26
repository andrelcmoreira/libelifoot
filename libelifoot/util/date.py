# Copyright (C) 2025 André L. C. Moreira <andrelcmoreira@proton.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from datetime import datetime

import time


_DAYS_IN_YEAR = 365
_DATE_FORMAT = '%d/%m/%Y'


def _get_work_days_in_session(start: str, end: str) -> int:
    date_start = datetime.strptime(start, _DATE_FORMAT)

    if end:
        date_end = datetime.strptime(end, _DATE_FORMAT)
    else:
        lt = time.localtime()
        date_end = datetime(year=lt.tm_year, month=lt.tm_mon, day=lt.tm_mday)

    diff = date_end - date_start

    return diff.days


def _get_work_days_in_end_session(end: str, season: int) -> int:
    date_start = datetime.strptime(f"01/01/{season}", _DATE_FORMAT)
    date_end = datetime.strptime(end, _DATE_FORMAT)
    diff = date_end - date_start

    return diff.days


def _get_work_days_in_start_session(start: str, season: int) -> int:
    date_start = datetime.strptime(start, _DATE_FORMAT)
    date_end = datetime.strptime(f"31/12/{season}", _DATE_FORMAT)
    diff = date_end - date_start

    return diff.days


def get_work_days_in_season(season: int, start: str, end: str) -> int:
    start_season_year = int(start.split('/')[2])
    end_season_year = int(end.split('/')[2]) if end else time.localtime().tm_year

    if start_season_year == season == end_season_year:
        return _get_work_days_in_session(start, end)
    if (season == start_season_year) and (season != end_season_year):
        return _get_work_days_in_start_session(start, season)
    if season > start_season_year and season == end_season_year:
        return _get_work_days_in_end_session(end, season)
    if end_season_year > season > start_season_year:
        return _DAYS_IN_YEAR

    return 0
