# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/python/Basic/solution.py

import numpy as np
import open3d as o3d



if __name__ == "__main__":
    # Read a TriangleMesh from File
    mesh = o3d.io.read_triangle_mesh("../../test_data/test_mesh.ply")
    #Getting connected components
    connected_components = mesh.identically_colored_connected_components()
    #print the connected components
    for connected_component in connected_components:
        for connected_component_vertex in connected_component:
            print(connected_component_vertex, end =" ")
        print()


          