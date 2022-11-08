import webbrowser as web

def openWebPage():
    url = input("What would you like to search for:  ")

    web.open(url, new=2)
