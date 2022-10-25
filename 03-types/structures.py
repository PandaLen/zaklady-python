veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."

def charFrequency(txt):
    return sorted([(char, txt.count(char)) for char in set(txt)], reverse=True, key=lambda i: i[1])

print(charFrequency(veta))