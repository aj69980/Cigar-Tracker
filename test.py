god = "$6.50"
fox = "$6.85"



def price_as_float(x):
    price = (float(x[1:5]))
    price = str(price)
    return price

god_price = price_as_float(god)
fox_price = price_as_float(fox)


print(type(fox_price))


# if god_price < fox_price:
#     best_price = god_price
# else:
#     best_price = fox_price
    
# # print(best_price)