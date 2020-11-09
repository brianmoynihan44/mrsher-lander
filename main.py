def on_up_pressed():
    mySprite.ay = blast
    mySprite.set_image(img("""
        . . . . 5 5 . . 5 . . 5 . . . . 
                . . 5 . . . . 5 . . 5 . . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . . 4 9 4 4 4 4 4 4 9 4 . . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . . . . 
                . . 4 4 4 f f f f 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . . . 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 . . . 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . . . . 
                . . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 9 9 9 9 9 9 9 2 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        200,
        0)
    music.pew_pew.play()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global dart
    for index in range(2):
        dart = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 9 9 9 9 9 9 9 2 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            200,
            0)
        music.pew_pew.play()
        pause(200)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    mySprite.ay = idle
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . . 4 9 4 4 4 4 4 4 9 4 . . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . . . . 
                . . 4 4 4 f f f f 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . . . 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 . . . 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . . . . 
                . . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    mySprite.ax = blast
    mySprite.set_image(img("""
        . . 5 . . . . . . . . . . . . . 
                . 5 . . . . . . . . . . . . . . 
                5 . 4 4 4 4 4 4 4 4 4 4 . . . . 
                5 . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . 5 4 9 4 4 4 4 4 4 9 4 . . . . 
                5 . 4 7 4 9 9 9 9 4 7 4 . . . . 
                5 . 4 4 4 f f f f 4 4 4 . . . . 
                5 . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . 7 5 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 7 7 7 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . . . . 
                5 . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    mySprite.ax = idle
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . . 4 9 4 4 4 4 4 4 9 4 . . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . . . . 
                . . 4 4 4 f f f f 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . . . 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 . . . 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . . . . 
                . . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    mySprite.ax = idle
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . . 4 9 4 4 4 4 4 4 9 4 . . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . . . . 
                . . 4 4 4 f f f f 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . . . 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 . . . 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . . . . 
                . . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_overlap_tile(sprite, location):
    info.change_score_by(3)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile)

def on_right_pressed():
    mySprite.ax = 0 - blast
    mySprite.set_image(img("""
        . . . . . . . . . . . 5 . . . . 
                . . . . . . . . . . . . 5 . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . 5 . . 
                . . 4 4 4 5 5 5 5 4 4 4 . 5 . . 
                . . 4 9 4 4 4 4 4 4 9 4 5 . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . 5 . . 
                . . 4 4 4 f f f f 4 4 4 . 5 . . 
                . . 4 4 4 4 4 4 4 4 4 4 . 5 . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . 7 5 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 7 7 7 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . 5 . . 
                . . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    mySprite.ay = idle
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . . 4 9 4 4 4 4 4 4 9 4 . . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . . . . 
                . . 4 4 4 f f f f 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . 4 . . . 4 f f 4 5 7 . 4 . . . 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                . 4 . . . 4 4 4 4 7 7 . 4 . . . 
                . . 5 5 4 4 5 5 4 4 7 . . . . . 
                . . 5 5 4 5 5 5 5 4 5 5 . . . . 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    mySprite.ay = 0 - blast
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                . . 4 4 4 5 5 5 5 4 4 4 . . . . 
                . 5 4 9 4 4 4 4 4 4 9 4 . . . . 
                . . 4 7 4 9 9 9 9 4 7 4 . . . . 
                . . 4 4 4 f f f f 4 4 4 . . . . 
                . . 4 4 4 4 4 4 4 4 4 4 . 5 . . 
                . . 4 4 4 4 4 4 4 4 4 4 . . . . 
                5 4 . . . 4 f f 4 5 7 . 4 . . 5 
                4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
                5 4 . . . 4 4 4 4 7 7 . 4 . . . 
                . 5 5 5 4 4 5 5 4 4 7 . . . 5 . 
                5 . 5 5 4 5 5 5 5 4 5 5 . . . 5 
                . 5 5 5 4 5 5 5 5 4 5 5 5 5 . 5 
                . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_menu_pressed():
    music.set_volume(10)
    game.reset()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_overlap_tile2(sprite, location):
    info.change_score_by(2)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile2)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.clouds, 100)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_overlap_tile3(sprite, location):
    info.change_score_by(6)
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile3)

bogey: Sprite = None
dart: Sprite = None
mySprite: Sprite = None
idle = 0
blast = 0
music.set_volume(30)
GOING_UP = "F E A B G C F E "
blast = 46
idle = 0
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 4 4 4 4 4 4 4 4 4 4 . . . . 
            . . 4 4 4 5 5 5 5 4 4 4 . . . . 
            . . 4 9 4 4 4 4 4 4 9 4 . . . . 
            . . 4 7 4 9 9 9 9 4 7 4 . . . . 
            . . 4 4 4 f f f f 4 4 4 . . . . 
            . . 4 4 4 4 4 4 4 4 4 4 . . . . 
            . . 4 4 4 4 4 4 4 4 4 4 . . . . 
            . 4 . . . 4 f f 4 5 7 . 4 . . . 
            4 4 4 4 4 4 f f 4 4 4 4 4 4 . . 
            . 4 . . . 4 4 4 4 7 7 . 4 . . . 
            . . 5 5 4 4 5 5 4 4 7 . . . . . 
            . . 5 5 4 5 5 5 5 4 5 5 . . . . 
            . 5 5 5 4 5 5 5 5 4 5 5 5 5 . . 
            . 5 5 4 4 5 5 5 5 4 4 5 5 5 . .
    """),
    SpriteKind.player)
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 6 6 6 6 6 6 6 6 6 6 . . . . 
            . . 6 6 6 a a a a 6 6 6 . . . . 
            . . 6 9 6 6 6 6 6 6 9 6 . . . . 
            . . 6 8 6 9 9 9 9 6 8 6 . . . . 
            . . 6 6 6 f f f f 6 6 6 . . . . 
            . . 6 6 6 6 6 6 6 6 6 6 . . . . 
            . . 6 6 6 6 6 6 6 6 6 6 . . . . 
            . 6 . . . 6 f f 6 a b . 6 . . . 
            6 6 6 6 6 6 f f 6 6 6 6 6 6 . . 
            . 6 . . . 6 6 6 6 b b . 6 . . . 
            . . a a 6 6 a a 6 6 b . . . . . 
            . . a a 6 a a a a 6 a a . . . . 
            . a a a 6 a a a a 6 a a a a . . 
            . a a 6 6 a a a a 6 6 a a a . .
    """),
    SpriteKind.player)
# This is Gravity
mySprite.ay = 66
scene.camera_follow_sprite(mySprite)
light.set_all(0x007fff)
tiles.set_tilemap(tilemap("""
    level
"""))
effects.star_field.start_screen_effect()

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 7 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 f 7 f 7 7 . . . . . 
                    7 7 7 7 7 7 f 7 f 7 7 7 7 7 7 . 
                    . . . . 7 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 7 7 7 7 7 . . . . . 
                    . . . 7 7 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 7 7 7 7 . . . . . . 
                    . . . . . 7 7 7 7 . . . . . . . 
                    . . . . . 7 . . 7 . . . . . . . 
                    . . . . . 7 . . 7 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(142, randint(0, 120))
game.on_update_interval(2000, on_update_interval)

def on_forever():
    global GOING_UP
    GOING_UP = "F E A B G C F E "
    music.play_melody(GOING_UP, 120)
forever(on_forever)
