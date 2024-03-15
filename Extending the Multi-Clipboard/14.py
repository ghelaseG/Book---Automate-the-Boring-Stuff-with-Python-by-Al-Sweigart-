# mcb.py - saves and loads pieces of text to the clipboard.
# usage: py.exe mcb.py save <keyword> - saves clipboard to keyword
#        py.exe mcb.py <keyword> - loads keyword to clipboard.
#        py.exe mcb.py list - loads all keywords to clipboard.
#        python3 extendedMcb.py delete <keyword> or deleteall
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
   mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for keyword in list(mcbShelf.keys()):
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
