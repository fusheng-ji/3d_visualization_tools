import polyscope as ps
import numpy as np
import tqdm
from tqdm import tqdm
import open3d as o3d
import os
ps.init()
ps.set_ground_plane_mode("none") 
ps.set_up_dir("z_up")

def load_ann(annonation_path):
    print(f"->loading point cloud... {annonation_path}")
    annfile=[]
    point_temp_ls=[]
    all_points_ls = []

    annfile=open(f"{annonation_path}",'r').readlines()
    ls_len = len(annfile)
    print(ls_len)
    for point in tqdm(annfile, total = ls_len):
         point_temp_ls = point.strip('\n').split(' ')[:3]
         point_temp_ls = [float(i) for i in point_temp_ls]
         all_points_ls.append(point_temp_ls)

    point_cloud_np=np.array(all_points_ls)
    return point_cloud_np


def main():
        semantic_ann_dir = "Annotations_path"
        files = []
        files = os.listdir(semantic_ann_dir)
        lens = len(files)
        for __, name in tqdm(enumerate(files), total=lens):
               label = name[2:-4]
               points = load_ann(semantic_ann_dir + name)
               
               ps.register_point_cloud(label, points, radius=0.0002)   
        
        origin_point_dir = "origin_point_cloud_path"
        origin_point = points = load_ann(origin_point_dir)
        ps.register_point_cloud("origin", origin_point, radius=0.0003, point_render_mode='quad')
        ps.show()

if __name__ == "__main__":
     main()
