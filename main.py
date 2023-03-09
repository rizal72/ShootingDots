def on_sound_loud():
    pass
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_a():
    NAVE.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Shoot():
    global shooting, COLPO
    shooting = 1
    COLPO = game.create_sprite(NAVE.get(LedSpriteProperty.X), NAVE.get(LedSpriteProperty.Y))
    COLPO.set(LedSpriteProperty.BRIGHTNESS, 20)
    for index in range(4):
        COLPO.change(LedSpriteProperty.Y, -1)
        basic.pause(50)
        if COLPO.is_touching(NEMICO) or NEMICO.is_touching(COLPO):
            NEMICO.delete()
            soundExpression.happy.play()
            game.add_score(1)
            COLPO.delete()
    if COLPO.get(LedSpriteProperty.Y) <= 0:
        COLPO.delete()
    shooting = 0

def on_button_pressed_ab():
    if not (shooting):
        Shoot()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    NAVE.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if game.is_paused():
        game.resume()
    else:
        game.pause()
    if game.is_game_over():
        control.reset()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

NEMICO: game.LedSprite = None
COLPO: game.LedSprite = None
shooting = 0
NAVE: game.LedSprite = None
music.set_built_in_speaker_enabled(True)
music.set_volume(100)
game.set_score(0)
speed = 1000
NAVE = game.create_sprite(2, 4)

def on_forever():
    global speed, NEMICO
    if speed >= 100:
        speed += -50
    NEMICO = game.create_sprite(randint(0, 4), 0)
    NEMICO.set(LedSpriteProperty.BRIGHTNESS, 200)
    basic.pause(500)
    for index2 in range(4):
        NEMICO.change(LedSpriteProperty.Y, 1)
        basic.pause(speed)
        if NEMICO.is_touching(NAVE):
            music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
            game.game_over()
    if NEMICO.is_touching_edge():
        NEMICO.delete()
basic.forever(on_forever)
