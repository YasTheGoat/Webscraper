import newegg_page
import amazon_page

while True:
    chosen_store = input(
        " Wich store do you want to scan(Newegg/Amazon): ")

    if chosen_store.lower() == "newegg":
        newegg_page.run()
        break
    elif chosen_store.lower() == "amazon":
        amazon_page.run()
        break
    else:
        print("Invalid Input...Please try again.")
        continue
