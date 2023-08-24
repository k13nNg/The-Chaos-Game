import turtle
import random
import numpy as np

# CONSTANTS

# Vertices
A = np.array((0, 300))
B = np.array((-300, -100))
C = np.array((300, -100))


# hide turtle
turtle.hideturtle()
# set speed of turtle to max
turtle.speed(10)
turtle.title("The Chaos Game")
turtle.penup()

# generate_random_points(p_A, p_B, p_C) generates a random point inside a triangle that
# is created by the 3 points: p_A, p_B, p_C
# generate_random_points: (tuple) (tuple) (tuple) => (tuple)

def generate_random_points(p_A, p_B, p_C):
    # create 2 vectors that span 2 sides of the "imaginary" parallelogram
    # that "contains" 2 triangles
    vec_u = p_A - p_B
    vec_v = p_C - p_B
        
    # generate scalars
    u_1 = random.uniform(0, 1)
    u_2 = random.uniform(0, 1)

    # logic check for reflections (if needed)
    if (u_1 + u_2 > 1):
        u_1 = 1 - u_1
        u_2 = 1 - u_2
    
    # form vector for the new random point
    w = (u_1 * vec_u + u_2 * vec_v) + p_B

    return w

# draw_triangle(p_A, p_B, p_C) draws a triangle from 3 points: p_A, p_B, p_C
# draw_triangle: (tuple) (tuple) (tuple) => None
def draw_triangle(p_A, p_B, p_C):
    turtle.penup()
    turtle.goto(p_A)
    turtle.pendown()
    turtle.goto(p_B)
    turtle.goto(p_C)
    turtle.goto(p_A)
    turtle.penup()

# draw the triangle between 3 points: A, B and C
# draw_triangle(A, B, C)

# generate the first random point for starting
midpoint = generate_random_points(A, B, C)
    
# generates 100000 points (might be repeated)
for i in range(100000):
    print("i: ", i)
    
    # choose a random vertex
    random_vertex = random.choice([A, B, C])

    # redefine the midpoint 
    midpoint = (midpoint + random_vertex) / 2

    # draw the midpoint
    turtle.goto(midpoint)
    turtle.dot()

turtle.done()
