'''
launches a map in the browser using an address from the command line

'''


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('http://google.com/maps/place/' + address)
