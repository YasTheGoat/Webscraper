import os
import webbrowser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import colorama as color
color.init(autoreset=True)

products_found = 0
products_search_len = 0
product_dic = {}
link = ""


def run():
    global products_search_len
    global product_dic
    global link

    product_search = input(" What product do you want to track: ")
    product_search = product_search.split(" ")
    pages = input(" Wich pages do you wanna scan(Separe b y a '-'): ")
    specification = input(" Do you have any specs specification: ")
    budget = input(" Do you have any budget(Whithout $ sign): ")
    print("")

    pages = pages.split("-")

    my_url = 'https://www.newegg.ca/p/pl?d='

    if len(product_search) > 1:
        for word in product_search:
            my_url += word
            products_search_len += 1
            if products_search_len != len(product_search):
                my_url += '+'
    else:
        my_url += product_search[0]

    while True:
        global products_found

        id = 0

        for page in pages:

            my_url = my_url + "&page=" + str(page)

            uClient = uReq(my_url)

            page_html = uClient.read()

            uClient.close()

            page_soup = soup(page_html, "html.parser")

            containers = page_soup("div", {"class": "item-container"})

            for container in containers:
                # try:
                try:
                    # product brand
                    brand = container.find("div", {"class": "item-info"}).find(
                        "div", {"class": "item-branding"}).find("a", {"class": "item-brand"}).img["title"]
                except:
                    brand = 'None'

                try:
                    # product title
                    title_container = container.findAll(
                        "a", {"class": "item-title"})
                    product_name = title_container[0].text.strip()
                except:
                    product_name = 'None'

                try:
                    # product shipping price
                    shipping_container = container.findAll(
                        "li", {"class": "price-ship"})
                    shipping = shipping_container[0].text.strip()
                except:
                    shipping = 'None'

                try:
                    # product price
                    price_container = container.find(
                        "li", {"class": "price-current"})
                    price_ = price_container.strong.text
                    price_cent = price_container.sup.text

                    if ',' in price_:
                        price_ = price_.replace(",", "")
                except:
                    price_ = 0
                    price_cent = 0

                try:
                    link = container.a["href"]
                except:
                    link = 'None'

                if specification != "":
                    if budget != "":
                        if specification.lower() in product_name.lower() and int(price_) <= int(budget):
                            id += 1
                            product_dic[id] = link
                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Brand: {color.Fore.WHITE}{brand}")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Shipping: {color.Fore.WHITE}{shipping}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}${price_}{price_cent}")
                            print(
                                f" {color.Fore.BLUE}Link : {color.Fore.WHITE}{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                    else:
                        if specification.lower() in product_name.lower():
                            id += 1
                            product_dic[id] = link
                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Brand: {color.Fore.WHITE}{brand}")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Shipping: {color.Fore.WHITE}{shipping}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}${price_}{price_cent}")
                            print(
                                f" {color.Fore.BLUE}Link : {color.Fore.WHITE}{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                elif budget != "":
                    if specification != "":
                        if specification.lower() in product_name.lower() and int(price_) <= int(budget):
                            id += 1
                            product_dic[id] = link
                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Brand: {color.Fore.WHITE}{brand}")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Shipping: {color.Fore.WHITE}{shipping}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}${price_}{price_cent}")
                            print(
                                f" {color.Fore.BLUE}Link : {color.Fore.WHITE}{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                    else:
                        if int(price_) <= int(budget):
                            id += 1
                            product_dic[id] = link
                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Brand: {color.Fore.WHITE}{brand}")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Shipping: {color.Fore.WHITE}{shipping}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}${price_}{price_cent}")
                            print(
                                f" {color.Fore.BLUE}Link : {color.Fore.WHITE}{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                else:
                    id += 1
                    product_dic[id] = link
                    print(
                        "---------------------------------------------------------------------------------------------------------------------")
                    print(
                        f" {color.Fore.BLUE}Brand: {color.Fore.WHITE}{brand}")
                    print(
                        f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                    print(
                        f" {color.Fore.BLUE}Shipping: {color.Fore.WHITE}{shipping}")
                    print(
                        f" {color.Fore.BLUE}Price: {color.Fore.WHITE}${price_}{price_cent}")
                    print(
                        f" {color.Fore.BLUE}Link : {color.Fore.WHITE}{link}\n")
                    print(
                        f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                    products_found += 1
        break

    print("---------------------------------------------------------------------------------------------------------------------")
    if products_found == 0:
        print(
            f" {color.Fore.RED}Sorry, no products within {str(product_search)} with {specification} found")
    else:
        print(f" {color.Fore.GREEN}{str(products_found)} products found.\n")

    while True:
        operation = input("Quit/Retry/open product in browser(ID): ")
        try:
            if operation.lower() == 'retry':
                os.system("cls" if os.name == "nt" else "clear")
                os.system("python main.py")
                break
            elif operation.lower() == 'quit':
                break
            elif operation.lower() == "id":
                product_id = input("Product ID: ")
                for id in product_dic:
                    if int(product_id) == int(id):
                        opera_browser = 'C:/Users/OKIYY/AppData/Local/Programs///Opera/launcher.exe %s'
                        webbrowser.get(opera_browser).open(product_dic[id])
                        continue
            else:
                print("Invalid Input...Please try again.")
                continue
        except:
            print("Something went wrong...Please try again.")
            continue
