########################################### MaiCity Dataset ###########################################
dataset_name = "maicity_01_"
c_gt_pcd_path = "/home/zoratt/ImMesh_output/kitti04_raw.ply"
c_pred_mesh_path = "/home/zoratt/ImMesh_output/kitti04_raw.ply"
method_name = "ours_gt"
# evaluation results output file
base_output_folder = "./experiments/evaluation/"
output_csv_path =  method_name + "_eval.csv"
# evaluation parameters
# For MaiCity
down_sample_vox = 0.05 #-1 means no downsample,to make sure the same density as the ground truth
dist_thre = 0.2
truncation_dist_acc = 2.0 
truncation_dist_com = 2.0
icp_align=False
