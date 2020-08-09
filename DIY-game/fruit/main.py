import pgzrun
from random import randint

apple = Actor("apple")

def place_apple():
    apple.x = randint(0,300)
    apple.y = randint(0,200)
    apple.r = 1

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('good job!')
        place_apple()

def draw():
    screen.clear()
    apple.draw()
    

pgzrun.go()