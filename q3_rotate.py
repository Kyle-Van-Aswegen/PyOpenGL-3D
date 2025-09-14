from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

#  WINDOW 
width, height = 800, 600

# MODEL DATA 
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

#  STATE 
model_keys = list(models.keys())
current_model_index = 0

# Translation and Rotation States
translation = [0.0, 0.0, -5.0]
rotation = [0.0, 0.0, 0.0]  # x, y, z

# DRAW FUNCTION 
def draw_model():
    model = models[model_keys[current_model_index]]
    vertices = model["vertices"]
    edges = model["edges"]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# DISPLAY CALLBACK 
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Apply translation
    glTranslatef(*translation)

    #  QUESTION 3: APPLY ROTATION 
    glRotatef(rotation[0], 1, 0, 0)  # X-axis
    glRotatef(rotation[1], 0, 1, 0)  # Y-axis
    glRotatef(rotation[2], 0, 0, 1)  # Z-axis

    glColor3f(1.0, 1.0, 1.0)
    draw_model()
    glutSwapBuffers()

# === RESHAPE CALLBACK ===
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (w/h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# KEYBOARD HANDLING (Includes Q2 + Q3)
def keyboard(key, x, y):
    global current_model_index, translation, rotation

    # Model switching
    if key == b'n':
        current_model_index = (current_model_index + 1) % len(model_keys)
    elif key == b'\x1b':  # Esc to exit
        sys.exit()

    # QUESTION 2: TRANSLATION CONTROLS 
    elif key == b'w': translation[1] += 0.2  # +Y
    elif key == b's': translation[1] -= 0.2  # -Y
    elif key == b'd': translation[0] += 0.2  # +X
    elif key == b'a': translation[0] -= 0.2  # -X
    elif key == b'e': translation[2] += 0.2  # +Z
    elif key == b'q': translation[2] -= 0.2  # -Z

    #  QUESTION 3: ROTATION CONTROLS 
    elif key == b'i': rotation[0] += 5.0  # Rotate +X
    elif key == b'k': rotation[0] -= 5.0  # Rotate -X
    elif key == b'j': rotation[1] += 5.0  # Rotate +Y
    elif key == b'l': rotation[1] -= 5.0  # Rotate -Y
    elif key == b'u': rotation[2] += 5.0  # Rotate +Z
    elif key == b'o': rotation[2] -= 5.0  # Rotate -Z

    glutPostRedisplay()

#  MAIN FUNCTION 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Model Viewer with Rotation (Q3)")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
