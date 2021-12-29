# flatex2parquet

Convert flatex' CSV output to a format that [parqet](https://www.parqet.com/)
understands.

## Dependencies

* A recent version of Python. I tested 3.8.
* Optional: poetry.

## Usage

With (plain) Python:

```
python flatex2parquet.py Depotumsaetze.csv -o parquet.csv
```

With poetry:

```
poetry run flatex2parquet Depotumsaetze.csv -o parquet.csv
```

## Limitations

* No fees and taxes
* Expiration and knockouts are treated as "Sell"
* No support for types other than "Buy" and "Sell"
