def stock_availability(list_of_cupcakes, command, *args):
    if command == "delivery":
        for arg in args:
            arg = str(arg)
            if arg.isalpha():
                list_of_cupcakes.append(arg)

    elif command == "sell":
        if not args:
            list_of_cupcakes.pop(0)
            return list_of_cupcakes

        for arg in args:
            arg = str(arg)
            if not arg.isalpha():
                [list_of_cupcakes.pop(0) for _ in range(int(arg))]
            elif arg.isalpha():
                if arg in list_of_cupcakes:
                    while arg in list_of_cupcakes:
                        list_of_cupcakes.remove(arg)
    return list_of_cupcakes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
