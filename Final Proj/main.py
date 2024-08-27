# Final Project
# CS 111, Hayes & Reckinger

# Student Name: Le Nguyen (Nguyen)
# UIN: 656884422
# Project Name: Welcome to the Windy City!

import turtle
import random
global FONTSIZE
global inc, inc01, inc02, inc03, inc04
global screens
# For both
global picture_box01, caption_box01
global picture_box02, caption_box02
global arrow_pixel01, arrow_pixel02 
# for Vietnam
global food_list, location_list # Food attribute
global caption_list, location_caption_list # Location attribute
# for Chicago
global chicago_food_list, chicago_food_caption_list # Food attribute
global activity_list, activity_caption_list # Location attribute
# conclusion text
global conclusion_text_01, conclusion_text_02
FONTSIZE = 12
turtle.tracer(0)

# Code starts from here

def writeIntro(color, text):

    intro = turtle.Turtle()
    intro.hideturtle()
    intro.penup()
    intro.goto(0, 220)
    intro.showturtle()
    intro.pencolor(color)
    intro.pendown()
    intro.write(text, False, align = "center", font=("Helvetica", FONTSIZE*4, "bold"))

def draw_word_box(box, x, y, width, height, color, word):
   # draw
   box.goto(x+(width/2), y + 17 + (height/2))
   box.pendown()
   box.fillcolor(color)
   box.pencolor("black")
   box.begin_fill()
   for i in range(2):
        box.right(90)
        box.forward(height)
        box.right(90)
        box.forward(width)
   box.end_fill()
   box.penup()
   # text
   box.goto(x, y - 50)
   box.pencolor("dark blue")
   box.write(word, False, align = "center", font=("Helvetica", round(FONTSIZE*1.5), "bold"))

def writeText(text, x, y, color, text_choice):
    text.goto(x, y)
    text.pencolor(color)
    text.pendown()
    text.write(text_choice, False, align = "center", font=("Helvetica", FONTSIZE*2, "bold"))

def whiteScreen(x,y):  # transition to white screen where the question "How are you feeling today?"
    global inc
    inc += 1

    turtle.hideturtle()

    s.clear()
    s.bgpic(screens[inc])

    welcome_text_02 = "How are you feeling today?"
    writeIntro("black", welcome_text_02)

    turtle.addshape("option_red.gif")

    # option 1, move to the 3rd screen

    option_box = turtle.Turtle()
    option_box.shape("option_red.gif")
    option_box.penup()
    option_box.hideturtle()
    option_box.goto(-300, -50)
    option = "I'm missing home :("
    option_box.write(option, False, align = "center", font=("Helvetica", round(FONTSIZE*1.25), "bold"))
    option_box.showturtle()

    # option 2, move to the 4th screen

    option_box2 = turtle.Turtle()
    option_box2.shape("option_red.gif")
    option_box2.penup()
    option_box2.hideturtle()
    option_box2.goto(300, -50)
    option2 = "I want to explore Chicago!"
    option_box2.write(option2, False, align = "center", font=("Helvetica", round(FONTSIZE*1.25), "bold"))
    option_box2.showturtle()

    # transition to the module
    # module 1: "I'm missing home :("
    # module 2: "I want to explore!"
    option_box.onclick(module1)
    option_box2.onclick(module2) 

def module1(x,y): # Vietnam option
    global inc
    inc += 1

    s.clear()
    s.bgpic(screens[inc])
    intro2 = "Explore Little Vietnam in Chicago :)" 
    writeIntro("white", intro2)

    # menu selection starts here
    # food box

    turtle.addshape("box2.gif") 

    selection_food = turtle.Turtle()
    selection_food.shape("box2.gif")
    selection_food.hideturtle()
    selection_food.penup()
    selection_food.goto(-500,120)
    selection_food.showturtle()

    writeText(text, -510, 100, "white", "Cuisine")

    # location box 

    selection_location = turtle.Turtle()
    selection_location.shape("box2.gif")
    selection_location.hideturtle()
    selection_location.penup()
    selection_location.goto(-500,-120)
    selection_location.showturtle()

    writeText(text, -510, -140, "white", "Location")

    # on-click event

    selection_food.onclick(activity01)
    selection_location.onclick(activity02)

