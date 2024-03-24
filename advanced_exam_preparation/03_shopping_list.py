def shopping_list(budget, **kwargs):
    result = ""
    basket = {}

    if budget < 100:
        result += "You do not have enough budget."
        return result

    for type_product, tuples in kwargs.items():
        price, qty = tuples
        total_price = price * qty

        if total_price <= budget and len(basket) < 5:
            budget -= total_price
            basket[type_product] = total_price

    for product, price in basket.items():
        result += f"You bought {product} for {price:.2f} leva.\n"

    return result


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
