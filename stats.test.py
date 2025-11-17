import unittest
import stats as statistics
import math


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Specify the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html
  
  def test_if_nan_in_input(self):
    computedStats = statistics.calculateStats([1.0, float('nan'), 3.0])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 2.0, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 3.0, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.0, delta=epsilon)
  
  def test_absurd_value_input(self):
    computedStats = statistics.calculateStats([1.0, 2.0, 1e100])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))


if __name__ == "__main__":  # pragma: no cover
  unittest.main()
