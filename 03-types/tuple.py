'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
In Python tuples are written with round brackets.
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
# Chcete-li vytvořit n-tici pouze s jednou položkou, musíte za položku přidat čárku, pokud Python nerozpozná proměnnou jako n-tici.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# You can specify a range of indexes by specifying where to start and where to end the range.
# Rozsah indexů můžete určit určením, kde začít a kde ukončit rozsah.
# When specifying a range, the return value will be a new tuple with the specified items.
# Při zadávání rozsahu bude vrácená hodnota nová n-tice se zadanými položkami.
print(f'chars[2:5]: {chars[2:5]}')

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Negativní indexování znamená začátek od konce, -1 odkazuje na poslední položku, -2 odkazuje na předposlední položku atd.
# Specify negative indexes if you want to start the search from the end of the tuple:
# Pokud chcete zahájit hledání od konce n-tice, zadejte záporné indexy:
# This example returns the items from index -4 (included) to index -1 (excluded)
# Tento příklad vrátí položky z indexu -4 (zahrnuto) do indexu -1 (vyloučeno)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# To determine how many items a tuple has, use the len() method:
# Chcete-li zjistit, kolik položek má n-tice, použijte metodu len():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
