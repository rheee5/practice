#! python3
# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text on the clipboard.


#import pyperclip
import pyperclip
pyperclip.copy('''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars''')
orig_text = pyperclip.paste()

# seperate lines and add stars
newline = orig_text.split('\n')
for i in range(len(newline)):  # loop through all index in the "lines" list
    newline[i] = '* ' + newline[i]  # add star to each string in the list
text = '\n'.join(newline)
print(text)
print(newline)
