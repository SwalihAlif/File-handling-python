# to run this in termianl command => python main.py

import os

NOTES_DIR = "notes"

# ensure the notes folder exists, if not it will create a new one.
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def create_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content:\n")
    with open(f"{NOTES_DIR}/{title}.txt", "w") as f:
        f.write(content)
    print("Note saved!\n")

def view_notes():
    files = os.listdir(NOTES_DIR)
    if not files:
        print("No notes found.\n")
        return
    for file in files:
        print(f"\n--- {file} ---")
        with open(f"{NOTES_DIR}/{file}", "r") as f:
            print(f.read())

def delete_note():
    title = input("Enter note title to delete: ").strip()
    path = f"{NOTES_DIR}/{title}.txt"
    if os.path.exists(path):
        os.remove(path)
        print("Note deleted.\n")
    else:
        print("Note not found.\n")

def menu():
    while True:
        print("=== Notes Manager ===")
        print("1. Create a note")
        print("2. View all notes")
        print("3. Delete a note")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        match choice:
            case "1":
                create_note()
            case "2":
                view_notes()
            case "3":
                delete_note()
            case "4":
                break # to exit from the while loop
            case _:
                print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()