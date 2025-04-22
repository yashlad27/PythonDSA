# write a function to count all vowels (a,e,i,o,u) in a string

def count_vowels(txt):
    vowels = ['a', 'e', 'i', 'o', 'u']
    x = 0
    
    for char in txt.lower():

        if char in vowels:
            x+=1

    return print(x)

txt = "I love python"

count_vowels(txt)


def count_vowels_set(t):
    v=set("aeiou")
    c=0
    for x in t.lower():
        if x in v:
            c+=1
    return c

print(count_vowels_set("yash lad"))
