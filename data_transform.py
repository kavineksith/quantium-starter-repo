import csv
from pathlib import Path

DATA_DIRECTORY = Path("./data")
OUTPUT_FILE_PATH = Path("./formatted_data.csv")

HEADER = ["sales", "date", "region"]
TARGET_PRODUCT = "pink morsel"


def calculate_sale(price: str, quantity: str) -> float:
    """Calculate total sale amount."""
    cleaned_price = float(price.replace("$", ""))
    return cleaned_price * int(quantity)


def process_row(row: list[str]) -> list:
    """Process a single CSV row and return formatted output."""
    product, raw_price, quantity, transaction_date, region = row

    if product != TARGET_PRODUCT:
        return None

    sale = calculate_sale(raw_price, quantity)

    return [sale, transaction_date, region]


def process_file(file_path: Path, writer: csv.writer) -> None:
    """Read and process a single CSV file."""
    with file_path.open(mode="r", newline="") as input_file:
        reader = csv.reader(input_file)

        # Skip header row
        next(reader, None)

        for row in reader:
            processed_row = process_row(row)

            if processed_row:
                writer.writerow(processed_row)


def main() -> None:
    """Main application entry point."""
    with OUTPUT_FILE_PATH.open(mode="w", newline="") as output_file:
        writer = csv.writer(output_file)

        # Write CSV header
        writer.writerow(HEADER)

        # Process all CSV files in data directory
        for file_path in DATA_DIRECTORY.iterdir():
            if file_path.suffix == ".csv":
                process_file(file_path, writer)


if __name__ == "__main__":
    main()