"""Customer Data Quality & Validation Automation Tool.

This module loads, validates, classifies, and reports customer data.
"""

# Standard-library modules used for CSV files, logging, patterns, dates, and paths.

from __future__ import annotations # What does this __future__ import annotations do? It allows for postponed evaluation of type annotations, which can help with forward references and improve performance in some cases.

import csv # this module provides functionality to read from and write to CSV files, making it easier to handle tabular data in a structured format.
import logging # this module provides a flexible framework for emitting log messages from Python programs, allowing developers to track events and issues during execution.
import re # this module provides support for regular expressions, enabling pattern matching and text manipulation in strings.
import sys # this module provides access to system-specific parameters and functions, allowing interaction with the interpreter and command-line arguments.
from collections import Counter # this module provides a convenient way to count occurrences of elements in an iterable, returning a dictionary-like object that maps elements to their counts.
from datetime import datetime # this module provides classes for manipulating dates and times, allowing for date arithmetic, formatting, and parsing.
from pathlib import Path # this module provides an object-oriented interface for working with filesystem paths, making it easier to handle file and directory operations across different operating systems.
from typing import Dict, Iterable, List, Tuple 

APPLICATION_NAME = "Customer Data Quality & Validation Automation Tool"
# These are the six columns required in every customer input record.
FIELDS = [
    "customer_id",
    "name",
    "email",
    "phone",
    "city",
    "date_of_registration",
]
# Compile validation patterns once so repeated checks are efficient and consistent.
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$") # this pattern matches a basic email format with a local part, an '@' symbol, and a domain part with at least one dot.
PHONE_PATTERN = re.compile(r"^[6-9]\d{9}$") # this pattern matches a 10-digit phone number starting with digits 6, 7, 8, or 9.

# this custom exception class is defined to handle errors related to input data processing. It is raised when the input file cannot be safely processed, allowing the application to catch and handle these specific errors in a controlled manner.
class InputDataError(Exception):
    """Raised when the input file cannot be safely processed."""

# this function configures the logging system to write timestamped messages to a specified log file. It sets the logging level to DEBUG, ensuring that all messages of this level and above are captured. The log format includes the timestamp, log level, and message content. The force=True parameter ensures that any previous logging configuration is overridden, allowing for consistent logging behavior throughout the application.
def configure_logging(log_path: Path) -> None:
    """Configure readable timestamped messages in the execution log."""
    # force=True replaces any previous test or application logging configuration.
    logging.basicConfig(
        filename=log_path,
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        force=True,
    )

