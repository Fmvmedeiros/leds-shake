control.onEvent(EventBusSource.MICROBIT_ID_ACCELEROMETER, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (input.acceleration(Dimension.Strength) > 2100) {
        Tiro()
    }
})
function Tiro () {
    for (let index = 0; index <= strip.length(); index++) {
        strip.setPixelColor(index - 1, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(index, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.pause(60)
    }
}
let stop = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Green))
basic.forever(function () {
    let go = 0
    if (go) {
        stop = 0
        strip.clear()
        strip.show()
    }
})
