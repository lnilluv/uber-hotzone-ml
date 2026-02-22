import csv
from pathlib import Path


class ResultCsvAdapter:
    def save(self, rows: list[dict], output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="") as file_handle:
            writer = csv.DictWriter(file_handle, fieldnames=["weekday", "hour", "zone", "pickup_count"])
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
