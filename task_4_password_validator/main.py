def is_valid_password(password):
    """Check if the given password meets all validation conditions."""
    check_length = len(password) >= 6
    check_number = any(char.isdigit() for char in password)
    check_capital = any(char.isupper() for char in password)

    return check_length and check_number and check_capital


def main():
    print("=== Simple Password Validator ===")
    print("Check if your password is strong enough.\n")

    while True:
        password = input("Enter a password to validate (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("\nThank you for using Password Validator. Goodbye!")
            break

        if is_valid_password(password):
            print("Password Accepted\n")
        else:
            print("Password Invalid, must have at least 6 characters, one number, and one capital letter.\n")


if __name__ == "__main__":
    main()
