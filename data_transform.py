import argparse
from pathlib import Path

import pandas as pd


def load_and_process_csvs(data_dir: Path) -> pd.DataFrame:
    csv_files = sorted(data_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")

    df_list = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df_list.append(df)

    combined = pd.concat(df_list, ignore_index=True)
    pink_morsels = combined[combined["product"] == "Pink Morsel"].copy()
    pink_morsels["Sales"] = pink_morsels["quantity"] * pink_morsels["price"]

    result = pink_morsels[["Sales", "date", "region"]].rename(
        columns={"date": "Date", "region": "Region"}
    )

    return result


def main():
    parser = argparse.ArgumentParser(description="Combine and format Soul Foods sales data.")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Folder containing the daily_sales_data CSV files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("formatted_sales.csv"),
        help="Output CSV file path.",
    )
    args = parser.parse_args()

    formatted = load_and_process_csvs(args.data_dir)
    formatted.to_csv(args.output, index=False)
    print(f"Wrote formatted sales data to {args.output}")


if __name__ == "__main__":
    main()