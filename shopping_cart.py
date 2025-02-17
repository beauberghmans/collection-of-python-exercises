print("WELCOME TO OUR USELESS STORE!")
print("*****************************")
sort_item = input("What item are you purchasing? ")
price_item = input("What is the price of the following item? -> " + sort_item + " -> price per item: ")
quantity_item = input("How many units of the following item are you buying? -> " + sort_item + " -> # of units: ")

print(f"\nAdded {quantity_item} {sort_item}(s) to your shopping cart.")
print(f"Subtotal: ${float(price_item) * int(quantity_item)}")
