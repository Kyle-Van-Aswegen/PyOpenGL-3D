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
        ),
        #  QUESTION 5: Define surfaces for cube 
        "surfaces": (
            (0,1,2,3),
            (4,5,1,0),
            (6,7,5,4),
            (2,3,6,7),
            (1,2,7,5),
            (0,3,6,4)
        )
    },
    "pyramid": {
        "vertices": (
            (1, -1, 1), (-1, -1, 1), (0, -1, -1), (0, 1, 0)
        ),
        "edges": (
            (0,1), (0,2), (0,3), (2,1), (2,3), (3,1)
        ),
        #  QUESTION 5: Define surfaces for pyramid 
        "surfaces": (
            (0, 1, 2),
            (0, 1, 3),
            (1, 2, 3),
            (2, 0, 3)
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
        ),
        #  QUESTION 5: Define surfaces for prism 
        "surfaces": (
            (0,1,2),
            (3,4,5),
            (0,1,4,3),
            (1,2,5,4),
            (2,0,3,5)
        )
    }
}

#  STATE TRACKING 
model_keys = list(models.keys())
current_model_index = 0
translation = [0.0, 0.0, -5.0]
rotation = [0.0, 0.0, 0.0]
scaling = [1.0, 1.0, 1.0]

#  QUESTION 5: FACE COLORS 
face_colors = [
    (1, 0, 0),  # red
    (0, 1, 0),  # green
    (0, 0, 1),  # blue
    (1, 1, 0),  # yellow
    (1, 0, 1),  # magenta
    (0, 1, 1),  # cyan
]

def draw_faces():
    model = models[model_keys[current_model_index]]
    vertices = model["vertices"]
    if "surfaces" not in model:
        return

    glBegin(GL_QUADS if len(model["surfaces"][0]) == 4 else GL_TRIANGLES)
    for i, surface in enumerate(model["surfaces"]):
        color = face_colors[i % len(face_colors)]
        glColor3f(*color)  # Apply face color
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_edges():
    model = models[model_keys[current_model_index]]
    vertices = model["vertices"]
    edges = model["edges"]

    glColor3f(1, 1, 1)  # White edges
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(*translation)
    glRotatef(rotation[0], 1, 0, 0)
    glRotatef(rotation[1], 0, 1, 0)
    glRotatef(rotation[2], 0, 0, 1)
    glScalef(*scaling)

    draw_faces()  # Colored faces
    draw_edges()  # White wireframe
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (w/h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global current_model_index, translation, rotation, scaling

    if key == b'n':
        current_model_index = (current_model_index + 1) % len(model_keys)
    elif key == b'\x1b':
        sys.exit()

    # Translation
    elif key == b'w': translation[1] += 0.2
    elif key == b's': translation[1] -= 0.2
    elif key == b'd': translation[0] += 0.2
    elif key == b'a': translation[0] -= 0.2
    elif key == b'e': translation[2] += 0.2
    elif key == b'q': translation[2] -= 0.2

    # Rotation
    elif key == b'i': rotation[0] += 5.0
    elif key == b'k': rotation[0] -= 5.0
    elif key == b'j': rotation[1] += 5.0
    elif key == b'l': rotation[1] -= 5.0
    elif key == b'u': rotation[2] += 5.0
    elif key == b'o': rotation[2] -= 5.0

    # Scaling
    elif key == b'z': scaling[0] += 0.1
    elif key == b'x': scaling[0] = max(0.1, scaling[0] - 0.1)
    elif key == b'c': scaling[1] += 0.1
    elif key == b'v': scaling[1] = max(0.1, scaling[1] - 0.1)
    elif key == b'b': scaling[2] += 0.1
    elif key == b'n': scaling[2] = max(0.1, scaling[2] - 0.1)

    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Model Viewer with Colour (Q5)")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
