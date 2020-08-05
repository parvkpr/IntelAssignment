# IntelAssignment
## File placement
The file structure has been maintained to the original Open3D library. Please place the respective files in the same locations in your open3D installation folders

## Build and running

* Do a regular Open3D install but with BuildTest set to ON in CMakeLists.txt
* after building the binary for solution.cpp will be placed in build/bin/examples execute the binary providing the test_mesh.ply file location as an argument
* execute python solution.py located in examples/python/Basic/
* to check c++ colored component test, execute the binary created for TriangleMesh test 
* to check python colored component test, execute pytest test_trianglemesh_col_con_comp.py

The example given in assignment file has been used for unit tests

## Task check
* Task 1: edits made in cpp/open3d/geometry/TriangleMesh.cpp and cpp/open3d/geometry/TriangleMesh.h
* Task 2: edits made in cpp/pybind/geometry/TriangleMesh.cpp
* Task 3: file added to assignment/examples/cpp/solution.cpp
* Task 4: file added to assignment/examples/python/Basic/solution.py
* Task 5: C++ example writes the txt file to test_data folder. Use sudo while running the binary in case file stream error occurs
* Task 6: Unit tests written in cpp/tests/geometry/TriangleMesh.cpp and python/tests/test_trianglemesh_col_con_comp.py
* Task 7: algorithm explained below

## Algorithm
* initialise visited array of size=vertices 
* compute adjacency list of the mesh
* for each vertice do
    * if vertex has not been visited:
      * push vertex to connected_components_sublist
      * set visited of this vertex as connected_component index in connected_components
      * if color of adjacent vertices is same then add the vertex to component and set visited of this vertex as connected_component index in connected components
    * sort the component added to maintain ascending order of vertex
    * else
      * add all non visited same colored adjacent vertices to the connected component associated with this vertex
      * set visited of added vertices to the index of associated connected component
      * sort to maintain ascending order
    
