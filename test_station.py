import unittest
import numpy as np
import station

class TestStation(unittest.TestCase):
    def test_get_df(self):
        dfs = station.get_df()
        self.assertEqual(5, len(dfs))
        self.assertEqual(10853, len(dfs["station"]))

    def test_pref_id(self):
        self.assertEqual(1, station.get_pref_cd("北海道"))
        self.assertEqual(13, station.get_pref_cd("東京都"))

        with self.assertRaises(ValueError, msg="東京 is not exist"):
            station.get_pref_cd("東京")

    def test_get_lat_lng(self):
        np.testing.assert_array_almost_equal(np.array([41.773709, 140.726413]), station.get_lat_lng_from_station_name("函館"))
        np.testing.assert_array_almost_equal(np.array([35.681391, 139.766103]), station.get_lat_lng_from_station_name("東京"))

        with self.assertRaises(ValueError, msg="hogehoge is not exist"):
            station.get_lat_lng_from_station_name("hogehoge")
