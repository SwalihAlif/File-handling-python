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

