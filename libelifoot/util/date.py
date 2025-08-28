from datetime import datetime
from time import localtime


_DAYS_IN_YEAR = 365
_DATE_FORMAT = '%d/%m/%Y'


def _get_work_days_in_session(start: str, end: str) -> int:
    date_start = datetime.strptime(start, _DATE_FORMAT)

    if end:
        date_end = datetime.strptime(end, _DATE_FORMAT)
    else:
        lt = localtime()
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
    end_season_year = int(end.split('/')[2]) if end else localtime().tm_year

    if start_season_year == season == end_season_year:
        return _get_work_days_in_session(start, end)
    if (season == start_season_year) and (season != end_season_year):
        return _get_work_days_in_start_session(start, season)
    if season > start_season_year and season == end_season_year:
        return _get_work_days_in_end_session(end, season)
    if end_season_year > season > start_season_year:
        return _DAYS_IN_YEAR

    return 0
