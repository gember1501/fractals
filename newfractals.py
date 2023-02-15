import cairo 

def huisje(x, y, grootte):

    context.rectangle(x, y, grootte, grootte)

with cairo.SVGSurface("fractal.svg", 700, 700) as surface:
    context = cairo.Context(surface)
huisje(100, 100, 100)

print("File Saved")