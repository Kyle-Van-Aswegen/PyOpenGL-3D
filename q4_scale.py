from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

#  WINDOW SETTINGS
width, height = 800, 600

#  MODEL DATA
models = {
    "cube": {
        "vertices": (
            (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
            (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
        ),
        "edges": (
            (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
            (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
        )
    },
    "pyramid": {
        "vertices": (
            (1, -1, 1), (-1, -1, 1), (0, -1, -1), (1, 1, 0.5)
        ),
        "edges": (
            (0,1), (0,2), (0,3), (2,1), (2,3), (3,1)
        )
    },
    "prism": {
        "vertices": (
            (-1, -1, 1), (1, -1, 1), (0, 1, 1),
            (-1, -1, -1), (1, -1, -1), (0, 1, -1)
        ),
        "edges": (
            (0,1), (0,2), (1,2), (3,4), (3,5), (4,5),
            (0,3), (1,4), (2,5)
        )
    }
}

#  STATE TRACKING 
model_keys = list(models.keys())
current_model_index = 0

translation = [0.0, 0.0, -5.0]
rotation = [0.0, 0.0, 0.0]
scaling = [1.0, 1.0, 1.0]  # X, Y, Z scaling factors

#  DRAW FUNCTION 
def draw_model():
    model = models[model_keys[current_model_index]]
    vertices = model["vertices"]
    edges = model["edges"]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

#  DISPLAY CALLBACK 
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Apply transformations
    glTranslatef(*translation)
    glRotatef(rotation[0], 1, 0, 0)
    glRotatef(rotation[1], 0, 1, 0)
    glRotatef(rotation[2], 0, 0, 1)
    glScalef(*scaling)  # QUESTION 4: Apply scaling

    glColor3f(1.0, 1.0, 1.0)
    draw_model()
    glutSwapBuffers()

#  RESHAPE CALLBACK 
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (w/h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# KEYBOARD INPUT 
def keyboard(key, x, y):
    global current_model_index, translation, rotation, scaling

    # Model cycling
    if key == b'n':
        current_model_index = (current_model_index + 1) % len(model_keys)
    elif key == b'\x1b':
        sys.exit()

    # Translation (Question 2)
    elif key == b'w': translation[1] += 0.2
    elif key == b's': translation[1] -= 0.2
    elif key == b'd': translation[0] += 0.2
    elif key == b'a': translation[0] -= 0.2
    elif key == b'e': translation[2] += 0.2
    elif key == b'q': translation[2] -= 0.2

    # Rotation (Question 3)
    elif key == b'i': rotation[0] += 5.0
    elif key == b'k': rotation[0] -= 5.0
    elif key == b'j': rotation[1] += 5.0
    elif key == b'l': rotation[1] -= 5.0
    elif key == b'u': rotation[2] += 5.0
    elif key == b'o': rotation[2] -= 5.0

    #  SCALING CONTROLS (Question 4) 
    elif key == b'z': scaling[0] += 0.1  # Scale X+
    elif key == b'x': scaling[0] = max(0.1, scaling[0] - 0.1)  # Scale X-
    elif key == b'c': scaling[1] += 0.1  # Scale Y+
    elif key == b'v': scaling[1] = max(0.1, scaling[1] - 0.1)  # Scale Y-
    elif key == b'b': scaling[2] += 0.1  # Scale Z+
    elif key == b'n': scaling[2] = max(0.1, scaling[2] - 0.1)  # Scale Z-

    glutPostRedisplay()

# MAIN FUNCTION 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Model Viewer with Scaling (Q4)")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
