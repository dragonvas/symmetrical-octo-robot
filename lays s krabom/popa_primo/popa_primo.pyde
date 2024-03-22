b=0
def setup():
    size(1400, 1400)
def draw():
    global b
    for b in range(100000):
        rect(1,100,33,33)
        rect(1,200,33,33)
        rect(1,300,33,33)
        rect(1,400,33,33)
        rect(1,500,33,33)
        rect(1,600,33,33)
        rect(1,700,33,33)
        rect(1,800,33,33)
        rect(1,900,33,33)
        rect(1,1000,33,33)
        rect(1,1100,33,33)
        rect(1,1200,33,33)
        translate(b,0)
