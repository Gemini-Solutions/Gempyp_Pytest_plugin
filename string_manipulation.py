def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

def count_words(sentence):
    words = sentence.split()
    return(len(words))

def trucate_string(sentence, index):
    if (len(sentence) > index):
        return sentence[:index] + "..."
    return sentence

def remove_character_from_string(sentence, char):
    return sentence.replace(char, "")
