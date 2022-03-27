import os
import webbrowser
from bs4 import BeautifulSoup as soup
from urllib.request import build_opener, urlopen as uReq
import colorama as color
color.init(autoreset=True)

products_found = 0
products_search_len = 0
product_dic = {}
link = ""


def run():
    global products_search_len
    global link
    global product_dic

    product_search = input(" What product do you want to track: ")
    product_search = product_search.split(" ")
    pages = input(" Wich pages do you wanna scan(Separe by a '-'): ")
    specification = input(" Do you have any specs specification: ")
    budget = input(" Do you have any budget(Whithout $ sign): ")
    print("")

    pages = pages.split("-")

    my_url = f'https://www.amazon.ca/s?k='

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

            opener = build_opener()
            opener.addheaders = [
                ("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 OPR/74.0.3911.160")]
            response = opener.open(my_url)
            page_html = response.read()

            page_soup = soup(page_html, "html.parser")

            containers = page_soup(
                "div", {"class": "a-section a-spacing-medium"})

            for container in containers:

                try:
                    # product title
                    title_container = container.findAll(
                        "a", {"class": "a-link-normal a-text-normal"})
                    product_name = title_container[0].span.text.strip()
                except:
                    product_name = 'None'

                try:
                    # product price
                    price_container = container.findAll(
                        "span", {"class": "a-offscreen"})
                    price_ = price_container[0].text.strip()

                    price_whole = price_.split("$")
                    price_whole = price_whole[1].split(".")
                    price_whole = price_whole[0]
                    if "," in price_whole:
                        price_whole = price_whole.replace(",", "")
                except:
                    price_whole = 0
                    price_ = 'None'

                try:
                    # product rating
                    rating_container = container.findAll(
                        "div", {"class": "a-row a-size-small"})
                    rating = rating_container[0].span.text.strip()
                except:
                    rating = 'None'

                # product link
                link_container = container.findAll(
                    "a", {"class": "a-link-normal a-text-normal"})
                link = link_container[0]["href"]

                if specification != "":
                    if budget != "":
                        if specification.lower() in product_name.lower() and int(price_whole) <= int(budget):
                            id += 1
                            product_dic[id] = 'www.amazon.ca' + link

                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}{price_}")
                            print(
                                f" {color.Fore.BLUE}Rating: {color.Fore.WHITE}{rating}")
                            print(
                                f" {color.Fore.BLUE}Link: {color.Fore.WHITE}www.amazon.ca{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                    else:
                        if specification.lower() in product_name.lower():
                            id += 1
                            product_dic[id] = 'www.amazon.ca' + link

                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}{price_}")
                            print(
                                f" {color.Fore.BLUE}Rating: {color.Fore.WHITE}{rating}")
                            print(
                                f" {color.Fore.BLUE}Link: {color.Fore.WHITE}www.amazon.ca{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                elif budget != "":
                    if specification != "":
                        if specification.lower() in product_name.lower() and int(price_whole) <= int(budget):
                            id += 1
                            product_dic[id] = 'www.amazon.ca' + link

                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}{price_}")
                            print(
                                f" {color.Fore.BLUE}Rating: {color.Fore.WHITE}{rating}")
                            print(
                                f" {color.Fore.BLUE}Link: {color.Fore.WHITE}www.amazon.ca{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                    else:
                        if int(price_whole) <= int(budget):
                            id += 1
                            product_dic[id] = 'www.amazon.ca' + link

                            print(
                                "---------------------------------------------------------------------------------------------------------------------")
                            print(
                                f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                            print(
                                f" {color.Fore.BLUE}Price: {color.Fore.WHITE}{price_}")
                            print(
                                f" {color.Fore.BLUE}Rating: {color.Fore.WHITE}{rating}")
                            print(
                                f" {color.Fore.BLUE}Link: {color.Fore.WHITE}www.amazon.ca{link}\n")
                            print(
                                f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                            products_found += 1
                else:
                    id += 1
                    product_dic[id] = 'www.amazon.ca' + link

                    print(
                        "---------------------------------------------------------------------------------------------------------------------")
                    print(
                        f" {color.Fore.BLUE}Product Name: {color.Fore.WHITE}{product_name}")
                    print(
                        f" {color.Fore.BLUE}Price: {color.Fore.WHITE}{price_}")
                    print(
                        f" {color.Fore.BLUE}Rating: {color.Fore.WHITE}{rating}")
                    print(
                        f" {color.Fore.BLUE}Link : {color.Fore.WHITE}www.amazon.ca{link}\n")
                    print(
                        f" {color.Fore.BLUE}ID: {color.Fore.WHITE}{id}")
                    products_found += 1

                # except:
                #     pass
        break

    print("---------------------------------------------------------------------------------------------------------------------")
    if products_found == 0:
        print(
            f" {color.Fore.RED}Sorry, no products within {str(product_search)} with {specification} found")
    else:
        print(f" {color.Fore.GREEN}{str(products_found)} products found.\n")

    while True:
        operation = input("Quit/Retry/ID: ")
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
