from PIL import Image, ImageDraw
import math
import random
import time

WHITE = (255, 255, 255)

def magnitude(x, y):
    return math.sqrt(x*x + y*y)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def cartesian(x, y, size):
    # take (x, y) points and turn them into cartesian points
    return (int(x + size[0] / 2), int(y + size[1] / 2))

def add_points(a, b):
    return (a[0] + b[0], a[1] + b[1])

def quad(a, b, width, theta):
    add = (width * math.cos(theta), width * math.sin(theta))
    a1 = add_points(a, add) 
    b1 = add_points(b, add)
    return [a, a1, b, b1]

def generate_spiral(image, A, B, color, width, spiral_type):
    draw = ImageDraw.Draw(image)

    size = image.size
    length = magnitude(size[0], size[1]) 
    theta = 0.0
    step = 0.2
    prev_position = None 

    while 1:
        if spiral_type == "log":
            r = 1 + A * math.exp(theta * B) 
        else:
            r = A + B * theta 
        x = int(r * math.cos(theta))
        y = int(r * math.sin(theta))
        scale = magnitude(x, y) / length 
        position = cartesian(x, y, size)
        if prev_position == None:
            prev_position = position

        if position[0] >= size[0] or position[1] >= size[1]:
            break

        # for rougher spiral, add random.randint(-3, 3) to width
        rectangle = quad(prev_position, position, width * scale, theta)
        draw.polygon(rectangle, outline=color)
        prev_position = position
        theta += step / r

if __name__ == "__main__":
    for i in range(19000):
        ink = random_color() 
        spiral = Image.new("RGB", (128, 128), ink) 
        generate_spiral(
                image = spiral,
                A = random.random() * 2,
                B = random.random() * 0.5,
                color = random_color(),
                width = random.random() * 50 + 10, 
                spiral_type = "log",
        )
        filename = "spirals/" + str(int(time.time()*1000)) + ".png"
        spiral.save(filename)
        print(filename)
