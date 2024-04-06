def setup():
    size(960, 960)
    olho()
def olho(x,y,c):
    ellipse(x,y,2*c,c)
    circle(x,y,c)
    circle(x,y,c/4)
