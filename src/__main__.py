from src.app.gui import Gui

app = Gui(sirina=400, visina=400)

while True:
    app.narisi()
    app.vnos()
    if app.konec():
        break
