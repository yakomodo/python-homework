import string

def create_hashtag(text):
    for char in string.punctuation:
        text = text.replace(char, ' ')
    
    words = text.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    
    return hashtag

user_input = input("Введіть текст для hashtag: ")
print(create_hashtag(user_input))