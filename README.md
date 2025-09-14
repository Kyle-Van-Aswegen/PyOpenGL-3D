3D Model Viewer – PyOpenGL 



Overview

This project is a simple 3D model viewer built using Python and PyOpenGL. It focuses on practicing 3D transformations such as translation, rotation, scaling, and applying basic coloring to models. The models used include a cube, a pyramid, and a triangular prism. The program is controlled entirely through the keyboard.

Each question in the assignment adds a new transformation or feature. The final version (`q5_colour.py`) includes all the functionality implemented across the five questions.

Running the Program

Make sure Python is installed (Python 3.10–3.13 recommended).

To install the required libraries, run:

    pip install PyOpenGL PyOpenGL_accelerate

To run the final version of the application:

    python q5_colour.py

Files Included

- `q1_display.py`   – Displays models and allows switching
- `q2_translate.py` – Adds movement (translation)
- `q3_rotate.py`    – Adds rotation on all axes
- `q4_scale.py`     – Adds non-uniform scaling
- `q5_colour.py`    – Final version with colored faces
- `README.txt`      – Instructions and feature list

Keyboard Controls

Model Switching:
- `N` → Switch to next model

Translation:
- `W` / `S` → Move Up / Down (Y axis)
- `A` / `D` → Move Left / Right (X axis)
- `Q` / `E` → Move Backward / Forward (Z axis)

Rotation:
- `I` / `K` → Rotate Up / Down (X axis)
- `J` / `L` → Rotate Left / Right (Y axis)
- `U` / `O` → Rotate Clockwise / Counterclockwise (Z axis)

Scaling:
- `Z` / `X` → Stretch / Squeeze X axis
- `C` / `V` → Stretch / Squeeze Y axis
- `B` / `N` → Stretch / Squeeze Z axis

Feature Summary

Question 1: Display & Model Switching
- Three models available (cube, pyramid, prism)
- Press `N` to cycle between them

Question 2: Translation
- Models can be moved on all 3 axes
- Translations are retained when switching models

Question 3: Rotation
- Models rotate around their local X, Y, and Z axes
- Rotation state is preserved across model switches

Question 4: Scaling
- Models can be stretched or squashed along each axis independently
- Scaling remains intact when switching models

Question 5: Colouring
- Each face of the model has a solid color (no transparency)
- Edges remain white for clarity
- Face colors do not affect position, orientation, or size

Notes

- There is no dedicated exit key; just close the window normally
- All transformations are preserved as you switch between models
- Coloring uses `GL_QUADS` and `GL_TRIANGLES`, with basic RGB values

