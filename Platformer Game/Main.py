import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
from RectangleCollision import collision

Texture = 'Textures/'
Level = 0
# Window
window = pyglet.window.Window(caption='Platformer Game' ,width=600,height=600)
window.set_location(window.screen.width//2-window.width//2, window.screen.height//2-window.height//2)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Key handler
key_handler = key.KeyStateHandler()
window.push_handlers(key_handler)

# Mouse handler
mouse_handler = mouse.MouseStateHandler()
window.push_handlers(mouse_handler)
# Start menu True or False
Start = True

# Object

ObjectBatch = pyglet.graphics.Batch()
# Start Menu
StartButton = pyglet.image.load(Texture+ 'Start button.png')
StartLabel = pyglet.text.Label('Platformer game', x=50,y=500,color=(0,128,0,255), font_size=50)
# Player
PlayerImage1 = pyglet.image.load(Texture+ 'Player=Left.png')
PlayerImage2 = pyglet.image.load(Texture+ 'Player=Right.png')
Player = pyglet.sprite.Sprite(PlayerImage2 ,x=100,y=200, batch=ObjectBatch)
PlayerOldPosY = 0
Jump = False
# Blocks
BlockImage1 = pyglet.image.load(Texture+ 'Grass.png')
if Level == 0:
    Block1 = pyglet.sprite.Sprite(BlockImage1 ,x=0,y=100, batch=ObjectBatch)
    Block2 = pyglet.sprite.Sprite(BlockImage1 ,x=32,y=100, batch=ObjectBatch)
    Block3 = pyglet.sprite.Sprite(BlockImage1 ,x=64,y=100, batch=ObjectBatch)
    Block4 = pyglet.sprite.Sprite(BlockImage1 ,x=96,y=100, batch=ObjectBatch)
    Block5 = pyglet.sprite.Sprite(BlockImage1 ,x=128,y=100, batch=ObjectBatch)
    Block6 = pyglet.sprite.Sprite(BlockImage1 ,x=160,y=100, batch=ObjectBatch)
    Block7 = pyglet.sprite.Sprite(BlockImage1 ,x=192,y=100, batch=ObjectBatch)
    Block8 = pyglet.sprite.Sprite(BlockImage1 ,x=224,y=100, batch=ObjectBatch)
    Block9 = pyglet.sprite.Sprite(BlockImage1 ,x=256,y=100, batch=ObjectBatch)
    Block10 = pyglet.sprite.Sprite(BlockImage1 ,x=288,y=100, batch=ObjectBatch)
    Block11 = pyglet.sprite.Sprite(BlockImage1 ,x=320,y=100, batch=ObjectBatch)
    Block12 = pyglet.sprite.Sprite(BlockImage1 ,x=352,y=100, batch=ObjectBatch)
    Block13 = pyglet.sprite.Sprite(BlockImage1 ,x=384,y=100, batch=ObjectBatch)
    Block14 = pyglet.sprite.Sprite(BlockImage1 ,x=416,y=100, batch=ObjectBatch)
    Block15 = pyglet.sprite.Sprite(BlockImage1 ,x=448,y=100, batch=ObjectBatch)
    Block16 = pyglet.sprite.Sprite(BlockImage1 ,x=480,y=100, batch=ObjectBatch)
    Block17 = pyglet.sprite.Sprite(BlockImage1 ,x=512,y=100, batch=ObjectBatch)
    Block18 = pyglet.sprite.Sprite(BlockImage1 ,x=544,y=100, batch=ObjectBatch)
    Block19 = pyglet.sprite.Sprite(BlockImage1 ,x=576,y=100, batch=ObjectBatch)
def BlockSolid(BlockX, BlockY):
    global Jump, PlayerOldPosY
    if collision.rectangle(Player.x,Player.y ,BlockX+5,BlockY+30 ,32,32 ,22,2):
        Player.y += 1
        if key_handler[key.W]:
            PlayerOldPosY = Player.y
            Jump = True
    if collision.rectangle(Player.x,Player.y+0.1 ,BlockX,BlockY ,32,32 ,32,2):
        Jump = False
    if collision.rectangle(Player.x,Player.y ,BlockX,BlockY+1 ,32,32 ,2,30):
        Player.x -= 1
    if collision.rectangle(Player.x,Player.y ,BlockX+30,BlockY+1 ,32,32 ,2,30):
        Player.x += 1
# Enemy
EnemyImage1 = pyglet.image.load(Texture+ 'Enemy.png')
Enemy1 = pyglet.sprite.Sprite(EnemyImage1 ,x=220,y=132, batch=ObjectBatch)
# Goal
GoalImage1 = pyglet.image.load(Texture+ 'Goal.png')
Goal1 = pyglet.sprite.Sprite(GoalImage1 ,x=544,y=132, batch=ObjectBatch)
# Mouse Position
MouseX = 0
MouseY = 0
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global MouseX, MouseY
    MouseX = x
    MouseY = y
@window.event
def on_mouse_motion(x, y, dx, dy):
    global MouseX, MouseY
    MouseX = x
    MouseY = y

# Update function
def update(dt):
    global Start, Jump
    # If Start = True
    if Start == True:
        pyglet.gl.glClearColor(0.5,1,1,0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        if collision.rectangle(MouseX,MouseY ,200,300 ,1,1 ,183,65):

            if mouse_handler[mouse.LEFT]: Start = False

    # If start = False
    if Start == False:
        pyglet.gl.glClearColor(0,1,1,0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        Player.y -= 1

        if key_handler[key.A]:
            Player.x -= 1
            Player.image = PlayerImage1
        if key_handler[key.D]:
            Player.x += 1
            Player.image = PlayerImage2
        if Jump == True:
            Player.y += 3
            if Player.y >= PlayerOldPosY + 80: Jump = False
        if Level == 0:
            BlockSolid(Block1.x,Block1.y)
            BlockSolid(Block2.x,Block2.y)
            BlockSolid(Block3.x,Block3.y)
            BlockSolid(Block4.x,Block4.y)
            BlockSolid(Block5.x,Block5.y)
            BlockSolid(Block6.x,Block6.y)
            BlockSolid(Block7.x,Block7.y)
            BlockSolid(Block8.x,Block8.y)
            BlockSolid(Block9.x,Block9.y)
            BlockSolid(Block10.x,Block10.y)
            BlockSolid(Block11.x,Block11.y)
            BlockSolid(Block12.x,Block12.y)
            BlockSolid(Block13.x,Block13.y)
            BlockSolid(Block14.x,Block14.y)
            BlockSolid(Block15.x,Block15.y)
            BlockSolid(Block16.x,Block16.y)
            BlockSolid(Block17.x,Block17.y)
            BlockSolid(Block18.x,Block18.y)
            BlockSolid(Block19.x,Block19.y)
        if collision.rectangle(Player.x,Player.y ,Enemy1.x,Enemy1.y ,32,32 ,32,32):
            if Level == 0:
                Player.x = 100
                Player.y = 200
# Draw the objects on screen
@window.event
def on_draw():
    window.clear()
    if Start == True:
        StartLabel.draw()
        StartButton.blit(200,300)
    if Start == False: ObjectBatch.draw()

# update the update function
pyglet.clock.schedule_interval(update, 1/120)
# Makes it work
pyglet.app.run()