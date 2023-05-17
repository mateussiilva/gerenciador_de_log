import PySimpleGUI as sg
from setings import HEIGHT,WIDTH

layout = [
    [sg.Input(""),sg.Button("Buscar",key='-BUSCAR-')],
    [sg.Multiline(s=(WIDTH,HEIGHT),key='-SAIDA-')],
]


window = sg.Window(" ", layout, size=(WIDTH,HEIGHT))

while True:
    events, value = window.read()
    
    if events == sg.WIN_CLOSED:
        break
    elif events == '-BUSCAR-':
        with open("log.log",'r') as file:
            
            linhas = [
                [linha] 
                for linha in file.readlines()
                if len(linha) > 1
                ]
        window['-SAIDA-'].update(linhas[:50])
    else:
        print(events)
    
    
window.close()