# this function creates a sample input CSV file at the specified path if it does not already exist. The sample data includes a variety of valid, invalid, incomplete, and duplicate records to demonstrate the validation capabilities of the application. It ensures that the parent directory exists before writing the file and uses CSV escaping rules to write the header and sample rows.
def create_sample_input(path: Path) -> None:
    """Create the demonstration dataset only when no input file exists."""
    # Never overwrite a user-provided dataset.
    if path.exists():
        return
    # The sample rows intentionally include valid, invalid, incomplete, and duplicate data.
    rows = [
        ["C001", "Aarav Sharma", "aarav@example.com", "9876543210", "Delhi", "2026-01-10"],
        ["C002", "Priya Patel", "priya.patel@example.com", "8765432109", "Mumbai", "2026-02-15"],
        ["C003", "Rahul Verma", "rahul@gmail.com", "7654321098", "Pune", "2025-12-01"],
        ["C004", "Neha Singh", "neha@example.com", "9123456780", "Jaipur", "2026-03-05"],
        ["C005", "Vikram Rao", "vikram@", "9876501234", "Chennai", "2026-01-22"],
        ["C006", "", "missing.name@example.com", "9876543211", "Kochi", "2026-01-12"],
        ["C007", "Amit Joshi", "amitgmail.com", "9876543212", "Indore", "2026-01-14"],
        ["C008", "Sara Khan", "sara@example.com", "123", "Bhopal", "2026-01-16"],
        ["C009", "Rohan Das", "rohan@example.com", "98765abc10", "Surat", "2026-01-18"],
        ["C010", "Meera Nair", "meera@example.com", "9876543214", "", "2026-01-20"],
        ["C011", "Dev Mehta", "dev@example.com", "9876543215", "Delhi", "2026-02-30"],
        ["C012", "Isha Roy", "isha@example.com", "9876543216", "Kolkata", "invalid-date"],
        ["C013", "Kabir Shah", "kabir@example.com", "9876543217", "Nagpur", "2026-02-10"],
        ["C013", "Duplicate ID", "duplicate@example.com", "9876543218", "Nagpur", "2026-02-11"],
        ["C014", "  Anil Gupta  ", " anil@example.com ", " 9876543219 ", "  Noida ", " 2026-02-12 "],
        ["", "No ID", "noid@example.com", "9876543220", "Agra", "2026-02-13"],
        ["C015", "Missing Email", "", "9876543221", "Goa", "2026-02-14"],
        ["C016", "Missing Phone", "nophone@example.com", "", "Mysuru", "2026-02-16"],
        ["C017", "Missing City", "nocity@example.com", "9876543223", "", "2026-02-17"],
        ["C018", "Multiple Errors", "bad-email", "111", "", "not-a-date"],
        ["C003", "Rahul Verma", "rahul@gmail.com", "7654321098", "Pune", "2025-12-01"],
    ]
    # Create the parent folder before opening the input file.
    path.parent.mkdir(parents=True, exist_ok=True)
    # Write the header followed by all sample rows using CSV escaping rules.
    with path.open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerows([FIELDS, *rows]) # The `writerows` method writes multiple rows to the CSV file, starting with the header defined in `FIELDS`, followed by the sample data rows. The `*rows` syntax unpacks the list of sample rows so that each row is written as a separate line in the CSV file.

# this function reads a CSV file from the specified path, normalizes the customer fields, and validates the structure of the CSV. It checks for required columns, trims whitespace, and handles missing or extra columns. It also processes each row to ensure that all required fields are present and properly formatted, returning a list of normalized records for further processing.
def load_customers(path: Path) -> List[Dict[str, str]]:
    """Load and normalize customer fields, validating the CSV structure."""
    try:
        # utf-8-sig reads normal UTF-8 and also removes an optional BOM from the header.
        with path.open("r", newline="", encoding="utf-8-sig") as handle:
            # DictReader maps each row to a dictionary using the first row as column names.
            reader = csv.DictReader(handle)
            # No fieldnames means the file has no usable header.
            if reader.fieldnames is None:
                raise InputDataError("The CSV file is empty or has no header row.")
            # Trim header whitespace before comparing names with the required schema.
            headers = [header.strip() for header in reader.fieldnames if header is not None]
            # Find every required column that is missing instead of reporting only one.
            missing = [field for field in FIELDS if field not in headers]
            if missing:
                raise InputDataError("Missing required column(s): " + ", ".join(missing))
            # Extra columns are allowed, but they are reported and ignored.
            unexpected = [header for header in headers if header not in FIELDS]
            if unexpected:
                logging.warning("Ignoring unexpected column(s): %s", ", ".join(unexpected))
            # Keep every data row so invalid rows can be exported with their reasons.
            records = []
            # Data starts on CSV line 2 because line 1 contains the header.
            for row_number, row in enumerate(reader, start=2):
                # Replace missing cells with empty strings and trim surrounding whitespace.
                values = {field: (row.get(field) or "").strip() for field in FIELDS}
                # A None value means the row had fewer cells than the header.
                if any(value is None for value in row.values()):
                    logging.warning("Incomplete record at CSV row %d", row_number)
                # Add the normalized row to the list sent to validation.
                records.append(values)
            # Return all normalized rows to the processing stage.
            return records
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, csv.Error) as exc:
        # Convert common input failures into one clear application-specific exception.
        raise InputDataError(f"Unable to read input file '{path.name}': {exc}") from exc

# this function checks for missing required fields in a given record (dictionary) and returns a list of error messages for each missing field. It iterates over the predefined FIELDS list and checks if each field is present and non-empty in the record. If a field is missing or empty, it adds an error message to the list, which is then returned to the caller.
def validate_required_fields(record: Dict[str, str]) -> List[str]:
    """Return an error for every required field that is empty."""
    # The comprehension intentionally collects all missing fields from one record.
    return [f"missing required field: {field}" for field in FIELDS if not record.get(field, "").strip()]

