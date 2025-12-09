def on_received_number(receivedNumber):
    global numDiceMicrobit2
    numDiceMicrobit2 = randint(1, 6)
    basic.show_number(numDiceMicrobit2)
    if numDiceMicrobit2 > numDice:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global numDice
    numDice = randint(1, 6)
    basic.show_number(numDice)
    radio.send_number(numDice)
input.on_button_pressed(Button.A, on_button_pressed_a)

numDice = 0
numDiceMicrobit2 = 0
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
