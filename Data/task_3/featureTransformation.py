import unittest
import numpy as np

def cyclical_time_encoding(time):
    angle = (2 * np.pi * time) / 24
    return np.sin(angle), np.cos(angle)


class TestCyclicalTimeEncoding(unittest.TestCase):
    def test_midnight(self):
        sin, cos = cyclical_time_encoding(0)
        self.assertAlmostEqual(sin, 0.0)
        self.assertAlmostEqual(cos, 1.0)

    def test_noon(self):
        sin, cos = cyclical_time_encoding(12)
        self.assertAlmostEqual(sin, 0.0)
        self.assertAlmostEqual(cos, -1.0)

    def test_six_am(self):
        sin, cos = cyclical_time_encoding(6)
        self.assertAlmostEqual(sin, 1.0)
        self.assertAlmostEqual(cos, 0.0)

    def test_six_pm(self):
        sin, cos = cyclical_time_encoding(18)
        self.assertAlmostEqual(sin, -1.0)
        self.assertAlmostEqual(cos, 0.0)

    def test_difference_23_01(self):
        sin1, cos1 = cyclical_time_encoding(23)
        sin2, cos2 = cyclical_time_encoding(1)
        angle1 = np.arctan2(sin1, cos1)
        angle2 = np.arctan2(sin2, cos2)
        difference = (angle2 - angle1) % (2 * np.pi)
        self.assertAlmostEqual(difference, np.deg2rad(30))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)