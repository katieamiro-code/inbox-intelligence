def categorize_email(email_text):
    text = email_text.lower()
    if "order" in text:
        return "Order/Shipping"
    if "payment" in text:
        return "Bill/Payment"
    if any(word in text for word in ("urgent", "important", "deadline", "appointment", "asap")):
        return "Urgent"
    return "other"


def main():
    print("Inbox Intelligence is starting...")
    email_text = input("Paste an email here: ")
    print("Email received:", email_text)
    print("Category:", categorize_email(email_text))


if __name__ == "__main__":
    main()
