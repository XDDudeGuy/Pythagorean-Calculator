#!/bin/env python3
import PySimpleGUI as sg #type: ignore
from math import sqrt

def leg_calc(c, x):
	return sqrt(int(c)**2-int(x)**2)

def hypotenuse(a, b):
	return sqrt(int(a)**2+int(b)**2)

layout = [
		[sg.Text("a="), sg.Input(key="-LEG_A-", size=(10,1)), sg.Text("b="), sg.Input(key="-LEG_B-", size=(10,1)), sg.Text("c="), sg.Input(key='-HYP-', size=(10,1))],
		  	[sg.Text(size=(40,1), key='-OUTPUT-')],
		 	[sg.Button("Calculate Hypotenuse"), sg.Button("Calculate Leg"), sg.Button('Quit')]
		 ]

window = sg.Window("   Pythagoras", layout)

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	try:
		if event == "Calculate Hypotenuse":
			window['-OUTPUT-'].update(f"Hypotenuse = " + str(hypotenuse(values["-LEG_A-"], values["-LEG_B-"])))
		elif event == "Calculate Leg":
			if not (values["-LEG_B-"]==""):
				window["-OUTPUT-"].update("Leg A Length = " + str(leg_calc(values["-HYP-"], values["-LEG_B-"])))
			else:
				window["-OUTPUT-"].update("Leg B Length = " + str(leg_calc(values["-HYP-"], values["-LEG_A-"])))
	except ValueError:
		window["-OUTPUT-"].update("ERROR")


if __name__ == "__main__":
	window.close()