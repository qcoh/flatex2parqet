"""
Convert Flatex portfolio transactions CSV to parqet.

Usage (plain Python):
    python cli.py path/to/input.csv [-o path/to/output.csv]

Usage (poetry):
    poetry run flatex2parqet path/to/input.csv [-o path/to/output.csv]

References:
    https://www.parqet.com/blog/csv
"""

import argparse
import csv
import sys

# empty last column due to parsing error
# (see https://community.parqet.com/c/discussions/csv-import)
PARQET_FIELDNAMES = ["date", "fee", "isin", "price", "shares", "tax", "type", ""]


def main():
    parser = argparse.ArgumentParser(description="Convert flatex CSV to parqet CSV")
    parser.add_argument(
        "input",
        help="Path to flatex CSV",
        type=argparse.FileType("r", encoding="latin-1"),
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to output file",
        type=argparse.FileType("w"),
        default=sys.stdout,
    )
    args = parser.parse_args()

    parqet_writer = csv.DictWriter(
        args.output, PARQET_FIELDNAMES, delimiter=";", quoting=csv.QUOTE_NONE
    )
    parqet_writer.writeheader()
    flatex_reader = csv.DictReader(args.input, delimiter=";")

    for flatex_row in flatex_reader:
        parqet_row = {}

        parqet_row["date"] = flatex_row["Buchtag"]
        parqet_row["isin"] = flatex_row["ISIN"]
        parqet_row["shares"] = flatex_row["Nominal"].replace("-", "")
        parqet_row["price"] = flatex_row["Kurs"]

        # Don't know how to do this at the moment.
        parqet_row["tax"] = 0
        parqet_row["fee"] = 0

        if "ORDER Kauf" in flatex_row["Buchungsinformationen"]:
            parqet_row["type"] = "Buy"
        elif "ORDER Verkauf" in flatex_row["Buchungsinformationen"]:
            parqet_row["type"] = "Sell"
        elif "Ablauf" in flatex_row["Buchungsinformationen"]:
            parqet_row["type"] = "Sell"
        elif "vorz. KO" in flatex_row["Buchungsinformationen"]:
            parqet_row["type"] = "Sell"
        else:
            # e.g. "Thesaurierung", not sure how to do this.
            continue

        parqet_writer.writerow(parqet_row)


if __name__ == "__main__":
    main()
