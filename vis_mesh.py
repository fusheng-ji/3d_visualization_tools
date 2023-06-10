import polyscope as ps
import numpy as np
import open3d as o3d


ps.init()
ps.set_ground_plane_mode("none") 
ps.set_up_dir("z_up")

def load_obj(obj_path):
    mesh = o3d.io.read_triangle_mesh(obj_path)
    vertex = np.array(mesh.vertices)
    faces = np.array(mesh.triangles)
    return vertex, faces



def main():
        obj_path = "obj_path"
        verts, faces = load_obj(obj_path)
        ps.register_surface_mesh("mesh_label", verts, faces, smooth_shade=True)

        ps.show()

if __name__ == "__main__":
     main()