import datetime
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from PeninsulaElectricDataSystem.transform.cleaning.filter_to_today_data import filter_to_today_data


class FilterToTodayDataShould(unittest.TestCase):
    def test_remain_data_from_other_days(self):
        column_date = 'date'
        today_dt = datetime.datetime.today()
        today = today_dt.strftime("%Y-%m-%d %H:%M")
        yesterday = (today_dt - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        tomorrow = (today_dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        init_data = pd.DataFrame([
            {column_date: yesterday, 'otros': 1},
            {column_date: today, 'otros': 1},
            {column_date: tomorrow, 'otros': 1}
        ])
        today_data = pd.DataFrame([
            {column_date: today, 'otros': 1},
        ])

        assert_frame_equal(
            filter_to_today_data(init_data, column_date),
            today_data
        )


if __name__ == '__main__':
    unittest.main()