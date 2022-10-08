import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from PeninsulaElectricDataSystem.transform.cleaning.remove_duplicates_from_change_hour import \
    remove_duplicates_from_change_hour


class RemoveDuplicatesFromChangeHour(unittest.TestCase):

    def test_(self):
        column_date = 'date'
        init_data = pd.DataFrame([
            {column_date: "2021-02-12 1A:30", 'value': 2},
            {column_date: "2021-02-12 1B:30", 'value': 2},
            {column_date: "2021-02-12 2A:40", 'value': 2},
            {column_date: "2021-02-12 2B:40", 'value': 2},
        ])
        data_without_duplicates = pd.DataFrame(
            [
                {column_date: "2021-02-12 01:30", 'value': 2},
                {column_date: "2021-02-12 02:40", 'value': 2},
            ]
        )
        assert_frame_equal(
            remove_duplicates_from_change_hour(init_data,column_date),
            data_without_duplicates
        )


if __name__ == '__main__':
    unittest.main()