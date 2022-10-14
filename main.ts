control.onEvent(EventBusSource.MICROBIT_ID_ACCELEROMETER, EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE, function () {
    forca = input.acceleration(Dimension.Strength)
    if (forca > 1700) {
        strip.setPixelColor(0, neopixel.hsl(Math.map(Math.constrain(forca, 1600, 2000), 1600, 2000, 250, 0), 80, 50))
    }
})
let forca = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Orange))
basic.forever(function () {
    strip.shift(1)
    strip.show()
    basic.pause(20)
})
