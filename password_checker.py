import re

def check_password_strength(password):
    suggestions = []

    # Length check
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")

    # Uppercase check
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase check
    if not re.search(r"[a-z]", password):
        suggestions.append("Add at least one lowercase letter.")

    # Digit check
    if not re.search(r"[0-9]", password):
        suggestions.append("Include at least one number.")

    # Special character check
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add at least one special character (e.g., !, @, #, $).")

    # Evaluate strength
    score = 5 - len(suggestions)
    if score == 5:
        strength = "Very Strong ✅"
    elif score >= 4:
        strength = "Strong 👍"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, suggestions

# -----------------------------
# Main Program
# -----------------------------
def main():
    print("🔒 Password Strength Checker")
    while True:
        password = input("\nEnter a password (or type 'exit' to quit):\n> ")
        if password.lower() == "exit":
            break

        strength, suggestions = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        if suggestions:
            print("Suggestions to improve:")
            for s in suggestions:
                print(f"- {s}")
        else:
            print("Your password is strong! 🎉")

if __name__ == "__main__":
    main()
