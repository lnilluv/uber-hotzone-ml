from collections import defaultdict


def aggregate_hotzones(rows: list[dict], top_k: int) -> list[dict]:
    grouped: dict[tuple[str, int, str], int] = defaultdict(int)

    for row in rows:
        key = (str(row["weekday"]), int(row["hour"]), str(row["zone"]))
        grouped[key] += 1

    ranked = sorted(grouped.items(), key=lambda item: (-item[1], item[0][0], item[0][1], item[0][2]))
    top_rows = ranked[:top_k]

    result: list[dict] = []
    for (weekday, hour, zone), count in top_rows:
        result.append(
            {
                "weekday": weekday,
                "hour": hour,
                "zone": zone,
                "pickup_count": count,
            }
        )
    return result
