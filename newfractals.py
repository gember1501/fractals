import cairo
import math as m



def triangle(lengte, x, y):
    rechts = x + lengte
    midden = x + (lengte * 0.5) 
    hoogte = y - (lengte * 0.5) 


    context.move_to(x, y)
    context.line_to(rechts, y)
    context.line_to(midden, hoogte)
    context.close_path()
    
    
def huisje(x, y, grootte, hoek, aantal):


    # ctx.rectangle(x, y, 3, 3)
    
    if hoek ==315 or aantal == 7:
        context.translate(x, y )
        context.rotate(hoek*m.pi/180)
        context.set_source_rgba(0, 0, 0, 1)
        context.rectangle(0, 0 - grootte, grootte, grootte)
        triangle(grootte, 0, 0 - grootte)

    else:
        context.translate(x, y)
        context.rotate(hoek*m.pi/180)
        context.set_source_rgba(0, 0, 0, 1)
        context.rectangle(0, 0, grootte, grootte)
        triangle(grootte, 0, 0 - grootte)


    if aantal > 0:
            grootte_nw = nieuwe_lengte(grootte)
            aantal -= 1
            huisje(0, 0-grootte, grootte_nw, 315, aantal)
            huisje(0, 0-grootte, grootte_nw, 45, aantal)
        
        
    

def nieuwe_lengte (huidige_lengte):
    # pythagoraske
    halve_lengte = huidige_lengte * 0.5    
    te_wortelen = (halve_lengte * halve_lengte) + (halve_lengte * halve_lengte)

    return m.sqrt(te_wortelen)


with cairo.SVGSurface("newfractal.svg", 700, 700) as surface:
    context = cairo.Context(surface)
    context.set_source_rgba(0, 0, 0, 1)
    huisje(400, 600, 100, 0, 7)
    context.stroke()

print("File Saved")