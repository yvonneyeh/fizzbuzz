import unittest
from pingout import pingout


class TestPingout(unittest.TestCase):

    def test_first_check(self):
            i = 1
            print('Testing:', i)
            assert pingout(i) == "PING"

    def test_check_signal_strength(self):
        for i in [3, 6, 9, 18]:
            print('Testing:', i)
            assert pingout(i) == "CHECK_SIGNAL_STRENGTH"

    def test_check_channel_noise(self):
        for i in [5, 10, 50]:
            print('Testing:', i)
            assert pingout(i) == "CHECK_CHANNEL_NOISE"

    def test_scan_for_towers(self):
        for i in [15, 30, 75]:
            print('Testing:', i)
            assert pingout(i) == "SCAN_FOR_TOWERS"

if __name__ == '__main__':
    unittest.main()
