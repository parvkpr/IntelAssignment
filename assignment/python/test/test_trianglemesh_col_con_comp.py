import open3d as o3d
import numpy as np
import time
import pytest
import os
from open3d_test import test_data_dir



def test_identically_colored_connected_components():
	output = [[0, 3, 5, 6], [1, 4], [2]]
	
	vertices = [[1, 1, 1], 
				[1, 0, 1],
				[0, 0, 1],
				[1, 0, 1],
				[1, 0, 1],
				[0, 0, 1],
				[0, 0, 1]]

	triangles = [[0, 2, 3], 
			     [0, 3, 1],
				 [1, 3, 4],
				 [2, 5, 3],
				 [3, 5, 6],
				 [3, 6, 4]]
	mesh = o3d.geometry.TriangleMesh(o3d.utility.Vector3dVector(vertices), o3d.utility.Vector3iVector(triangles))
	mesh.vertex_colors = o3d.utility.Vector3dVector([[1, 0, 0], 
                                                     [0, 1, 0], 
                                                     [0, 0, 1],
                                                     [1, 0, 0],
                                                     [0, 1, 0],
                                                     [1, 0, 0],
                                                     [1, 0, 0]])
	
	
	connected_components = mesh.identically_colored_connected_components()
	
	for con, out in zip(connected_components, output):
		for con_val, out_val in zip(con, out):
			np.testing.assert_equal(con_val, out_val)

	