# this function checks if a given email address matches a predefined regular expression pattern for valid email formats. It first strips any leading or trailing whitespace from the email string and then uses the compiled EMAIL_PATTERN to check for a full match. If the email is non-empty and matches the pattern, it returns True; otherwise, it returns False, indicating an invalid email format.
def validate_email(email: str) -> bool:
    """Return True when the email matches the project's practical format rule."""
    # Strip outer spaces, then require the complete value to match the regex.
    return bool(email and EMAIL_PATTERN.fullmatch(email.strip()))

# this function checks if a given phone number is a valid 10-digit mobile number that starts with the digits 6, 7, 8, or 9. It first strips any leading or trailing whitespace from the phone string and then uses the compiled PHONE_PATTERN to check for a full match. If the phone number is non-empty and matches the pattern, it returns True; otherwise, it returns False, indicating an invalid phone format.
def validate_phone(phone: str) -> bool:
    """Return True for a 10-digit mobile number beginning with 6, 7, 8, or 9."""
    # Strip outer spaces, then require every character to match the phone regex.
    return bool(phone and PHONE_PATTERN.fullmatch(phone.strip()))

# this function checks if a given registration date string is a valid date in the format YYYY-MM-DD. It attempts to parse the date using datetime.strptime, which will raise an exception for impossible dates (e.g., February 30). Additionally, it uses a regular expression to ensure that the input has exactly four digits for the year, two digits for the month, and two digits for the day. If both checks pass, it returns True; otherwise, it returns False.
def validate_registration_date(value: str) -> bool:
    """Return True only for a real date written as YYYY-MM-DD."""
    try:
        # strptime rejects impossible calendar dates such as 2026-02-30.
        datetime.strptime(value.strip(), "%Y-%m-%d")
        # The regex confirms the input has exactly four, two, and two digits.
        return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value.strip()))
    except (TypeError, ValueError):
        # Bad text and impossible dates are both invalid.
        return False

# this function detects duplicate customer IDs and exact duplicate records in a list of customer records. It uses sets to track seen IDs and complete rows, and counters to record the indexes of later duplicate occurrences. The function returns two counters: one for duplicate customer IDs and another for exact duplicate records, allowing the caller to classify and report duplicates effectively.
def detect_duplicates(records: Iterable[Dict[str, str]]) -> Tuple[Counter, Counter]:
    """Return counts of repeated IDs and exact rows, keyed by record index."""
    # Sets make it efficient to check whether an ID or complete row was seen earlier.
    ids = set()
    rows = set()
    # Counters store the indexes of later duplicate occurrences.
    duplicate_ids = Counter()
    duplicate_rows = Counter()
    # Enumerate rows so duplicate results can be matched to the original record.
    for index, record in enumerate(records):
        # A tuple is hashable, so all six normalized fields can be stored in a set.
        identity = tuple(record[field] for field in FIELDS)
        # An ID already in the set is a duplicate; otherwise remember its first occurrence.
        if record["customer_id"] in ids:
            duplicate_ids[index] += 1
        else:
            ids.add(record["customer_id"])
        # Compare the complete normalized row for exact duplicate detection.
        if identity in rows:
            duplicate_rows[index] += 1
        else:
            rows.add(identity)
    # Return both duplicate categories for use during classification.
    return duplicate_ids, duplicate_rows

