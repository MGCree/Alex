import webbrowser as web

def openWebPage():
    url = input("What would you like to surch for:  ")

    web.open(url, new=2)
