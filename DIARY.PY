import os
import datetime

def write_diary_entry():
    # Get the current date and time
    now = datetime.datetime.now()
    entry_date = now.strftime("%Y-%m-%d %H:%M:%S")

    # Ask the user for their diary entry
    entry = input("Write your diary entry for today:\n")

    # Create a file for the diary entry (use the date as the filename)
    filename = f"{now.strftime('%Y-%m-%d')}.txt"
    with open(filename, "a") as file:
        file.write(f"Entry Date: {entry_date}\n")
        file.write(f"{entry}\n")
        file.write("\n")

def read_diary_entries():
    # List all diary entry files in the current directory
    diary_files = [file for file in os.listdir() if file.endswith(".txt")]

    if not diary_files:
        print("No diary entries found.")
        return

    # Display a list of available diary entries
    print("Available diary entries:")
    for index, file in enumerate(diary_files):
        print(f"{index + 1}. {file}")

    # Ask the user to choose an entry to read
    entry_number = int(input("Enter the number of the entry you want to read: ")) - 1

    #if entry_numbers == 0;
     #   return
    
    if 0 <= entry_number < len(diary_files):
        with open(diary_files[entry_number], "r") as file:
            entry_contents = file.read()
            print("\nDiary Entry:")
            print(entry_contents)
    else:
        print("Invalid entry number.")

def main():
    while True:
        print("\nPersonal Diary")
        print("1. Write a new diary entry")
        print("2. Read diary entries")
        print("3. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            write_diary_entry()
        elif choice == "2":
            read_diary_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
