#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spotColor = "pink"
spotShape = "circle"
spotSize = 2
score = 0
font_setup = ("Arial", 20, "normal")
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.goto(-250,250)
#-----game functions--------
def spot_clicked(x,y):
  change_position()
  update_score()
  
def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()

def update_score():
  global score
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write(score, font=font_setup)
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()