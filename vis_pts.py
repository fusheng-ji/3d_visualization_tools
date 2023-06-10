import polyscope as ps
import numpy as np
import tqdm
from tqdm import tqdm
import open3d as o3d
# Initialize polyscope
ps.init()

### Register a point cloud
def creat_numpy(path):
    print(f"->loading file... {path}")
    ptsfile=[]
    point_temp_ls=[]
    all_points_ls = []
    #first line of pts format need to be ignored
    ptsfile=open(f"{path}",'r').readlines()[1:]
    ls_len = len(ptsfile)
    print(ls_len)
    for point in tqdm(ptsfile, total = ls_len):
         point_temp_ls = point.strip('\n').split(' ')[:3]
         point_temp_ls = [float(i) for i in point_temp_ls]
         all_points_ls.append(point_temp_ls)
    # convert points to numpy array
    point_cloud_np=np.array(all_points_ls)
    return point_cloud_np

def main():
        pts_path = "pts_path"
        points = creat_numpy(pts_path)
        ps.register_point_cloud("points_name", points, point_render_mode='quad')
        ps.show()

if __name__ == "__main__":
     main()