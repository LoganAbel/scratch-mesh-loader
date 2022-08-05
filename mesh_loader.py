import numpy as np
import trimesh

indices = [1]
with open("meshes.csv", "w") as f:
	pass

while 1:
	inp = input('in: ')
	if not inp:
		break
	mesh = trimesh.load(inp)
	center, radius = trimesh.nsphere.minimum_nsphere(mesh.vertices)
	mesh.vertices -= center
	mesh.vertices /= radius

	data = mesh.vertices[mesh.faces].flatten().tolist()

	with open("meshes.csv", "a") as f:
		np.savetxt(f, data, delimiter="\n")

	indices += [indices[-1] + len(data)]

np.savetxt("mesh_starts.csv", indices, delimiter="\n")

input('done')
