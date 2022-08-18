from turtle import *
import turtle as tur

screen = tur.Screen()
 
def draw(rad):
  
    for i in range(2):
        tur.circle(rad,90)
        tur.circle(rad//2,90)

screen.setup(500,500)

screen.bgcolor('black')

col=['violet','blue','green','yellow',
     'orange','red']
 
val=10
ind=0

tur.speed(100)

for i in range(36):
    
    tur.seth(-val)
    tur.color(col[ind])
     
    if ind==5:
        ind=0
    else:
        ind+=1
     
    draw(80)
    
    val+=10
 
tur.hideturtle()
tur.done()