def setupArrow():
    
    global arrow_pixel01, arrow_pixel02

    arrow_pixel01 = turtle.Turtle()
    arrow_pixel01.shape("arrow.gif")
    arrow_pixel01.hideturtle()
    arrow_pixel01.penup()
    arrow_pixel01.goto(430,20)
    arrow_pixel01.showturtle()

    arrow_pixel02 = turtle.Turtle()
    arrow_pixel02.shape("arrow2.gif")
    arrow_pixel02.hideturtle()
    arrow_pixel02.penup()
    arrow_pixel02.goto(-70,20)
    arrow_pixel02.showturtle()

def setupModule1(): # set up turtle in the place ready and hidden

    global picture_box01, caption_box01

    # picture box and caption box in Food selection

    picture_box01 = turtle.Turtle()
    picture_box01.hideturtle()
    picture_box01.penup()
    picture_box01.goto(180,20) 

    caption_box01 = turtle.Turtle()
    caption_box01.hideturtle()
    caption_box01.penup()
    caption_box01.goto(220,-270) 

def setupModule1_2(): # Still in Vietnam screen, Location attribute
    
    global picture_box02, caption_box02, arrow_pixel01, arrow_pixel02

    # picture box and caption box in Location selection

    picture_box02 = turtle.Turtle()
    picture_box02.hideturtle()
    picture_box02.penup()
    picture_box02.goto(180,20)

    caption_box02 = turtle.Turtle()
    caption_box02.hideturtle()
    caption_box02.penup()
    caption_box02.goto(220,-270)

def activity01(x,y): # Food selection

    global arrow_pixel01, arrow_pixel02
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    setupModule1_2()

    picture_box02.hideturtle()
    caption_box02.hideturtle()

    setupArrow()
    setupModule1()

    arrow_pixel01.onclick(changePic01)
    arrow_pixel02.onclick(changePic02)

def changePic01(x,y): # Food attribute, picture change only

    global inc01
    global picture_box01, caption_box01
    global picture_box02, caption_box02
    global arrow_pixel01, arrow_pixel02

    if -1 <= inc01 <= 3:
        inc01 += 1

    picture_box01.shape(food_list[inc01])
    picture_box01.showturtle()

    # caption box

    caption_box01.shape(caption_list[inc01])
    caption_box01.showturtle()

    if inc01 == 4:
        inc01 = -1

def changePic02(x,y): # Food attribute, caption change only

    global inc01
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    if 1 <= inc01 <= 4:
        inc01 -= 1

    # picture box
    picture_box01.shape(food_list[inc01])
    picture_box01.showturtle()

    # caption box
    caption_box01.shape(caption_list[inc01])
    caption_box01.showturtle()

    if inc01 == -1:
        inc01 = 4

def activity02(x,y): # Location selection in module 1

    s.clear()
    module1(x,y)
    
    global arrow_pixel01, arrow_pixel02
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    setupArrow()
    setupModule1()
    picture_box01.hideturtle()
    caption_box01.hideturtle()

    setupModule1_2()

    arrow_pixel01.onclick(changePic03)
    arrow_pixel02.onclick(changePic04)

def changePic03(x,y): # Location attribute, picture change only

    global inc02
    global arrow_pixel01, arrow_pixel02
    global picture_box01, caption_box01
    global picture_box02, caption_box02
    global conclusion_box

    if -1 <= inc02 <= 3:
        inc02 += 1

    picture_box02.shape(location_list[inc02])
    picture_box02.showturtle()

    # caption box

    caption_box02.shape(location_caption_list[inc02])
    caption_box02.showturtle()

    # write conclusion box

    if inc02 == 4:
        conclusion_box = turtle.Turtle()
        conclusion_box.shape("conclusion.gif")
        conclusion_box.penup()
        conclusion_box.goto(0,0)
        conclusion_box.hideturtle()
        writeText(conclusion_box, 0, 0, "black", "Conclusion")
        conclusion_box.showturtle()
        
        conclusion_box.onclick(conclusionScreen)

def changePic04(x,y): # Location attribute, caption change only

    global inc02
    global arrow_pixel01, arrow_pixel02
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    # picture box
    picture_box02.shape(location_list[inc02])
    picture_box02.showturtle()

    # caption box
    caption_box02.shape(location_caption_list[inc02])
    caption_box02.showturtle()
        
