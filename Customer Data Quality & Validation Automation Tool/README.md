# Customer Data Quality & Validation Automation Tool

This command-line capstone reads customer records from `customers.csv`, validates required fields and formats, detects duplicates, and writes clean and rejected records.

# Commands to run the project
Open PowerShell in the project folder:

cd "C:\Users\yashk\OneDrive\Desktop\Customer Data Quality & Validation Automation Tool"

1. Run the application
python main.py

If python is not recognized, use:
C:\python312\python.exe main.py

2. Run the unit tests
python -m unittest tests.py

Or:
C:\python312\python.exe -m unittest tests.py

Expected result:
Ran 8 tests

OK

3. Run tests with more detail
python -m unittest -v tests.py


4. View the generated files
>>> Get-ChildItem

To display the report:

>>> Get-Content quality_report.txt

To display rejected records:
>>> Get-Content rejected_customers.csv

To display the log:
>>> Get-Content customer_quality.log

s

## Run

```text
python main.py
python -m unittest tests.py
```

If `customers.csv` does not exist, the application creates a fictional demonstration dataset. An existing input file is never overwritten.

## Input schema

`customer_id`, `name`, `email`, `phone`, `city`, and `date_of_registration`.

All six fields are required. Email validation uses a practical regular expression and checks format only; it does not prove that an address exists. Phone numbers must be exactly 10 digits and begin with 6, 7, 8, or 9. Registration dates must be real dates in `YYYY-MM-DD` format.

## Duplicate policy

The first occurrence of an ID or exact row can be accepted if otherwise valid. Every later occurrence is rejected. Duplicate tracking is performed consistently even when the first row is invalid. A rejected row can have multiple semicolon-separated reasons, while record counts still count it only once.

## Generated files

- `valid_customers.csv`: accepted records.
- `rejected_customers.csv`: original fields plus `error_reasons`.
- `quality_report.txt`: record counts, error counts, quality percentage, and conclusion.
- `customer_quality.log`: timestamped processing events and failures.

The quality percentage is `(valid records / total records processed) * 100`; it is `0.00%` when no records are present. Missing-field and format counts are validation-error counts, so one record may contribute to multiple counts.

## Core Python concepts

The project uses `csv`, `re`, `datetime`, `logging`, `pathlib`, lists, dictionaries, sets, `Counter`, functions, comprehensions, and exception handling. It has no third-party dependencies.

## Limitations

Format checks do not confirm that emails or phone numbers are active. The CSV structure must contain all required headers. Unexpected columns are logged and ignored.
