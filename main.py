#Contact Book Using Dictionary
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=""):
        key = name.strip()
        if key in self.contacts:
            print(f"Error: Contact '{key}' already exists.")
            return False
        self.contacts[key] = {"phone": phone.strip(), "email": email.strip()}
        print(f"Contact '{key}' added successfully.")
        return True

    def search_contact(self, query):
        query_lower = query.strip().lower()
        matches = {
            name: details
            for name, details in self.contacts.items()
            if query_lower in name.lower()
        }
        if not matches:
            print(f"No contacts found matching '{query}'.")
            return {}

        print(f"Found {len(matches)} contact(s):")
        for name, details in matches.items():
            print(f"  • {name} | Phone: {details['phone']} | Email: {details['email'] or 'N/A'}")
        return matches

    def update_contact(self, name, phone=None, email=None):
        key = name.strip()
        if key not in self.contacts:
            print(f"Error: Contact '{key}' not found.")
            return False
        if phone:
            self.contacts[key]["phone"] = phone.strip()
        if email is not None:
            self.contacts[key]["email"] = email.strip()
        print(f"Contact '{key}' updated successfully.")
        return True

    def delete_contact(self, name):
        key = name.strip()
        if key in self.contacts:
            del self.contacts[key]
            print(f"Contact '{key}' deleted successfully.")
            return True
        print(f"Error: Contact '{key}' not found.")
        return False


# Example Usage:
book = ContactBook()
book.add_contact("Alice Smith", "+1-555-0199", "alice@example.com")
book.add_contact("Bob Jones", "+1-555-0144")
book.search_contact("alice")
book.update_contact("Bob Jones", email="bob.jones@work.com")
book.delete_contact("Alice Smith")

print("-"*50)
#Word Counter from text file

# Step 1: Create a sample text file to read from
sample_content = """Python is a high-level programming language.
It emphasizes code readability and simplicity.
Counting words, lines, and characters is easy."""

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(sample_content)


# Step 2: Read and calculate statistics
def count_file_stats(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

            line_count = len(text.splitlines())
            word_count = len(text.split())
            char_count = len(text)

        print(f"--- File Stats: {filepath} ---")
        print(f"Lines:      {line_count}")
        print(f"Words:      {word_count}")
        print(f"Characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' does not exist.")


# Step 3: Run the function
count_file_stats("sample.txt")
print("-"*50)
#JSON File Reader
import json

# Step 1: Create a sample JSON file to read from
sample_data = {
    "organization": "Developer Hub",
    "active": True,
    "members_count": 3,
    "members": [
        {"name": "Alice", "role": "Backend Developer"},
        {"name": "Bob", "role": "Frontend Developer"},
        {"name": "Charlie", "role": "DevOps Engineer"}
    ]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(sample_data, f)


# Step 2: Read, parse, and pretty-print the JSON
def read_and_format_json(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        print(f"--- Formatted JSON Output ({filepath}) ---")
        print(json.dumps(data, indent=4))

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON syntax ({e}).")


# Step 3: Run the function
read_and_format_json("data.json")
