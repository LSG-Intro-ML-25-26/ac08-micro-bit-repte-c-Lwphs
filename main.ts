radio.onReceivedNumber(function (receivedNumber) {
    numDiceMicrobit2 = randint(1, 6)
    basic.showNumber(numDiceMicrobit2)
    if (numDiceMicrobit2 > receivedNumber) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
input.onButtonPressed(Button.A, function () {
    numDice = randint(1, 6)
    basic.showNumber(numDice)
    radio.sendNumber(numDice)
})
let numDice = 0
let numDiceMicrobit2 = 0
radio.setGroup(1)
basic.forever(function () {
	
})
