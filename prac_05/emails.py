"""
emails
Estimate: 30 minutes
Actual:   42 minutes
"""


def extract_name(email):
    """Extract a probable name from an email address."""
    email_name = email.split('@')[0]
    parts = email_name.split('.')
    parts = [part.capitalize() for part in parts]
    return ' '.join(parts)


def store_email():
    """Store users' emails and names in a dictionary."""
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        suggested_name = extract_name(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

        if confirmation and confirmation != 'y':
            name = input("Name: ")
        else:
            name = suggested_name

        email_to_name[email] = name

    print("\nStored email and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def main():
    store_email()

main()