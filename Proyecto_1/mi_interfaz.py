import PySimpleGUI as pg

pg.theme("DarkBlue")

layout = [
    [pg.Text(text="MI PRIMERA INTERFAZ"), ],
    [pg.InputText(key = "num_1"), pg.InputText(key = "num_2")],
    [pg.Button("SUMAR"), pg.Button("MULTIPLICAR")],
    # [pg.Slider((0,10), orientation="horizontal")],
    [pg.Output(size= (90,10))]
    
]

ventana = pg.Window("MI APLICACION", layout)

def sumar(*args):
    return sum(args)

while True:
    evento, valor = ventana.read()      #|  valor lee lo que ingresa el usuario
    if evento == pg.WIN_CLOSED:
        ventana.close()
        break
    if evento == "SUMAR":
        print(sumar(int(valor["num_1"]), int(valor["num_2"])))
    if evento == "MULTIPLICAR":
        print((int(valor["num_1"]) * int(valor["num_2"])))
