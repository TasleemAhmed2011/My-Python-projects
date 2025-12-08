import random
import string

# -------- RANDOM 4–6 LETTERS + DIGITS CODE --------
def random_code(min_len=4, max_len=6):
    length = random.randint(min_len, max_len)
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))

# -------- PASSWORD STRENGTH CHECK --------
def check_strength(pwd: str) -> str:
    length = len(pwd)
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in "!@#$%&*?_-+.,:" for c in pwd)

    if length >= 10 and has_lower and (has_upper or has_symbol) and has_digit:
        return "Strong"
    elif length >= 8 and has_lower and has_digit:
        return "Medium"
    else:
        return "Weak"


print("=== SMART PASSWORD MAKER  ===\n")

# ═══════════════════════════════════════════════════════════════════
#                🔁 MAIN LOOP → MAKE PASSWORDS AGAIN?
# ═══════════════════════════════════════════════════════════════════

while True:

    # ═══════════════════════════════════════════════════════════════
    #            🔁 INPUT-CONFIRMATION LOOP (ENTER AGAIN)
    # ═══════════════════════════════════════════════════════════════
    while True:
        # -------- USER INPUTS --------
        name = input("Enter your name: ").strip()
        dob = input("Enter your date of birth (example: 25-11-2011): ").strip()
        hobby = input("Enter your favourite hobby: ").strip()
        color = input("Enter your favourite color: ").strip()
        fav_number = input("Enter your favourite number: ").strip()

        # Confirmation Summary
        print("\nPlease confirm your details:")
        print("Name       :", name)
        print("DOB        :", dob)
        print("Hobby      :", hobby)
        print("Color      :", color)
        print("Fav number :", fav_number)

        ok = input("\nAre these correct? (Y to continue, N to re-enter): ").strip().lower()

        if ok == "y":
            break
        else:
            print("\nOkay, let's enter the details again...\n")

    # ═══════════════════════════════════════════════════════════════
    #                     PROCESS DATA AFTER CONFIRM
    # ═══════════════════════════════════════════════════════════════

    name = name.lower()
    hobby = hobby.lower()
    color = color.lower()

    dob_digits = "".join(ch for ch in dob if ch.isdigit())
    dob_last2 = dob_digits[-2:] if len(dob_digits) >= 2 else dob_digits
    dob_last4 = dob_digits[-4:] if len(dob_digits) >= 4 else dob_digits

    name_part = name[:6]
    hobby_part = hobby[:8]
    color_part = color[:6]

    # ═══════════════════════════════════════════════════════════════
    #                   GENERATE 5 UNIQUE PASSWORDS
    # ═══════════════════════════════════════════════════════════════

    p1 = random_code() + name_part + dob_last4
    p2 = random_code() + hobby_part + "." + color_part
    extra_digits = "".join(random.choice(string.digits) for _ in range(random.randint(3, 6)))
    p3 = name_part + fav_number + extra_digits + "#"
    p4 = color_part + random_code() + dob_last2

    first_letters = ""
    if name:
        first_letters += name[0]
    if hobby:
        first_letters += hobby[0]

    extra_digits2 = "".join(random.choice(string.digits) for _ in range(random.randint(2, 4)))
    p5 = random_code() + first_letters + extra_digits2

    passwords = [p1, p2, p3, p4, p5]

    # ═══════════════════════════════════════════════════════════════
    #                          SHOW PASSWORDS
    # ═══════════════════════════════════════════════════════════════

    print("\nHere are your 5 password suggestions:\n")
    for i, pwd in enumerate(passwords, start=1):
        print(f"{i}) {pwd}")

    # ═══════════════════════════════════════════════════════════════
    #       🔁 STRENGTH CHECK LOOP – CHECK MULTIPLE PASSWORDS
    # ═══════════════════════════════════════════════════════════════

    while True:
        print("\n--- Password Strength Checker ---")
        user_pwd = input("Enter a password to check (or press Enter to skip): ")

        if user_pwd.strip() == "":
            print("Skipped strength check.")
            break

        print("Strength:", check_strength(user_pwd))

        again = input("Check another password? (Y/N): ").strip().lower()
        if again != "y":
            break

    # ═══════════════════════════════════════════════════════════════
    #             ASK USER IF THEY WANT TO MAKE PASSWORDS AGAIN
    # ═══════════════════════════════════════════════════════════════

    repeat = input("\nDo you want to make passwords again? (Y/N): ").strip().lower()

    if repeat != "y":
        print("\nThank you for using the Password Maker! Goodbye.")
        print("\nCreated By Tasleem Ahmed.")

        break
