import time

def show_header():
    print("=========================================")
    print("   Scientific CSV Processing System")
    print("=========================================")

def show_menu():
    print("\nChoose an option:")
    print("1. Connect to FTP and list files")
    print("2. Process new files")
    print("3. View error log")
    print("4. Exit")

def connect_and_list_files():
    print("\n[STEP 1] Connecting to FTP server...")
    time.sleep(0.5)
    print("Connected successfully.")
    print("Files found on FTP:")
    print(" - MED_DATA_20240101120000.csv")
    print(" - MED_DATA_20240101130000.csv")
    print(" - MED_DATA_20240101140000.csv")

def process_new_files():
    print("\n[STEP 2] Downloading new files...")
    time.sleep(0.5)
    print("Downloaded: MED_DATA_20240101120000.csv")
    print("Skipped (already processed): MED_DATA_20240101130000.csv")

    print("\n[STEP 3] Validating files...")
    time.sleep(0.5)
    print("Validation passed: MED_DATA_20240101120000.csv")
    print("Validation failed: MED_DATA_20240101130000.csv (Invalid reading > 9.9)")

    print("\n[STEP 4] Storing valid files...")
    time.sleep(0.5)
    print("Stored in: archive/2024/01/01/12/")

    print("\n[STEP 5] Logging invalid files...")
    time.sleep(0.5)
    print("Logged: MED_DATA_20240101130000.csv")

def view_error_log():
    print("\n[ERROR LOG]")
    print("MED_DATA_20240101130000.csv – Invalid reading > 9.9")

def main():
    show_header()
    while True:
        show_menu()
        choice = input("\nEnter your choice (1–4): ")

        if choice == "1":
            connect_and_list_files()
        elif choice == "2":
            process_new_files()
        elif choice == "3":
            view_error_log()
        elif choice == "4":
            print("\nExiting system. Goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
