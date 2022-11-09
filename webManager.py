import webbrowser as web

def openWebPage():
    url = input("What would you like to search for:  ")

    web.open_new_tab(url + ".com")
