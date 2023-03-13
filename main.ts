input.onButtonPressed(Button.A, function () {
    NAVE.move(-1)
})
function Shoot () {
    shooting = 1
    COLPO = game.createSprite(NAVE.get(LedSpriteProperty.X), NAVE.get(LedSpriteProperty.Y))
    COLPO.set(LedSpriteProperty.Brightness, 20)
    for (let index = 0; index < 4; index++) {
        COLPO.change(LedSpriteProperty.Y, -1)
        basic.pause(20)
        if (COLPO.isTouching(NEMICO) || NEMICO.isTouching(COLPO)) {
            NEMICO.delete()
            soundExpression.happy.play()
            game.addScore(1)
            COLPO.delete()
        }
    }
    if (COLPO.get(LedSpriteProperty.Y) <= 0) {
        COLPO.delete()
    }
    shooting = 0
}
input.onSound(DetectedSound.Loud, function () {
	
})
input.onButtonPressed(Button.AB, function () {
    if (!(shooting)) {
        Shoot()
    }
})
input.onButtonPressed(Button.B, function () {
    NAVE.move(1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (game.isPaused()) {
        game.resume()
    } else {
        game.pause()
    }
    if (game.isGameOver()) {
        control.reset()
    }
})
let NEMICO: game.LedSprite = null
let COLPO: game.LedSprite = null
let shooting = 0
let NAVE: game.LedSprite = null
music.setBuiltInSpeakerEnabled(true)
music.setVolume(100)
game.setScore(0)
let speed = 1000
NAVE = game.createSprite(2, 4)
basic.forever(function () {
    if (speed >= 100) {
        speed += -50
    }
    NEMICO = game.createSprite(randint(0, 4), 0)
    NEMICO.set(LedSpriteProperty.Brightness, 200)
    basic.pause(500)
    for (let index = 0; index < 4; index++) {
        NEMICO.change(LedSpriteProperty.Y, 1)
        basic.pause(speed)
        if (NEMICO.isTouching(NAVE)) {
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
            game.gameOver()
        }
    }
    if (NEMICO.isTouchingEdge()) {
        NEMICO.delete()
    }
})
