from libelifoot.util.date import get_work_days_in_season


def test_get_work_days_in_season_less_than_one_year():
    assert get_work_days_in_season(2020, '15/03/2020', '20/06/2020') == 97


def test_get_work_days_in_season_more_than_one_year():
    assert get_work_days_in_season(2020, '15/03/2020', '20/06/2021') == 291


def test_get_work_days_in_season_full_year():
    assert get_work_days_in_season(2020, '01/01/2020', '20/06/2021') == 365


def test_get_work_days_in_season_end_year():
    assert get_work_days_in_season(2021, '15/03/2020', '20/06/2021') == 170
