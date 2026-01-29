"""
Extract earthquakes data from USGS API.
Saves raw data to data/raw/earthquakes_last_15_days.csv
"""

import os
from datetime import datetime, timedelta

import requests
import pandas as pd


def fetch_earthquakes_last_15_days() -> pd.DataFrame:
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=15)

    start_str = start_time.strftime("%Y-%m-%d")
    end_str = end_time.strftime("%Y-%m-%d")

    url = (
        "https://earthquake.usgs.gov/fdsnws/event/1/query"
        f"?format=geojson&starttime={start_str}&endtime={end_str}"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    features = data.get("features", [])

    rows = []
    for f in features:
        props = f.get("properties", {})
        geom = f.get("geometry", {})
        coords = geom.get("coordinates", [None, None, None])  # [lon, lat, depth]

        rows.append(
            {
                "id": f.get("id"),
                "time_ms": props.get("time"),
                "place": props.get("place"),
                "mag": props.get("mag"),
                "type": props.get("type"),
                "url": props.get("url"),
                "longitude": coords[0],
                "latitude": coords[1],
                "depth_km": coords[2],
            }
        )

    df = pd.DataFrame(rows)

    if "time_ms" in df.columns:
        df["time_utc"] = pd.to_datetime(df["time_ms"], unit="ms", utc=True)

    return df


def save_raw(df: pd.DataFrame, out_dir: str = "data/raw") -> str:
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "earthquakes_last_15_days.csv")
    df.to_csv(out_path, index=False)
    return out_path


if __name__ == "__main__":
    df = fetch_earthquakes_last_15_days()
    path = save_raw(df)

    print(f"Extract OK ✅ Rows: {len(df)}")
    print(f"Saved to: {path}")
    print(df.head(5))
