#include "open3d/Open3D.h"
#include <iostream>
#include <fstream>
using namespace open3d;
int main(int argc, char *argv[] ) {
// Read triangle mesh "test_mesh.ply"
geometry::TriangleMesh mesh;
auto mesh1 = io::CreateMeshFromFile(argv[1]);
mesh = *mesh1;

auto connected_components = mesh.IdenticallyColoredConnectedComponents(); // Then get connected components


std::ofstream output_file("../../../examples/test_data/results.txt"); //create output filestream to output results
bool check = output_file.is_open();
if(!check){
	std::cerr<<"File wasn't created \n";
	return -1;
}


// Print and write to file connected_components in the specified format
for(auto ConComp:connected_components ){
	
	for(auto ConCompVertex:ConComp){
		
		std::cout<< ConCompVertex << " ";
		output_file << ConCompVertex << " ";
	}
std::cout<< "\n";
output_file << "\n";
}

output_file.close(); //close the file stream
return 0;
}