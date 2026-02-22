from pathlib import Path

from uber_hotzone_ml.application.ports import PickupPort, ResultPort
from uber_hotzone_ml.domain.hotzones import aggregate_hotzones


def build_hotzone_report(
    pickup_port: PickupPort,
    result_port: ResultPort,
    pickup_csv_path: Path,
    output_path: Path,
    top_k: int,
) -> None:
    rows = pickup_port.load_pickups(pickup_csv_path)
    report = aggregate_hotzones(rows, top_k)
    result_port.save(report, output_path)
