from dataset.gmm import GMMDataset as Dataset
from sogmm_py.vis_open3d import VisOpen3D
import numpy as np
import open3d as o3d
from sogmm_py.utils import o3d_to_np, np_to_o3d
from sogmm_py.sogmm import SOGMM
from vdbfusion_pipeline import VDBFusionPipeline as Pipeline
from visualize_pc import visualize_cloud,color_point_cloud_by_normals
fastlio_root_dir="/home/zoratt/datasets/VETS"
bag_name="maicity00.bag"
pointcloud_name="/encoded_pointcloud"
config="/home/zoratt/3D/gira3d-reconstruction/docs/test/config/maicity.yaml"
odom_name="/encoded_odometry"
n_scans=700
dataset=Dataset(fastlio_root_dir, bag_name,odom_name,pointcloud_name, config,n_scans)
K = np.eye(3)
K[0, 0] = 525.0
K[1, 1] = 525.0
K[0, 2] = 319.5
K[1, 2] = 239.5
W = (int)(640)
H = (int)(480)
pipline=Pipeline(dataset,config,"maicity",0,n_scans)
# for idx,scan in enumerate(dataset.scans):

#     # pcld_deci_np =  np.concatenate(dataset.scans[:4],axis=0)
#     pcld_deci_np = np.concatenate([scan, np.ones((scan.shape[0],1))*0], axis=1)

#     sg_gpu = SOGMM(bandwidth=0.02, compute='GPU')
#     model_gpu = sg_gpu.fit(pcld_deci_np)
#     print(model_gpu.n_components_)
    


#     print(pcld_deci_np[:3])
#     if idx%10==0:
#         resampled_pcld = sg_gpu.joint_dist_sample(pcld_deci_np.shape[0])
#         pcld_pose = np.eye(4)
#         vis = VisOpen3D(visible=True)
#         vis.visualize_pcld(np_to_o3d(resampled_pcld), pcld_pose, K, W, H)
#         vis.render()
#         del vis

global_pc=np.concatenate(dataset.scans[:n_scans],axis=0)
# 创建一个Open3D的PointCloud对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(global_pc)

# 下采样
down_pcd = pcd.voxel_down_sample(voxel_size=0.05)

# 将下采样后的点云转换回numpy数组
downsampled_global_pc = np.asarray(down_pcd.points)
# 保存点云
o3d.io.write_point_cloud("downsampled_vox0.05_maicity.ply", down_pcd)
visualize_cloud(downsampled_global_pc,'colored_pc')






