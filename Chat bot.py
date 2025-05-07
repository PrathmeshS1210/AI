#Chat Bot

def bank():
    print("Welcome to BankBot! Ask your questions or type 'exit' to quit.\n")

    while True:
        msg = input("You: ").lower()

        if "balance" in msg:
            print("BankBot: Your current balance is ₹12,345.")
        elif "loan" in msg:
            print("BankBot: We offer home, car, and personal loans at competitive rates.")
        elif "account" in msg:
            print("BankBot: You can open a savings or current account with valid ID proof.")
        elif "atm" in msg:
            print("BankBot: The nearest ATM is 500 meters from your location.")
        elif "exit" in msg:
            print("BankBot: Thank you for visiting. Have a great day!")
            break
        else:
            print("BankBot: Sorry, I can only assist with basic banking queries.")

bank()
