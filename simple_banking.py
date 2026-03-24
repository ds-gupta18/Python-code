balance = 10000000
kyc_documents = {}

def check_balance():
    print(f"Your current balance is {balance}")
    print("=====================")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print(f"Can't deposit a negative amount or zero amount")
        print("=====================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print(f"Can't withdraw a negative amount or zero amount")
        print("=====================")
    elif amount > balance:
        print(f"Can't withdraw. Insufficient balance.")
        print("=====================")
    else:
        balance -= amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("=====================")

    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

        print("=====================")


if __name__ == "__main__":
    print("=====================")
    print("Welcome to SWIS BANK!")
    print("=====================")
    print()

while True:
    print("1. Check your balance")
    print("2. Deposit an amount")
    print("3. Withdraw an amount")
    print("4. Check KYC")
    print("5. Update KYC")
    print("6. Quit")
    choice = input("Enter your choice (1-6) : ")
    print("=====================")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amt = float(input("Enter the amount to deposit: "))
        deposit(amt)
        print(f"Amount {amt} deposited successfully")
        print("=====================")
    elif choice == '3':
        amt = float(input("Enter the amount to withdraw: "))
        reason = input("Enter the reason: ")
        withdraw(amt)
        print(f"Amount {amt} withdrawn successfully")
        print("Thank you for using SWISS BANK!")
        print("=====================")
    elif choice == '4':
        check_kyc()
    elif choice == '5':
        kyc_docs ={}
        n_documents = int(input("Enter the number of documents you want to add: "))
        for i in range(int(n_documents)):
            key = input("Enter the document type: ")
            value = input("Enter the document number: ")
            kyc_docs[key] = value
        update_kyc(kyc_docs)
        print(f"KYC updated successfully")
        print("=====================")
    elif choice == '6':
        print("Quiting, Have a good day!")
        break
    else:
        print("Invalid choice!!! Re-try.")
        print("=====================")

print()
print("Thank you for using ABC Bank!")
