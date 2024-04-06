#Des

def setup():
    size(960, 960)
    no_stroke()
    mickey()
def mickey(x,y,c):
    circle(x,y,c)
    circle(x-(c/2),y-(c/2),c/2)
    circle(x+(c/2),y-(c/2),c/2)
