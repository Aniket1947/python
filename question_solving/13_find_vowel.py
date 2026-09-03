# def count_vowel(text):
#     vowel=['a','e','i','o','u']
#     count=0
#     for char in text:
#         if char.lower() in vowel:
#             count += 1
#     print(count)

# text=input("Enter the Words:")
# count_vowel(text)


def count_vowel(text):
    vowel=['a','e','i','o','u']
    count=0
    for char in text:
        if char.lower() not in vowel:
            count += 1
    print(count)

text=input("Enter the Words:")
count_vowel(text)