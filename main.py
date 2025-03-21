products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "name": "BMW",
         "price": 30,
    }
]

def product_sum():
    total = 0
    for product in products:
        total += product['price']

    print(f"Celková cena všech produktů je {total}€")

def lowest_price():
    lowest_product = products[0]

    for product in products[1:]:

        if product["price"] < lowest_product["price"]:
            lowest_product = product

    return lowest_product

def highest_price():
    highest_product = products[0]

    for product in products[1:]:

        if product["price"] > highest_product["price"]:
            highest_product = product

    return highest_product


def search_product_by_name():
    query = input("Zadejte název produktu pro vyhledání: ").lower()
    found_products = [p for p in products if query in p["name"].lower()]

    if found_products:
        print("Nalezené produkty:")
        for p in found_products:
            print(f"Název: {p['name']}, Cena: {p['price']}€")
    else:
        print("Žádný produkt nenalezen.")

def search_product_by_price():
    price = int(input("Zadejte přesnou cenu produktu: "))
    found_products = [p for p in products if p["price"] == price]

    if found_products:
        print("\nNalezené produkty:")
        for p in found_products:
            print(f"Název: {p['name']}, Cena: {p['price']}€")
    else:
        print("\nŽádný produkt nebyl nalezen.")


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}€")


def add_product():
    product_name = input("Název produktu:")
    product_price = int(input("Název cenu:"))
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)


def menu():
    print("###############")
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Produkt s nejnižší cenou")
    print("4. Produkt s nejvyšší cenou")
    print("5. Celková suma produktú")
    print("6. Vyhledat produkt podle názvu")
    print("7. Vyhledat produkt podle ceny")


    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání poožky:")
        add_product()
        print("")
        menu()
    elif choice == 3:
        lowest_price()
        lowest_product = lowest_price()
        print(f"Produkt s nejnižší cenou je: {lowest_product['name']}, {lowest_product['price']}€\n")
        menu()
    elif choice == 4:
        highest_price()
        highest_product = highest_price()
        print(f"Produkt s nejvyšší cenou je: {highest_product['name']}, {highest_product['price']}€\n")
        menu()
    elif choice == 5:
        product_sum()
        print("")
        menu()
    elif choice == 6:
        search_product_by_name()
        print("")
        menu()
    elif choice == 7:
        search_product_by_price()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