# this function processes a list of customer records by validating each record against required fields, email format, phone format, and registration date format. It also checks for duplicate customer IDs and exact duplicate records. The function returns three values: a list of valid records, a list of rejected records with error reasons, and a Counter object containing counts of various validation errors encountered during processing.
def process_records(records: List[Dict[str, str]]) -> Tuple[List[Dict[str, str]], List[Dict[str, str]], Counter]:
    """Validate every record and return valid rows, rejected rows, and error counts."""
    # Detect duplicates before validating so the duplicate policy is consistent.
    duplicate_ids, duplicate_rows = detect_duplicates(records)
    # These lists contain records at the record level, while errors counts are independent.
    valid, rejected = [], []
    errors = Counter()
    # Process each input row exactly once.
    for index, record in enumerate(records):
        # Begin with every missing-field reason for this row.
        reasons = validate_required_fields(record)
        # Validate non-empty email values and count malformed values.
        if record["email"] and not validate_email(record["email"]):
            reasons.append("invalid email format")
            errors["invalid email"] += 1
        # Validate non-empty phone values and count malformed values.
        if record["phone"] and not validate_phone(record["phone"]):
            reasons.append("invalid phone format")
            errors["invalid phone"] += 1
        # Validate non-empty registration dates and count malformed values.
        if record["date_of_registration"] and not validate_registration_date(record["date_of_registration"]):
            reasons.append("invalid registration date (expected YYYY-MM-DD)")
            errors["invalid registration date"] += 1
        # Count each missing-field reason, even when one row has several.
        for reason in reasons:
            if reason.startswith("missing required field"):
                errors["missing required field"] += 1
        # Add duplicate reasons to the same list as field and format reasons.
        if index in duplicate_ids:
            reasons.append("duplicate customer ID")
            errors["duplicate customer ID"] += 1
        # An exact duplicate is tracked separately from a duplicate ID.
        if index in duplicate_rows:
            reasons.append("exact duplicate record")
            errors["exact duplicate record"] += 1
        # Reject a row once if it has one or more reasons, preserving all reasons.
        if reasons:
            rejected.append({**record, "error_reasons": "; ".join(reasons)})
        else:
            # Only a row with no validation or duplicate reasons is accepted.
            valid.append(record)
    # Store aggregate duplicate counts for the report and terminal summary.
    errors["duplicate customer ID count"] = sum(duplicate_ids.values())
    errors["exact duplicate record count"] = sum(duplicate_rows.values())
    # Return record collections and the detailed error counter to the caller.
    return valid, rejected, errors

# this function writes a list of dictionaries to a CSV file at the specified path, using the provided field names as column headers. It opens the file in write mode with UTF-8 encoding and ensures that no extra blank lines are added on Windows. The function uses csv.DictWriter to write the header and all rows, and it raises an InputDataError if there are any issues with file permissions or other OS-related errors during writing.
def write_csv(path: Path, rows: List[Dict[str, str]], fields: List[str]) -> None:
    try:
        # newline="" prevents extra blank lines when CSV files are written on Windows.
        with path.open("w", newline="", encoding="utf-8") as handle:
            # DictWriter writes dictionary values under the requested column names.
            writer = csv.DictWriter(handle, fieldnames=fields)
            # Always write a header, even when there are no records.
            writer.writeheader()
            # Write all records using the same column order as the header.
            writer.writerows(rows)
    except (PermissionError, OSError) as exc:
        # Surface write failures instead of logging a false success.
        raise InputDataError(f"Unable to write '{path.name}': {exc}") from exc

# this function generates a quality report summarizing the processing statistics of customer records. It calculates the overall data-quality percentage based on valid and total records, compiles a list of report lines including counts of valid, rejected, and error types, and writes the report to a specified text file. The function handles potential file writing errors by raising an InputDataError if it cannot write to the specified path.
def generate_quality_report(path: Path, input_name: str, total: int, valid: int, rejected: int, errors: Counter) -> None:
    """Write processing statistics and an explanation of the quality percentage."""
    # Protect the calculation from division by zero for an empty input.
    percentage = (valid / total * 100) if total else 0.0
    # Build the complete report in a list before writing it to disk.
    lines = [
        APPLICATION_NAME,
        f"Report generation timestamp: {datetime.now().isoformat(timespec='seconds')}",
        f"Input file name: {input_name}",
        "",
        f"Total records processed: {total}",
        f"Valid record count: {valid}",
        f"Rejected record count: {rejected}",
        f"Duplicate customer ID count: {errors['duplicate customer ID count']}",
        f"Exact duplicate record count: {errors['exact duplicate record count']}",
        f"Missing required-field error count: {errors['missing required field']}",
        f"Invalid email count: {errors['invalid email']}",
        f"Invalid phone count: {errors['invalid phone']}",
        f"Invalid registration date count: {errors['invalid registration date']}",
        f"Overall data-quality percentage: {percentage:.2f}%",
        "",
        "Data-quality percentage = (valid records / total records processed) x 100.",
        "A record may contribute to several validation-error counts but is counted once as valid or rejected.",
        "Conclusion: " + ("No records were processed." if not total else (
            "The main issues were missing fields, invalid formats, and duplicate records."
            if rejected else "All processed records passed validation."
        )),
    ]
    try:
        # Join report lines and finish with a newline for normal text-file formatting.
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except (PermissionError, OSError) as exc:
        # Tell the caller when the report could not be created.
        raise InputDataError(f"Unable to write '{path.name}': {exc}") from exc

