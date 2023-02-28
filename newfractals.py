import cairo
import math as m



def triangle(ctx, lengte, x, y):
    rechts = x + lengte
    midden = x + (lengte * 0.5) 
    hoogte = y - (lengte * 0.5) 


    ctx.move_to(x, y)
    ctx.line_to(rechts, y)
    ctx.line_to(midden, hoogte)
    ctx.close_path()
    
    
def huisje(ctx, x, y, grootte, hoek, aantal):


    # ctx.rectangle(x, y, 3, 3)
    
    if hoek == 315:
        ctx.translate(x, y )
        ctx.rotate(hoek*m.pi/180)
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.rectangle(0, 0 - grootte, grootte, grootte)
        triangle(ctx, grootte, 0, 0 - grootte)

    else:
        ctx.translate(x, y)
        ctx.translate(hoek*m.pi/180)
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.rectangle(0, 0, grootte, grootte)


    if aantal > 0:
            grootte_nw = nieuwe_lengte(grootte)
            aantal_nw = aantal - 1
            huisje(ctx, 0, 0-grootte, grootte_nw, 315, aantal_nw)
            #huisje(ctx, 0, 0-grootte, grootte_nw, 45, aantal_nw)
        
        
    

def nieuwe_lengte (huidige_lengte):
    # pythagoraske
    halve_lengte = huidige_lengte * 0.5    
    te_wortelen = (halve_lengte * halve_lengte) + (halve_lengte * halve_lengte)

    return m.sqrt(te_wortelen)


with cairo.SVGSurface("newfractal.svg", 700, 700) as surface:
    context = cairo.Context(surface)
    context.set_source_rgba(0, 0, 0, 1)
    huisje(context, 450, 400, 100, 0, 5)
    context.stroke()

print("File Saved")