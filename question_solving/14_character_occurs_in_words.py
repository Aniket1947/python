def occurence(text):
    char="p"
    count=0
    for t in text:
        if t.lower() == char:
            count += 1
    print(count)

text=input("Enter the Words:")
occurence(text)