#Chat bot 2

print("Welcome to LibBot! Ask me about our library services.")
print("Type 'exit' to end the chat.\n")
while True:
    user = input("You: ").lower()
    if user == "exit":
        print("LibBot: Goodbye! Happy reading!")
        break
    elif "membership" in user:
        print("LibBot: You can get a membership by filling out the form at the front desk or online.")
    elif "timing" in user or "hours" in user:
        print("LibBot: The library is open from 9 AM to 6 PM, Monday to Saturday.")
    elif "borrow" in user or "issue" in user:
        print("LibBot: You can borrow up to 3 books at a time for 14 days.")
    elif "return" in user:
        print("LibBot: Books should be returned within 14 days to avoid late fees.")
    elif "late fee" in user:
        print("LibBot: The late fee is ₹2 per day per book.")
    else:
        print("LibBot: Sorry, I didn't understand that. Please ask about timings, membership, borrowing, or returns.")
