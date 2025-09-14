from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
width, height = 800, 600


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


model_keys = list(models.keys())
current_model_index = 0
translation = [0.0, 0.0, -5.0]  # x, y, z

# DRAWING FUNCTION
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
    glTranslatef(*translation)  
    glColor3f(1.0, 1.0, 1.0)
    draw_model()
    glutSwapBuffers()

# RESHAPE CALLBACK
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (w/h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# KEYBOARD CONTROLS (Question 2 additions) 
def keyboard(key, x, y):
    global current_model_index, translation
    # Switch model
    if key == b'n':
        current_model_index = (current_model_index + 1) % len(model_keys)
        glutPostRedisplay()
    # Exit
    elif key == b'\x1b':  # ESC
        sys.exit()

    # QUESTION 2: TRANSLATION CONTROLS 
    elif key == b'w':  # Move up (Y+)
        translation[1] += 0.2
    elif key == b's':  # Move down (Y-)
        translation[1] -= 0.2
    elif key == b'd':  # Move right (X+)
        translation[0] += 0.2
    elif key == b'a':  # Move left (X-)
        translation[0] -= 0.2
    elif key == b'e':  # Move forward (Z+)
        translation[2] += 0.2
    elif key == b'q':  # Move back (Z-)
        translation[2] -= 0.2

    glutPostRedisplay()

# MAIN FUNCTION 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Model Viewer with Translation (Q2)")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
