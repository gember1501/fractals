import turtle as t
import math as m

t.shape()


t.speed(0)
t.color('#004c4c')
t.hideturtle()
t. pensize(1)

def nieuwe_lengte (huidige_lengte):
    # pythagoraske
    halve_lengte = huidige_lengte * 0.5    
    te_wortelen = (halve_lengte * halve_lengte) + (halve_lengte * halve_lengte)

    return m.sqrt(te_wortelen)






def huisje(lengte, aantal, richting):

        #kleur

    if aantal == 14:
       t.pencolor('#006666')
    
    if aantal == 11:
        t.pencolor('#008080')
    
    if aantal == 7:
        t.pencolor('#66b2b2')
    if aantal == 5:
        t.pencolor('#b2d8d8')
    
    # huisje
    t.setheading(richting)
    t.pendown()
    t. forward(lengte)
    derechterdakgoot=(t.xcor(), t.ycor())

    t.left(45)
    t. forward(nieuwe_lengte(lengte))
    t.left(90)
    denok=(t.xcor(), t.ycor())
    t. forward(nieuwe_lengte(lengte))
    t.left(45)
    t. forward(lengte)
    t.left(90)


   
    
    # opnieuw positioneren op de nok
    t. penup()
    t.goto(denok)
    t. pendown()
    if aantal > 0:
       
        # huisje maken
        huisje(nieuwe_lengte(lengte), aantal - 1, richting + 45)
        
        t.penup()
        t.goto(derechterdakgoot)
        
        t.pendown()
        huisje(nieuwe_lengte(lengte), aantal - 1, richting - 45)
        

    else:
        return(denok)



t.penup()
t. goto(100, -400)
t. pendown()
t. right(180)
t. forward(200)
t. right(180)
t. forward(200)
t.setheading(90)
huisje(200, 15, 90)


t.mainloop()
