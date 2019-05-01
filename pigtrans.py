def pig(word):
    
    first_let = word[0]
    
    # check for vowel
    if first_let in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_let + 'ay'
    
    return pig_word

x = input('Let me translate a word. : ')

print(pig(x))


