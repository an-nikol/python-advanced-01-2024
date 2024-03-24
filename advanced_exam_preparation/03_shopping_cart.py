def shopping_cart (*args):
    MAX_PRODUCT_SOUP, MAX_PRODUCT_PIZZA, MAX_PRODUCT_DESSERT  = 3, 4, 2

    shopping_list = {"Soup": [], "Pizza": [], "Dessert": []}

    for data in args:
        if data == "Stop":
            break

        meal_type, product = data[0], data[1]

        if product in shopping_list[meal_type]:
            continue

        if meal_type == "Soup" and len(shopping_list[meal_type]) < MAX_PRODUCT_SOUP:
            shopping_list[meal_type].append(product)
        elif meal_type == "Pizza" and len(shopping_list[meal_type]) < MAX_PRODUCT_PIZZA:
            shopping_list[meal_type].append(product)
        elif meal_type == "Dessert" and len(shopping_list[meal_type]) < MAX_PRODUCT_DESSERT:
            shopping_list[meal_type].append(product)

    shopping_list = dict(sorted(shopping_list.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ""

    if not any(shopping_list.values()):
        result += "No products in the cart!"
        return result

    for meal, products in shopping_list.items():
        result += f"{meal}:\n"
        if products:
            sorted_products = sorted(products)
            for product in sorted_products:
                result += f" - {product}\n"

    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
