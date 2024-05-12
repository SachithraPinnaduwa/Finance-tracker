import json
import datetime

# Global list to store transactions
class User:
    def __init__(self):
        self.transactions = []


    # File handling functions
    def load_transactions(self):
        self.transactions.clear()
        try:
            with open('SampleJSONFile.json', 'r') as file:
                # Load the JSON data

                data = json.load(file)
                for transaction in data:
                    self.transactions.append(transaction)

                self.view_transactions()
        except FileNotFoundError:
            print("File does not exist")

    def save_transactions(self):
        try:
            with open('SampleJSONFile.json', 'w') as file:
                # Load the JSON data
                file.write("[" + "\n")
                for transaction in self.transactions:
                    file.write(json.dumps(transaction))
                    if self.transactions[-1] != transaction:
                        file.write(",")
                    file.write("\n")
                file.write("]")
        except:
            print("Cannot save to file")

    # Feature implementations
    def add_transaction(self,amountinput, descriptioninput, typeinput):
        amount = amountinput
        description = descriptioninput
        typeoftransaction = typeinput
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.transactions.append([amount, description, typeoftransaction, time])
        self.view_transactions()

    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def update_transaction(self,descriptionupdate,updatewhat,value):
    
        description = descriptionupdate
        what = updatewhat.lower()
        for transaction in self.transactions:
            if (transaction[1] == description):
                if what == "type":
                    update_type = value
                    transaction[2] = update_type
                    break
                elif what == "amount":
                    update_amount = float(value)
                    transaction[0] = update_amount
                    break
                elif what == "description":
                    update_desc = value
                    transaction[1] = update_desc
                    break
                else:
                    print("Invalid")
                    break
        self.save_transactions()

    def delete_transaction(self,deletewhat):
   
        remove = deletewhat
        found = False
        with open('SampleJSONFile.json', 'r') as file:
            # Load the JSON data
            data = json.load(file)
            for transaction in data:
                if transaction[1] == remove:
                    self.transactions.remove(transaction)
                    found = True
                    break

        self.save_transactions()
        if found:
            return "Deleting transaction"
        else:
            return "Not found"

    def display_summary(self):
        print("Total Transactions: " + str(len(self.transactions)))
        total = 0
        for transaction in self.transactions:
            if transaction[2] == "income":
                total = total + transaction[0]
            elif transaction[2] == "expense":
                total = total - transaction[0]
        return "Total : " + str(total)

    def main_menu(self):
        self.load_transactions()  # Load transactions at the start
        while True:

            choice = input("Enter your choice: from 1 to 7")

            if choice == '1':
                self.add_transaction()
            elif choice == '2':
                self.view_transactions()
            elif choice == '3':
                self.update_transaction()
            elif choice == '4':
                self.delete_transaction()
            elif choice == '5':
                self.display_summary()
            elif choice == '6':
                self.save_transactions()
            elif choice == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        return (
            "\nPersonal Finance Tracker\n"
            " Add Transaction\n"
            " View Transactions\n"
            " Update Transaction\n"
            " Delete Transaction\n"
            " Display Summary\n"
            " Save to JSON file\n"
            " Exit"
        )
if __name__ == "__main__":
    user = User()
    user.main_menu()

