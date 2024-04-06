def setup():
    size(960, 960)
    background(255,255,255)
    mickey()
def mickey(x,y,c):
    no_stroke()
    fill(255,0,0)
    circle(x,y,c)
    fill(0,0,0)
    circle(x-(c/2),y-(c/2),c/2)
    circle(x+(c/2),y-(c/2),c/2)
