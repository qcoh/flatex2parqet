# flatex2parquet

Convert flatex' CSV output to a format that [parqet](https://www.parqet.com/)
understands.

## Dependencies

* A recent version of Python. I tested 3.8.
* Optional: poetry.

## Usage

With (plain) Python:

```
python cli.py Depotumsaetze.csv -o parqet.csv
```

With poetry:

```
poetry run flatex2parqet Depotumsaetze.csv -o parqet.csv
```

## Limitations

* No fees and taxes
* Expiration and knockouts are treated as "Sell"
* No support for types other than "Buy" and "Sell"
