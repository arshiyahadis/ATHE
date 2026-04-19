import re

class Validator:
    def validate(self, data):
        raise NotImplementedError("Subclasses must implement validate()")


class FilenameValidator(Validator):
    def validate(self, filename):
        pattern = r"^MED_DATA_\d{14}\.csv$"
        return re.match(pattern, filename) is not None


class HeaderValidator(Validator):
    def validate(self, header_line):
        expected = ["batch_id", "timestamp"] + [f"reading{i}" for i in range(1, 11)]
        return header_line.strip().split(",") == expected


class DuplicateBatchValidator(Validator):
    def validate(self, rows):
        seen = set()
        for row in rows:
            batch_id = row[0]
            if batch_id in seen:
                return False
            seen.add(batch_id)
        return True


class ReadingValidator(Validator):
    def validate(self, readings):
        if len(readings) != 10:
            return False
        try:
            return all(float(r) <= 9.9 for r in readings)
        except ValueError:
            return False


