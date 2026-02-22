from pathlib import Path
from typing import Protocol


class PickupPort(Protocol):
    def load_pickups(self, csv_path: Path) -> list[dict]: ...


class ResultPort(Protocol):
    def save(self, rows: list[dict], output_path: Path) -> None: ...
