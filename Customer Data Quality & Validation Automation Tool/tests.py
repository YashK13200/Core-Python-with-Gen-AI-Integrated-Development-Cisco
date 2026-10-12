import tempfile
import unittest
from pathlib import Path

import main


class ValidationTests(unittest.TestCase):
    def test_email_validation(self):
        self.assertTrue(main.validate_email("priya.patel@example.com"))
        self.assertFalse(main.validate_email("amitgmail.com"))
        self.assertFalse(main.validate_email("user@domain"))

    def test_phone_validation(self):
        self.assertTrue(main.validate_phone("9876543210"))
        self.assertFalse(main.validate_phone("123"))
        self.assertFalse(main.validate_phone("98765abc10"))

    def test_date_validation(self):
        self.assertTrue(main.validate_registration_date("2026-01-10"))
        self.assertFalse(main.validate_registration_date("2026-02-30"))
        self.assertFalse(main.validate_registration_date("invalid-date"))

    def test_required_fields_and_multiple_errors(self):
        record = {field: "" for field in main.FIELDS}
        self.assertEqual(len(main.validate_required_fields(record)), 6)
        valid, rejected, _ = main.process_records([{
            "customer_id": "C1", "name": "Test", "email": "bad",
            "phone": "123", "city": "", "date_of_registration": "no",
        }])
        self.assertEqual(len(valid), 0)
        self.assertEqual(len(rejected), 1)
        self.assertIn("invalid email format", rejected[0]["error_reasons"])
        self.assertIn("invalid phone format", rejected[0]["error_reasons"])

    def test_duplicate_ids_and_exact_rows(self):
        row = dict(zip(main.FIELDS, ["C1", "Test", "test@example.com", "9876543210", "Delhi", "2026-01-01"]))
        valid, rejected, errors = main.process_records([row, row.copy()])
        self.assertEqual(len(valid), 1)
        self.assertEqual(len(rejected), 1)
        self.assertEqual(errors["duplicate customer ID count"], 1)
        self.assertEqual(errors["exact duplicate record count"], 1)

    def test_empty_input_and_count_reconciliation(self):
        valid, rejected, _ = main.process_records([])
        self.assertEqual(valid, [])
        self.assertEqual(rejected, [])
        self.assertEqual(len(valid) + len(rejected), 0)

    def test_missing_file_and_unusable_structure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.csv"
            with self.assertRaises(main.InputDataError):
                main.load_customers(path)
            path.write_text("wrong_header\nvalue\n", encoding="utf-8")
            with self.assertRaises(main.InputDataError):
                main.load_customers(path)

    def test_run_writes_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "customers.csv"
            path.write_text(
                ",".join(main.FIELDS)
                + "\nC1,Test,test@example.com,9876543210,Delhi,2026-01-01\n",
                encoding="utf-8",
            )
            main.run(path)
            for filename in ("valid_customers.csv", "rejected_customers.csv", "quality_report.txt", "customer_quality.log"):
                self.assertTrue((Path(directory) / filename).exists())
            with (Path(directory) / "quality_report.txt").open(encoding="utf-8") as handle:
                report = handle.read()
            self.assertIn("Total records processed: 1", report)
            self.assertIn("Valid record count: 1", report)


if __name__ == "__main__":
    unittest.main()
