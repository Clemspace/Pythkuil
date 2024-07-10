VOWELS = set('aeiouäëöüîûâêôáéíóúàèìòù')
CONSONANTS = set('pbtdkgfvţḑszšžçxhļlrmnňŋy')

def is_vowel(char):
    return char.lower() in VOWELS

def is_consonant(char):
    return char.lower() in CONSONANTS

def classify_chars(word):
    return ['V' if is_vowel(c) else 'C' if is_consonant(c) else 'X' for c in word]

def get_char_pattern(word):
    return ''.join(classify_chars(word))