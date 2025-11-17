import math


def __validate_list(numbers):
  numbers = [x for x in numbers if not math.isnan(x)]  # ignoring the NaN value
  if any(x < 0 or x > 200 for x in numbers):  # avoid the sensor value batch if any absurd value
    return []
  return numbers

def calculateStats(numbers):
  numbers = __validate_list(numbers)
  if not numbers:
    return {"avg": math.nan, "min": math.nan, "max": math.nan}

  avg = sum(numbers) / len(numbers)
  min_val = min(numbers)
  max_val = max(numbers)

  return {"avg": avg, "min": min_val, "max": max_val}
