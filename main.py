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
    min_price = min(x["price"] for x in products)
    lowest_price_products = [x for x in products if x["price"] == min_price]

    print("\nProdukt(y) s nejnižší cenou:")
    for x in lowest_price_products:
        print(f"Název: {x['name']}, Cena: {x['price']}€")

def highest_price():
    max_price = max(x["price"] for x in products)
    highest_price_products = [x for x in products if x["price"] == max_price]
    print("\nProdukt(y) s nejvyšší cenou:")
    for x in highest_price_products:
        print(f"Název: {x['name']}, Cena: {x['price']}€")

def edit_product():
    for i, x in enumerate(products, 1):
        print(f"{i}. {x['name']} - {x['price']}€")

    choice = int(input("\nVyberte číslo produktu k úpravě: ")) - 1
    if not (0 <= choice < len(products)):
        print("Neplatná volba!")
        return

    products[choice]["name"] = input("Nový název: ") or products[choice]["name"]
    new_price = input("Nová cena: ")
    if new_price.isdigit():
        products[choice]["price"] = int(new_price)

    print("Produkt upraven!")



def search_product_by_name():
    name = input("Zadejte název produktu pro vyhledání: ").lower()
    found_products = [p for p in products if name in p["name"].lower()]

    if found_products:
        print("\nNalezené produkty:")
        for p in found_products:
            print(f"Název: {p['name']}, Cena: {p['price']}€")
    else:
        print("Žádný produkt nebyl nalezen.")

def search_product_by_price():
    price = int(input("Zadejte přesnou cenu produktu: "))
    found_products = [p for p in products if p["price"] == price]

    if found_products:
        print("\nNalezené produkty:")
        for p in found_products:
            print(f"Název: {p['name']}, Cena: {p['price']}€")
    else:
        print("\nŽádný produkt nebyl nalezen.")

def average_price():
    total_price = sum(p["price"] for p in products)
    avg_price = total_price / len(products)

    print(f"\nPrůměrná cena produktů je {avg_price}€")

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
    print("8. Pruměrná cena produktú")
    print("9. Upravit jméno a cenu produktú\n")


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
        print("")
        menu()
    elif choice == 4:
        highest_price()
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
    elif choice == 8:
        average_price()
        print("")
        menu()
    elif choice == 9:
        edit_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