def conclusionScreen(x,y): # after function change03 reaches the end of list

    global inc, conclusion_text_01
    inc += 1

    s.clear()
    s.bgpic(screens[inc])

    conclusion_text_box = turtle.Turtle()

    conclusion_text_box.goto(0, -80)
    conclusion_text_box.pencolor("white")
    conclusion_text_box.write(conclusion_text_01, False, align = "center", font=("Helvetica", round(FONTSIZE*2), "bold"))

# MODULE 2 STARTS FROM HERE

def module2(x,y): # Chicago option

    global inc
    inc += 1

    s.clear()
    s.bgpic(screens[inc])

    intro2 = "Explore Chi-Town :)" 
    writeIntro("white", intro2)

    # menu selection starts here

    # food box

    turtle.addshape("box2.gif") 

    selection_food = turtle.Turtle()
    selection_food.shape("box2.gif")
    selection_food.hideturtle()
    selection_food.penup()
    selection_food.goto(-500,120)
    selection_food.showturtle()

    writeText(text, -510, 100, "white", "Cuisine")

    # location box 

    selection_location = turtle.Turtle()
    selection_location.shape("box2.gif")
    selection_location.hideturtle()
    selection_location.penup()
    selection_location.goto(-500,-120)
    selection_location.showturtle()

    writeText(text, -510, -140, "white", "Activity")

    selection_food.onclick(activity03) # will run parallel with activity01
    selection_location.onclick(activity04) # will run parallel with activity02

def activity03(x,y):
    global arrow_pixel01, arrow_pixel02
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    setupModule1_2()

    picture_box02.hideturtle()
    caption_box02.hideturtle()

    setupArrow()
    setupModule1()
    
    arrow_pixel01.onclick(changePic05) # run parallel with changePic01
    arrow_pixel02.onclick(changePic06) # run parallel with changePic02

def changePic05(x,y):

    global inc03
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    if -1 <= inc03 <= 3:
        inc03 += 1

    picture_box01.shape(chicago_food_list[inc03])
    picture_box01.showturtle()

    # caption box

    caption_box01.shape(chicago_food_caption_list[inc03])
    caption_box01.showturtle()

    if inc03 == 4:
        inc03 = -1

def changePic06(x,y):

    global inc03
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    if 1 <= inc03 < 5:
        inc03 -= 1

    # picture box
    picture_box01.shape(chicago_food_list[inc03])
    picture_box01.showturtle()

    # caption box
    caption_box01.shape(chicago_food_caption_list[inc03])
    caption_box01.showturtle()

    if inc03 == -1:
        inc03 = -4

def activity04(x,y): # Activity selection in module 2

    s.clear()
    module2(x,y)

    global arrow_pixel01, arrow_pixel02
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    setupArrow()
    setupModule1()
    picture_box01.hideturtle()
    caption_box01.hideturtle()

    setupModule1_2()

    arrow_pixel01.onclick(changePic07)
    arrow_pixel02.onclick(changePic08)

def changePic07(x,y): # run in parallel with changePic03

    global inc04
    global picture_box01, caption_box01
    global picture_box02, caption_box02
    global conclusion_box

    if -1 <= inc04 <= 3:
        inc04 += 1

    picture_box02.shape(activity_list[inc04])
    picture_box02.showturtle()

    # caption box

    caption_box02.shape(activity_caption_list[inc04])
    caption_box02.showturtle()

    # write conclusion box

    if inc04 == 4:
        conclusion_box = turtle.Turtle()
        conclusion_box.shape("conclusion.gif")
        conclusion_box.penup()
        conclusion_box.goto(0,0)
        conclusion_box.hideturtle()
        writeText(conclusion_box, 0, 0, "black", "Conclusion")
        conclusion_box.showturtle()
        
        conclusion_box.onclick(conclusionScreen2)

def changePic08(x,y): # Location attribute, caption change only

    global inc04
    global picture_box01, caption_box01
    global picture_box02, caption_box02

    if 1 <= inc04 < 5:
        inc04 -= 1

    # picture box
    picture_box02.shape(activity_list[inc04])
    picture_box02.showturtle()

    # caption box
    caption_box02.shape(activity_caption_list[inc04])
    caption_box02.showturtle()

    if inc03 == -1:
        inc03 = 4
        
