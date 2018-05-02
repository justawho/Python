#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes keyw from the shelf
#        py.exe mcb.pyw <keyword> - Loads keyword to clipbard
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.exe mcb.pyw del - Deletes all keywords.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

    # Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    #Delete keyword from shelve
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
    del(mcbShelf[sys.argv[2]])
    
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    #Delete all keywords from shelve
    elif sys.argv[1].lower() == 'del':
        for key in mcbShelf:
            del (mcbShelf[key])
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])



mcbShelf.close()
