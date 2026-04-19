import os
import shutil
from datetime import datetime
from validator import (
    FilenameValidator,
    HeaderValidator,
    DuplicateBatchValidator,
    ReadingValidator
)

# AUTOMATED VALIDATORS (created once)
filename_validator = FilenameValidator()
header_validator = HeaderValidator()
duplicate_validator = DuplicateBatchValidator()
reading_validator = ReadingValidator()

# AUTOMATED LOGGING
def log_error(filename, message):
    with open("error_log.txt", "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {filename} - {message}\n")

def process_folder(folder_path):
    print(f"Scanning folder: {folder_path}")

    files = os.listdir(folder_path)
    print(f"Found {len(files)} files")

    for file in files:
        print(f"\nProcessing: {file}")
        full_path = os.path.join(folder_path, file)

        # 1. Filename validation
        if not filename_validator.validate(file):
            print("❌ Invalid filename")
            log_error(file, "Invalid filename format")
            continue

        with open(full_path, "r") as f:
            lines = f.readlines()

        # 2. Header validation
        if not header_validator.validate(lines[0]):
            print("❌ Invalid header")
            log_error(file, "Invalid header format")
            continue

        # 3. Duplicate batch ID check
        rows = [line.strip().split(",") for line in lines[1:]]
        if not duplicate_validator.validate(rows):
            print("❌ Duplicate batch ID")
            log_error(file, "Duplicate batch ID found")
            continue

        # 4. Reading validation
        for row in rows:
            readings = row[2:]
            if not reading_validator.validate(readings):
                print("❌ Invalid reading (>9.9)")
                log_error(file, "Invalid reading value")
                break
        else:
            print("✅ File is valid. Moving to archive...")
            archive_folder = "archive"
            os.makedirs(archive_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(archive_folder, file))
            continue
if __name__ == "__main__":
    process_folder("incoming_files")
