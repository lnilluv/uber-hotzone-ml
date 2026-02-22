import argparse
from pathlib import Path

from uber_hotzone_ml.adapters.pickup_csv import PickupCsvAdapter
from uber_hotzone_ml.adapters.result_csv import ResultCsvAdapter
from uber_hotzone_ml.application.use_cases import build_hotzone_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Uber Hotzone CLI")
    parser.add_argument("--pickup-csv", required=True)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--top-k", type=int, default=50)
    args = parser.parse_args()

    build_hotzone_report(
        pickup_port=PickupCsvAdapter(),
        result_port=ResultCsvAdapter(),
        pickup_csv_path=Path(args.pickup_csv),
        output_path=Path(args.output_csv),
        top_k=args.top_k,
    )
    print(f"Hotzone report saved to {args.output_csv}")


if __name__ == "__main__":
    main()
