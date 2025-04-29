import os

NOTES_DIR = "notes"

# ensure the notes folder exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def create_note():
    title = input("Enter not title: ").strip()
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