def conclusionScreen2(x,y): # after function change03 reaches the end of list

    global conclusion_text_02

    s.clear()

    end_inc = len(screens)-1

    s.bgpic(screens[end_inc])

    conclusion_text_box = turtle.Turtle()
    conclusion_text_box.goto(0, -80)
    conclusion_text_box.pencolor("white")
    conclusion_text_box.write(conclusion_text_02, False, align = "center", font=("Helvetica", round(FONTSIZE*2), "bold"))

if __name__ == '__main__':

    turtle.hideturtle() # hide default turtle

    screens = ["chicago_edited.gif", "white_screen.gif", "black_screen.gif", "black_screen.gif", "vn_edited.gif", "chicago_night.gif"]
    inc = 0 # variable for increasing index of screens list

    inc01 = -1 # variable for increasing index of cuisine attribute list in module 1
    inc02 = -1 # variable for increasing index of location attribute list in module 1

    inc03 = -1 # variable for increasing index of cuisine attribute list in module 2
    inc04 = -1 # variable for increasing index of location attribute list in module 2

    # VIETNAM option

    # Cuisine box: list of food and caption list, running parallel
    food_list = ["bun.gif", "goicuon.gif", "banhmi.gif", "banhxeo.gif", "miquang.gif"]  
    caption_list = ["bun_caption.gif", "goicuon_caption.gif", "banhmi_caption.gif", "banhxeo_caption.gif", "miquang_caption.gif"]
    # Location box: location list and caption list, running parallel
    location_list = ["argyle.gif", "tanknoodle.gif", "bale_sandwich.gif", "chiuquon.gif", "tainammarket.gif"]
    location_caption_list = ["argyle_caption.gif", "tanknoodle_caption.gif", "bale_caption.gif", "chiuquon_caption.gif", "tainam_caption.gif" ]

    # CHICAGO option
    # Cuisine box
    chicago_food_list = ["ramen_pixel.gif", "sushi_pixel.gif", "kbbq_pixel.gif", "taco_pixel.gif", "steak_pixel.gif"] 
    chicago_food_caption_list = ["ramen_caption.gif", "sushi_caption.gif", "kbbq_caption.gif", "taco_caption.gif", "steak_caption.gif"]
    # Activity box

    activity_list = ["museum_pixel.gif", "beach_pixel.gif", "sightsee_pixel.gif", "bookstore_pixel.gif", "ceramic_pixel.gif"]
    activity_caption_list = ["museum_caption.gif", "beach_caption.gif", "sightsee_caption.gif", "bookstore_caption.gif", "community_caption.gif"]

    for i in range(0, len(food_list), 1):
        # Vietnam option
        turtle.addshape(food_list[i])
        turtle.addshape(caption_list[i])
        turtle.addshape(location_list[i])
        turtle.addshape(location_caption_list[i])
        # Chicago option
        turtle.addshape(chicago_food_list[i])
        turtle.addshape(chicago_food_caption_list[i])
        turtle.addshape(activity_list[i])
        turtle.addshape(activity_caption_list[i])

    # set up screen
    s = turtle.getscreen()
    s.setup(800,600)
    s.bgpic(screens[0])

    # set up and call introduction text
    welcome_text = "Welcome to the Windy City!"
    writeIntro("white", welcome_text)

    # second introductory text

    description_box = turtle.Turtle()
    description_box.hideturtle()
    description_box.penup()

    word =  "Xin chào! You must be new around here :)\n\n" + "This graphic application is designed to help you get used to life in Chicago.\n\n" + "Let's take a look! Click anywhere on the screen to continue :)"

    draw_word_box(description_box, 0, 0, 886, 180, "white", word)

    text = turtle.Turtle()
    text.hideturtle()
    text.penup()

    # conclusion box, the user can move to the end screen, maybe give the option to return to main screen
    turtle.addshape("conclusion.gif")

    # read data from file for two conclusion screens

    conclusion_text_01 = ''
    conclusion_text_02 = ''

    file01 = open("conclusion01.txt")
    list01 = file01.readlines()
    for line in list01:
        new_line = line.capitalize()
        conclusion_text_01 += line.capitalize()

    file02 = open("conclusion02.txt")
    list02 = file02.readlines()
    for line in list02:
        new_line = line.capitalize()
        conclusion_text_02 += line.capitalize()
    
    # arrows set up

    turtle.addshape("arrow.gif") # arrow right
    turtle.addshape("arrow2.gif") # arrow left

    s.onclick(whiteScreen)

    s.mainloop()