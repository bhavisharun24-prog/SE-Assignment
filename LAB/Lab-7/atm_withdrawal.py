# Name: Bhavish A | SRN: PES2UG24AM040
# Fixed version: every function returns None for bad input instead of crashing.

DIGITS = "0123456789"


def notes_needed(amount):
    if not isinstance(amount, str):
        return None
    cleaned = amount.replace(',', '').strip()
    # only plain ASCII digits, so "", "-1", "abc", "1_000" or "١٢" are rejected
    if cleaned == "" or any(ch not in DIGITS for ch in cleaned):
        return None
    return int(cleaned) // 100


def mask_card(card_number):
    if not isinstance(card_number, str):
        return None
    digits = card_number.replace(" ", "")
    if len(digits) != 16 or any(ch not in DIGITS for ch in digits):
        return None
    return "XXXX XXXX XXXX " + digits[-4:]


def average_withdrawal(amounts_csv):
    if not isinstance(amounts_csv, str):
        return None
    amounts = []
    for part in amounts_csv.split(','):
        part = part.strip()
        if part == "" or any(ch not in DIGITS for ch in part):
            return None
        amounts.append(int(part))
    return sum(amounts) // len(amounts)  # split always gives at least one part


def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", result if result is not None else "Invalid amount")

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    result = mask_card(user_input)
    print("Masked Card:", result if result is not None else "Invalid card number")

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
