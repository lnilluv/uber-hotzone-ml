import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from uber_hotzone_ml.application.ports import PickupPort, ResultPort
from uber_hotzone_ml.application.use_cases import build_hotzone_report


class FakePickupAdapter(PickupPort):
    def load_pickups(self, csv_path: Path) -> list[dict]:
        return [{"weekday": "Monday", "hour": 8, "zone": "40.7,-74.0"}]


class FakeResultAdapter(ResultPort):
    def __init__(self) -> None:
        self.saved = False

    def save(self, rows: list[dict], output_path: Path) -> None:
        self.saved = True


class UseCaseTests(unittest.TestCase):
    def test_build_hotzone_report_saves_output(self) -> None:
        pickup_adapter = FakePickupAdapter()
        result_adapter = FakeResultAdapter()

        build_hotzone_report(
            pickup_port=pickup_adapter,
            result_port=result_adapter,
            pickup_csv_path=Path("pickup.csv"),
            output_path=Path("hotzones.csv"),
            top_k=1,
        )

        self.assertTrue(result_adapter.saved)


if __name__ == "__main__":
    unittest.main()
