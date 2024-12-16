import re


def assess_password_strength(password):
    # Criteria checks
    length_ok = len(password) >= 8  # Minimum length of 8
    upper_case = bool(re.search(r'[A-Z]', password))  # At least one uppercase letter
    lower_case = bool(re.search(r'[a-z]', password))  # At least one lowercase letter
    has_number = bool(re.search(r'[0-9]', password))  # At least one digit
    special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))  # Special character

    # Score the password based on criteria
    score = 0
    if length_ok:
        score += 1
    if upper_case:
        score += 1
    if lower_case:
        score += 1
    if has_number:
        score += 1
    if special_char:
        score += 1

    # Determine password strength
    if score == 5:
        strength = "Very Strong"
        feedback = "Your password is very strong. Good job!"
    elif score == 4:
        strength = "Strong"
        feedback = "Your password is strong. Consider adding more variety for extra security."
    elif score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Add some more variety like a special character or upper/lowercase mix."
    elif score == 2:
        strength = "Weak"
        feedback = "Your password is weak. Consider adding more length, special characters, and mixing cases."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. You should add length, use upper and lower case, numbers, and special characters."

    # Return the result and feedback
    return {
        "strength": strength,
        "feedback": feedback,
        "length_ok": length_ok,
        "upper_case": upper_case,
        "lower_case": lower_case,
        "has_number": has_number,
        "special_char": special_char
    }


def print_password_assessment(password):
    result = assess_password_strength(password)
    print(f"Password: {password}")
    print(f"Strength: {result['strength']}")
    print(f"Feedback: {result['feedback']}")
    print("\nPassword Criteria Check:")
    print(f"Length >= 8 characters: {'Yes' if result['length_ok'] else 'No'}")
    print(f"Contains uppercase letter: {'Yes' if result['upper_case'] else 'No'}")
    print(f"Contains lowercase letter: {'Yes' if result['lower_case'] else 'No'}")
    print(f"Contains number: {'Yes' if result['has_number'] else 'No'}")
    print(f"Contains special character: {'Yes' if result['special_char'] else 'No'}")


# Example Usage:
password = input("Enter a password to assess its strength: ")
print_password_assessment(password)
