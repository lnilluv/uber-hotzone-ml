import csv
from datetime import datetime
from pathlib import Path


class PickupCsvAdapter:
    def load_pickups(self, csv_path: Path) -> list[dict]:
        rows: list[dict] = []
        with csv_path.open("r", encoding="utf-8", newline="") as file_handle:
            reader = csv.DictReader(file_handle)
            for row in reader:
                timestamp = datetime.strptime(row["Date/Time"], "%m/%d/%Y %H:%M:%S")
                lat = float(row["Lat"])
                lon = float(row["Lon"])
                zone = f"{round(lat, 2)},{round(lon, 2)}"
                rows.append(
                    {
                        "weekday": timestamp.strftime("%A"),
                        "hour": timestamp.hour,
                        "zone": zone,
                    }
                )
        return rows
