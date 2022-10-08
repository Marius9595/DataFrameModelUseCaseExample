import unittest

import pandas as pd
from pandas.testing import assert_series_equal

from PeninsulaElectricDataSystem.transform.formating.format_decimals import format_decimals


class FormatDecimalsShould(unittest.TestCase):
    def setUp(self) -> None:
        self.column_date = 'date'
        self.init_data = pd.DataFrame([
            {self.column_date: "una_fecha", "prueba": 2.3242323},
            {self.column_date: "una_fecha", "prueba": 2.322513123}
        ])
        self.data_formated = pd.DataFrame([
            {self.column_date: "una_fecha", "prueba": 2.324},
            {self.column_date: "una_fecha", "prueba": 2.323}
        ])

    def test_(self):
        assert_series_equal(
            format_decimals(self.init_data, self.column_date)['prueba'],
            self.data_formated['prueba']
        )


if __name__ == '__main__':
    unittest.main()