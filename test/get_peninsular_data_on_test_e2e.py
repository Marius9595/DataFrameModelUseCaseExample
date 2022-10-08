import unittest
import datetime

from PeninsulaElectricDataSystem import peninsula
from PeninsulaElectricDataSystem.transform.DataFrameModels.peninsula import PeninsularData


class get_data_e2e(unittest.TestCase):
    def setUp(self) -> None:
        self.today = datetime.datetime.today()

    def test_should_works(self):
        peninsula.get_data_on(self.today)

    def test_should_return_correct_dataframeModel(self):
        self.assertTrue(isinstance(
                peninsula.get_data_on(self.today),
                PeninsularData
            )
        )

    def test_return_not_empty_dataframe(self):
        peninsulardata = peninsula.get_data_on(self.today).data
        self.assertTrue(
            peninsulardata.shape[0] > 0
            and
            peninsulardata.shape[1] > 1
        )

if __name__ == '__main__':
    unittest.main()