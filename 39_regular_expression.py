import re

text="The quick brown for fox jumps over the lazy dogs. 13@ age year old       He is very funny"

# match=re.search("fox",text)
# print(match)
# if match:
#     print("Match Found")
#     print("Starting Index:",match.start())
#     print("Ending Index:",match.end())

# matches=re.findall("the",text,re.IGNORECASE)
# print(matches)

# replace=re.sub("13@","13",text)
# print(replace)
#################################################################################################################

def convert_into_dashes(text):
    special_char_removing=re.sub(r'[^a-zA-z0-9 ]',"",text)
    print(special_char_removing)
    dashes_text=re.sub(r'\s+','-',special_char_removing)
    return dashes_text.lower()


text="The quick brown for fox jumps over the lazy dogs. 13@ age year old       He is very funny"
new=convert_into_dashes(text)
print(new)

###############################################################################################################

# def convert_into_dashes(text):
#     special_char_removing='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
#     cleaned_text=''.join(c for c in text if c in special_char_removing)
#     dashes_text = '-'.join(cleaned_text.split())
#     return dashes_text.lower()


# text="The quick brown for fox jumps over the lazy dogs. 13@ age year old       He is very funny"
# new=convert_into_dashes(text)
# print(new)


