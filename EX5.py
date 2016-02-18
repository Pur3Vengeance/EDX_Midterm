#items_price takes quantity (list a) and multiplies with cost (list b)
# to give a total cost of items. Lists are assumed to be equal length.

def items_price(a,b):

    total = 0
    for x in range(len(a)):
        total = a.pop(0)*b.pop(0) + total
    return(total)

a = [4, 6, 3, 1, 10]
b = [5, 6, 2, 4, 1]

items_price(a,b)
    
