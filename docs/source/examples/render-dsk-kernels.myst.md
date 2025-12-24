---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Rendering 3D Shape Models

This example shows how to visualize asteroid and comet shape models using DSK (Digital Shape Kernel) data from NAIF.

## Converting DSK to OBJ

Shape kernels from [NAIF](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/) are in `.bds` format. Use the `dskexp` utility to convert [run it in the terminal] - sample file: ROS_ST_K020_OSPCLAM_U_V1.bds:

```bash
# Install dskexp
./setup_dskexp.sh

# Convert to OBJ
**Command:**
dskexp -dsk <your_bds_file> -text <your_obj_file> -format obj -prec 10

**Example:**
dskexp -dsk ROS_ST_K020_OSPCLAM_U_V1.bds -text ROS_ST_K020_OSPCLAM_U_V1.obj -format obj -prec 10
```

## Example script

```{code-cell} ipython3

"""
Example of rendering a 3D model using the render module.

Author: Rahul R. Sah, Furman University
"""

from vispy import app
from boinor.render import MainWindow, load_data

# Path to your Phobos OBJ file
obj_path = "ROS_ST_K020_OSPCLAM_U_V1.OBJ"

# Load the mesh data (vertices and faces)
vertices, faces = load_data(obj_path)

# # Create the rendering window
window = MainWindow()

window.set_model(vertices, faces)

# Run the event loop to display the window
app.run()

```

![Phobos model](stein.png)

## Customizing the view

```{code-cell} ipython3

window = MainWindow(camera="arcball", fov=45, bgcolor="navy")
window.set_model(vertices, faces, shading="flat", color="grey")
app.run()
```

## References
- [NAIF Generic Kernels](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/)
- [SPICE](https://spiceypy.readthedocs.io/_/downloads/en/stable/pdf/)
- [Vispy](https://vispy.org/)
