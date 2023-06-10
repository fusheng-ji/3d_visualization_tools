import polyscope as ps
import numpy as np
import tqdm
from tqdm import tqdm
import open3d as o3d

ps.init()
ps.set_ground_plane_mode("none") 
ps.set_up_dir("z_up")

def load_obj(obj_path):
    mesh = o3d.io.read_triangle_mesh(obj_path)
    pcd = mesh.sample_points_uniformly(number_of_points=50000) 
    points = np.asarray(pcd.points)
    return points


def main():
        obj_path = "obj_path"
        points = load_obj(obj_path)
        ps.register_point_cloud("points_name", points, point_render_mode='quad')
        ps.show()

if __name__ == "__main__":
     main()
