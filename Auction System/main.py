from users import register_user, login_user
from auction import create_auction_item, place_bid


def main():
    print("Welcome to the Secure Online Auction System")
    while True:
        choice = input("1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(username, password))

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_status = login_user(username, password)
            print(login_status)
            if login_status == "Login successful.":
                while True:
                    user_choice = input("1. Create Auction\n2. Place Bid\n3. Logout\nChoose an option: ")
                    if user_choice == '1':
                        item_name = input("Enter item name: ")
                        starting_bid = float(input("Enter starting bid: "))
                        print(create_auction_item(username, item_name, starting_bid))

                    elif user_choice == '2':
                        item_name = input("Enter item name to bid on: ")
                        bid_amount = float(input("Enter your bid amount: "))
                        print(place_bid(username, item_name, bid_amount))

                    elif user_choice == '3':
                        break
                    else:
                        print("Invalid option. Try again.")

        elif choice == '3':
            print("Thank you for using the Auction System.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
