import eel


a=1
b=4

@eel.expose
def summer(c):
    if c=='a':
        return a
    else:
        return b
