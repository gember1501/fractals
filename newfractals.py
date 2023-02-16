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
    
    
def huisje(ctx, x, y, grootte):


    ctx.rectangle(x, y, grootte, grootte)
    triangle(ctx, grootte, x, y)
    
    

with cairo.SVGSurface("newfractal.svg", 700, 700) as surface:
    context = cairo.Context(surface)
    context.set_source_rgba(0, 0, 0, 1)
    huisje(context, 600, 400, 100)
    context.stroke()

print("File Saved")