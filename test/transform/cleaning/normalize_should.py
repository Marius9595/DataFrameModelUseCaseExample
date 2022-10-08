import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from PeninsulaElectricDataSystem.transform.cleaning.normalize import normalize


class NormalizeShould(unittest.TestCase):

    def setUp(self) -> None:
        self.init_data = pd.DataFrame([
            {"uno": 1, "dos": 2},
            {"uno": 1, "dos": 2}
        ])
        self.normalized_data = pd.DataFrame([
            {"one": 1, "two": 2},
            {"one": 1, "two": 2}
        ])

    def test_change_to_keys_predefined(self):
        dict_for_normalization = {
            "uno": "one",
            "dos": "two"
        }
        assert_frame_equal(
            normalize(self.init_data, dict_for_normalization),
            self.normalized_data
        )


if __name__ == '__main__':
    unittest.main()