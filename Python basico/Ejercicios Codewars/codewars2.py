def duplicate_count(text):
    n = 0
    for i in text:
        for j in text[text.index(i)+1::]:
            print(i,j)
            if i == j:
                n += 1
                text = text.replace(i,"")
                print(text)
                break

    return n

print(duplicate_count("invisibilidad"))
