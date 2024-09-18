import pgzrun
import random
message = ""
TITLE = "Good shot"
WIDTH = 600
HEIGHT = 500
cat = Actor("caticon1")
def draw():
    screen.clear()
    screen.fill("lightblue")
    cat.draw()
    screen.draw.text(message,center=(300,20),fontsize=30)

def place_cat():
    cat.x=random.randint(50,450)
    cat.y=random.randint(50,450)




def on_mouse_down(pos):
    global message
    if cat.collidepoint(pos):
        message = "Good shot"
        place_cat()
    else:
        message = "You missed"





    







pgzrun.go()