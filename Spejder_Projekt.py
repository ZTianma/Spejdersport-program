# lav et program som gemmer kontaktoplysninger i en text fil test
# if values.strip(): this line of code in memoriam of strip
# Z is a impostor
import PySimpleGUI as sg


layout = [[sg.Text('write your full name:', size=(20, 1)), sg.InputText()],
          [sg.Text('write your email:     ', size=(20, 1)), sg.InputText()],
          [sg.Text('write your phone nr.:', size=(20, 1)), sg.InputText()],
          [sg.Text('write your address:   ', size=(20, 1)), sg.InputText()],
          [sg.Text("strip", size=(50, 1), key='output', text_color="red")],
          [sg.Button('Save'), sg.Button('close')]]

window = sg.Window('Spejdersport', layout, margins=(100, 100))
window.read()


def save():
    with open('Brugerfile.txt', 'w') as f:
        f.write('Name: ')
        f.write(values[0])
        f.write('\n')
        f.write('Email: ')
        f.write(values[1])
        f.write('\n')
        f.write('Phone nr: ')
        f.write(values[2])
        f.write('\n')
        f.write('Address: ')
        f.write(values[3])


def reset_fields():
    for x in values:
        window.Element(x).update(background_color="white")


def update_error(errormsg, number):
    reset_fields()
    window.Element("output").update(errormsg)
    print(number)
    if number == 4:
        for x in values:
            if not values[x]:
                window.Element(x).update(background_color="red")
    else:
        window.Element(number).update(background_color="red")


def valid(validationdata):
    if all(validationdata[y] for y in validationdata):
        print("your fields were not empty good job!")
    else:
        print("one of your input fields are empty")
        update_error("one of your input fields are empty", 4)
        return False
    if all(x.isspace() or x.isalpha() for x in validationdata[0]):
        print("correct name")
    else:
        print("incorrect name")
        update_error("invalid name", 0)
        return False
    if "@gmail.com" in validationdata[1]:
        print("correct email")
    else:
        print("incorrect email")
        update_error("invalid email", 1)
        return False
    if len(validationdata[2]) == 8 and validationdata[2].isnumeric():
        print("correct phone number")
    else:
        print("incorrect phone number")
        update_error("invalid phone number", 2)
        return False
    if all(x.isalnum() or x.isnumeric() for x in validationdata[3]):
        print("correct address")
    else:
        print("incorrect address")
        update_error("invalid address", 3)
        return False
    return True


while True:
    event, values = window.read()
    if event == 'close' or event == sg.WINDOW_CLOSED:
        break
    if event == 'Save':
        if not valid(values):
            continue
        save()
        break