# this function orchestrates the entire process of loading customer data, validating it, generating output files, and reporting results. It configures logging, creates sample input if necessary, loads records from the input file, processes them to classify valid and rejected records, writes the results to CSV files, generates a quality report, and prints a summary to the terminal. It returns a Counter object containing error counts for further analysis or testing.
def run(input_path: Path) -> Counter:
    """Run loading, validation, output generation, reporting, and display."""
    # Keep the log beside the input and generated output files.
    log_path = input_path.parent / "customer_quality.log"
    # Configure logging before recording any processing events.
    configure_logging(log_path)
    logging.info("Application startup")
    # Create sample data only when the requested input file does not exist.
    create_sample_input(input_path)
    logging.info("Loading input file: %s", input_path.name)
    records = load_customers(input_path)
    logging.info("Loaded %d records", len(records))
    logging.info("Validation process started")
    # Divide all rows into outputs and calculate independent error counts.
    valid, rejected, errors = process_records(records)
    # Accepted rows retain only the six original customer columns.
    write_csv(input_path.parent / "valid_customers.csv", valid, FIELDS)
    # Rejected rows retain original fields and receive an error explanation.
    write_csv(input_path.parent / "rejected_customers.csv", rejected, FIELDS + ["error_reasons"])
    # Generate the report from the same values used for the terminal summary.
    generate_quality_report(input_path.parent / "quality_report.txt", input_path.name, len(records), len(valid), len(rejected), errors)
    logging.info("Validation complete: %d valid, %d rejected", len(valid), len(rejected))
    logging.info("Output files successfully generated")
    # Calculate the percentage safely when there are zero input records.
    percentage = (len(valid) / len(records) * 100) if records else 0.0
    # Display a concise result for the person running the command.
    print("\nCUSTOMER DATA QUALITY REPORT")
    print(f"Total records processed: {len(records)}")
    print(f"Valid records: {len(valid)}")
    print(f"Rejected records: {len(rejected)}")
    print(f"Duplicate customer IDs: {errors['duplicate customer ID count']}")
    print(f"Exact duplicate records: {errors['exact duplicate record count']}")
    print(f"Data-quality percentage: {percentage:.2f}%")
    print("\nGenerated files: valid_customers.csv, rejected_customers.csv, quality_report.txt, customer_quality.log")
    # Release the log file handle so it can be opened or removed immediately on Windows.
    logging.shutdown()
    # Return the error counter for tests or future callers.
    return errors

# this function serves as the entry point for the application when executed directly. It attempts to run the main processing function with a specified input file path, handling any InputDataError exceptions that may arise during execution. If an error occurs, it logs the error message, prints it to standard error, and returns a non-zero exit code to indicate failure. If the processing completes successfully, it returns zero to indicate success.
def main() -> int:
    """Start the application and return a success or failure exit code."""
    try:
        # Resolve the input beside this script, regardless of the current shell folder.
        run(Path(__file__).resolve().parent / "customers.csv")
        # Zero is the conventional operating-system success status.
        return 0
    except InputDataError as exc:
        # Show expected processing failures without exposing an unnecessary traceback.
        logging.error("%s", exc)
        print(f"ERROR: {exc}", file=sys.stderr)
        # Non-zero tells a shell or calling script that processing failed.
        return 1


# Only execute the CLI when this file is run directly; imports remain side-effect free.
if __name__ == "__main__":
    sys.exit(main())
