import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

message = "Welcome"
messages = ["Hello", "Cześć", "Good job"]

def click():
    global message
    message = random.choice(messages)

def draw(canvas):
    canvas.draw_text(message, [50, 112], 48, "Red") # jesli nie uzywam zadnej zmiennej to moge message bez global

frame = simplegui.create_frame("Python :)", 300, 200)

frame.add_button("Click me", click) # przekazuje adres w pamieci do click - nie wywowluje tej # jesli
# byloby click() to zwrociło by nam None bo w click nie ma zadnego returna

frame.set_draw_handler(draw)

frame.start()

