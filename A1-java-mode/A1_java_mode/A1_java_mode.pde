float x0 = 100;
float y0 = 500;
float x = x0;
float y = y0;

float angle = 45.0;
float v0 = 60.0;
float g = 9.81;

float t = 0.0;
float dt = 0.15;
boolean is_launch = false;

ArrayList<PVector> trajectory = new ArrayList<PVector>();

void setup() {
    size(1000, 600);
    textFont(createFont("SansSerif", 15));
}

void draw() {
    background(240, 245, 250);

    stroke(100);
    strokeWeight(3);
    line(0, y0 + 15, width, y0 + 15);

    float rad = radians(angle);
    stroke(37, 99, 235);
    strokeWeight(8);
    line(x0, y0, x0 + 45 * cos(rad), y0 - 45 * sin(rad));

    if (is_launch) {
        t += dt;
        float vx0 = v0 * cos(rad);
        float vy0 = v0 * sin(rad);

        float px = vx0 * t;
        float py = (vy0 * t) - (0.5 * g * t * t);
        
        x = x0 + px * 3.0;
        y = y0 - py * 3.0;

        if (y <= y0 + 15) {
            trajectory.add(new PVector(x, y));
        }

        if (py < 0) {
            is_launch = false;
            y = y0;
        }
    }

    noFill();
    stroke(239, 68, 68);
    strokeWeight(2);
    beginShape();
    for (PVector pt : trajectory) {
        vertex(pt.x, pt.y);
    }
    endShape();

    fill(239, 68, 68);
    noStroke();
    ellipse(x, y, 20, 20);

    draw_ui(rad);
}

void draw_ui(float rad) {
    float vy0 = v0 * sin(rad);
    float total_t = (2.0 * vy0) / g;
    float max_h = (vy0 * vy0) / (2.0 * g);
    float max_r = (v0 * v0 * sin(2 * rad)) / g;

    fill(255, 255, 255, 230);
    stroke(200);
    strokeWeight(1);
    rect(20, 20, 310, 220, 10);
    
    fill(30);
    text("--- Controls ---", 35, 45);
    text("UP / DOWN : Angle = " + int(angle) + " deg", 35, 70);
    text("LEFT / RIGHT : Velocity = " + int(v0) + " m/s", 35, 95);
    text("SPACEBAR : Launch / Reset", 35, 120);
    
    text("--- Real-time Calculations ---", 35, 150);
    text("Max Height (H): " + nf(max_h, 0, 2) + " m", 35, 175);
    text("Max Range (R): " + nf(max_r, 0, 2) + " m", 35, 195);
    text("Flight Time (T): " + nf(total_t, 0, 2) + " s", 35, 215);
}

void keyPressed() {
    if (keyCode == UP && angle < 90) {
        angle += 5;
    } else if (keyCode == DOWN && angle > 0) {
        angle -= 5;
    } else if (keyCode == RIGHT && v0 < 150) {
        v0 += 5;
    } else if (keyCode == LEFT && v0 > 10) {
        v0 -= 5;
    } else if (key == ' ') {
        is_launch = true;
        t = 0.0;
        x = x0;
        y = y0;
        trajectory.clear();
    }
}
