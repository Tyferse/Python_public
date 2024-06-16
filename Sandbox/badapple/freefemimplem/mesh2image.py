import gmsh
import matplotlib.pyplot as plt
import numpy as np


gmsh.initialize()
gmsh.open("meshframes/output_0105.mesh")
nodeTags, nodeCoords, _ = gmsh.model.mesh.getNodes()
elementTypes, elementTags, elementNodeTags = gmsh.model.mesh.getElements()

# Отображение сетки в matplotlib
plt.figure()
for elementType, elementTag, elementNodeTag in zip(elementTypes, elementTags, elementNodeTags):
    # Check if the element type is for triangles
    if elementType == 2:  # Triangle element type in Gmsh
        elementNodes = [nodeCoords[int(node) - 1] for node in elementNodeTag]  # Ensure node is converted to an integer
        elementNodes.extend(elementNodes[:2])  # Closing loop by adding the first point at the end
        elementNodes = np.array(elementNodes)  # Convert to numpy array for easier manipulation
        # print('\n\n', elementNodes[:9], end='\n\n')
        i = x/nx + nx * y/ny
        x, y = elementNodes[::2], elementNodes[1::2]  # Separate the x and y coordinates
        plt.plot(x, y)  # Plotting triangles

plt.axis('equal')  # Equal scaling of axes
# plt.gca().set_aspect('equal', adjustable='box')  # Aspect ratio of the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualization of mesh from Gmsh in matplotlib')
plt.show()

# Выход из gmsh
gmsh.finalize()
