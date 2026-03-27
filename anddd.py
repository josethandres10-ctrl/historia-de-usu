print("welcome to the app!!")
# calculate quantity and prince for the total of the product
def calculationTotalProduct (quantity, price ):
    result = quantity * price
    return result 

validateProduct = True
while validateProduct == True:
    nameProduct = input("Enter the name product: ").strip()

    if nameProduct and not nameProduct.isdigit():
        validateProduct = False

    elif nameProduct.isdigit():
        print("Error: the name to product only cant numbers")

    else:
        print("Error: the name of the product cant empty")
            
validatePrice = True  
while validatePrice:
    try:
        price = float(input("Enter the price of the product: "))

        if price > 0:
            validatePrice = False

        else:
            print("Error: the price to product is only positive")

    except ValueError:
        print("Error: please enter a valide number")

validateQuantity = True
while validateQuantity:
    try:
        quantity = int(input("Enter the quantity: "))

        if quantity > 0:
            validateQuantity = False

        else:
            print("Error: the quantity is only positive")
                
    except ValueError:
        print("Error: please enter a valide number")

# show data
print(f"""
Product: {nameProduct}
Price: {price}
Quantity: {quantity}
Total cost: {calculationTotalProduct(quantity, price)}""")