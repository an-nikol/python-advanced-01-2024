def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []

    for product_name, price in args:
        if price > budget:
            break
        elif (product_name not in bought_products) and (product_name in grocery_list) and (price <= budget):
            bought_products.append(product_name)
            budget -= price

    result = ""
    if len(bought_products) == len(grocery_list):
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."

    else:
        diff = [x for x in grocery_list if x not in bought_products]
        result += f"You did not buy all the products. Missing products: {', '.join(diff)}."

    return result

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
