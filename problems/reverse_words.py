# reverse words in a sentence 
# input: "I love python"
# output: "Python love I"

def reverse_words(txt):
    x = txt.split()
    print(x[::-1])

reverse_words("I love python")