import cairo 


def huisje(ctx, x, y, grootte):

    ctx.rectangle(x, y, grootte, grootte)

with cairo.SVGSurface("newfractal.svg", 700, 700) as surface:
    context = cairo.Context(surface)
    context.set_source_rgba(0, 0, 0, 1)
    huisje(context, 300, 300, 100)
    context.stroke()

print("File Saved")