x0 = 100
y0 = 500
x = x0
y = y0

angle = 45.0
v0 = 60.0
g = 9.81

t = 0.0
dt = 0.15
is_launch = False

trajectory = []

def setup():
    size(1000, 600)
    textFont(createFont("SansSerif", 15))

def draw():
    global x, y, t, is_launch, trajectory
    background(240, 245, 250)

    stroke(100)
    strokeWeight(3)
    line(0, y0 + 15, width, y0 + 15)

    rad = radians(angle)
    stroke(37, 99, 235)
    strokeWeight(8)
    line(x0, y0, x0 + 45 * cos(rad), y0 - 45 * sin(rad))

    if is_launch:
        t += dt
        vx0 = v0 * cos(rad)
        vy0 = v0 * sin(rad)

        px = vx0 * t
        py = (vy0 * t) - (0.5 * g * t * t)
        
        x = x0 + px * 3.0
        y = y0 - py * 3.0

        if y <= y0 + 15:
            trajectory.append((x, y))

        if py < 0:
            is_launch = False
            y = y0

    noFill()
    stroke(239, 68, 68)
    strokeWeight(2)
    beginShape()
    for pt in trajectory:
        vertex(pt[0], pt[1])
    endShape()

    fill(239, 68, 68)
    noStroke()
    ellipse(x, y, 20, 20)

    draw_ui(rad)

def draw_ui(rad):
    vy0 = v0 * sin(rad)
    total_t = (2.0 * vy0) / g
    max_h = (vy0 * vy0) / (2.0 * g)
    max_r = (v0 * v0 * sin(2 * rad)) / g

    fill(255, 255, 255, 230)
    stroke(200)
    strokeWeight(1)
    rect(20, 20, 310, 220, 10)
    
    fill(30)
    text("--- Controls ---", 35, 45)
    text("UP / DOWN : Angle = " + str(int(angle)) + " deg", 35, 70)
    text("LEFT / RIGHT : Velocity = " + str(int(v0)) + " m/s", 35, 95)
    text("SPACEBAR : Launch / Reset", 35, 120)
    
    text("--- Real-time Calculations ---", 35, 150)
    text("Max Height (H): " + nf(max_h, 0, 2) + " m", 35, 175)
    text("Max Range (R): " + nf(max_r, 0, 2) + " m", 35, 195)
    text("Flight Time (T): " + nf(total_t, 0, 2) + " s", 35, 215)

def keyPressed():
    global angle, v0, is_launch, t, x, y, trajectory
    if keyCode == UP and angle < 90:
        angle += 5
    elif keyCode == DOWN and angle > 0:
        angle -= 5
    elif keyCode == RIGHT and v0 < 150:
        v0 += 5
    elif keyCode == LEFT and v0 > 10:
        v0 -= 5
    elif key == ' ':
        is_launch = True
        t = 0.0
        x = x0
        y = y0
        trajectory = []
