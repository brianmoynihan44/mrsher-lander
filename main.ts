controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.ay = blast
    mySprite.setImage(img`
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
        `)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    dart = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 200, 0)
    music.pewPew.play()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    for (let index = 0; index < 2; index++) {
        dart = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 200, 0)
        music.pewPew.play()
        pause(200)
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.ay = idle
    mySprite.setImage(img`
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
        `)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.ax = blast
    mySprite.setImage(img`
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
        `)
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.ax = idle
    mySprite.setImage(img`
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
        `)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.ax = idle
    mySprite.setImage(img`
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
        `)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleBlueCrystal, function (sprite, location) {
    info.changeScoreBy(3)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.ax = 0 - blast
    mySprite.setImage(img`
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
        `)
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.ay = idle
    mySprite.setImage(img`
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
        `)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.ay = 0 - blast
    mySprite.setImage(img`
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
        `)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    music.setVolume(10)
    game.reset()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite, location) {
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.clouds, 100)
    music.baDing.play()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite, location) {
    info.changeScoreBy(6)
    game.over(true)
})
let bogey: Sprite = null
let dart: Sprite = null
let mySprite: Sprite = null
let idle = 0
let blast = 0
music.setVolume(30)
let GOING_UP = "F E A B G C F E "
blast = 46
idle = 0
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
let mySprite2 = sprites.create(img`
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
    `, SpriteKind.Player)
// This is Gravity
mySprite.ay = 66
scene.cameraFollowSprite(mySprite)
light.setAll(0x007fff)
tiles.setTilemap(tilemap`level`)
effects.starField.startScreenEffect()
game.onUpdateInterval(2000, function () {
    bogey = sprites.create(img`
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
        `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    bogey.setPosition(142, randint(0, 120))
})
forever(function () {
    GOING_UP = "F E A B G C F E "
    music.playMelody(GOING_UP, 120)
})
