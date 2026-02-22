import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from uber_hotzone_ml.domain.hotzones import aggregate_hotzones


class HotzoneDomainTests(unittest.TestCase):
    def test_aggregate_hotzones_returns_ranked_results(self) -> None:
        rows = [
            {"weekday": "Monday", "hour": 8, "zone": "40.7,-74.0"},
            {"weekday": "Monday", "hour": 8, "zone": "40.7,-74.0"},
            {"weekday": "Monday", "hour": 8, "zone": "40.8,-73.9"},
        ]

        result = aggregate_hotzones(rows, top_k=1)
        self.assertEqual(result, [{"weekday": "Monday", "hour": 8, "zone": "40.7,-74.0", "pickup_count": 2}])


if __name__ == "__main__":
    unittest.main()
