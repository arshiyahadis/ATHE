import os
import shutil

# Using OS API to scan a folder
print("Scanning folder using OS API...")
if os.path.exists("test_data"):
    files = os.listdir("test_data")
    print("Files found:", files)
else:
    print("Folder 'test_data' does not exist. Creating it now...")
    os.makedirs("test_data")
    files = os.listdir("test_data")
    print("Created empty folder:", files)

# Using OS API to create a folder automatically
print("\nCreating archive folder using OS API...")
os.makedirs("archive", exist_ok=True)
print("Archive folder is ready.")

# Using SHUTIL API to demonstrate file moving (simulation)
print("\nDemonstrating SHUTIL API for moving files...")
print("Example: shutil.move('source_path', 'destination_path')")
print("This is only a demonstration for 2M — no real files are moved.")

