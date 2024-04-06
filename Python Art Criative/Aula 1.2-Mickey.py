#Des

def setup():
    size(960, 960)
    mickey()
def mickey(x,y,c):
    no_stroke()
    circle(x,y,c)
    circle(x-(c/2),y-(c/2),c/2)
    circle(x+(c/2),y-(c/2),c/2)
