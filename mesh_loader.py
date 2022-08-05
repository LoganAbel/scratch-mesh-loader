import numpy as np
from trimesh import load as trimesh_load

indices = [1]
while 1:
	inp = input('in: ')
	if not inp:
		break
	mesh = trimesh_load(inp)
	mesh.vertices -= mesh.center_mass
	mesh.vertices /= np.amax(mesh.extents)

	data = mesh.vertices[mesh.faces].flatten().tolist()

	with open("meshes.csv", "a") as f:
		np.savetxt(f, data, delimiter="\n")

	indices += [indices[-1] + len(data)]

np.savetxt("mesh_starts.csv", indices, delimiter="\n")

input('done')