import cairo 
with cairo.SVGSurface("fractal.svg", 700, 700) as surface:
    context = cairo.Context(surface)


print("File Saved")