
import string

alphabet = string.ascii_lowercase

list_alph = list(alphabet)

def change(n):
    for i in range(len(list_alph)):
        print(i)
        
        
def shift(n):
    shift_listed = list_alph[n:]
    shift_listed.extend(list_alph[:n])
    empty_word = ""
    for char in shift_listed:
        empty_word += char
    return empty_word