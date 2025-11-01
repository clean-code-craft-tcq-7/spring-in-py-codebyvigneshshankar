import unittest
import stats as statistics


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([98.6, 98.2, 97.8, 102.2])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 99.2, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 102.2, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 97.8, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Specify the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html


if __name__ == "__main__":
  unittest.main()
