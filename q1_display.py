from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
width, height = 800, 600

# Define model data
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

# Model state
model_keys = list(models.keys())
current_model_index = 0

def draw_model():
    model = models[model_keys[current_model_index]]
    vertices = model["vertices"]
    edges = model["edges"]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)
    glColor3f(1.0, 1.0, 1.0)
    draw_model()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (w/h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global current_model_index
    if key == b'n':  # Press 'n' to switch to next model
        current_model_index = (current_model_index + 1) % len(model_keys)
        glutPostRedisplay()
    elif key == b'\x1b':  # Escape key
        sys.exit()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Model Viewer - Press 'n' to switch models")  
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
