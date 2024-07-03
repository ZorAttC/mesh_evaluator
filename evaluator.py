import csv
from mesh_evaluator.eval_utils import eval_mesh
from mesh_evaluator.eval_utils import eval_mesh2mesh
import argh
from mesh_evaluator.config import *



# pred_mesh_path = "xxx/baseline/vdb_fusion_xxx.ply"
# method_name = "vdb_fusion_xxx"

# pred_mesh_path = "xxx/baseline/puma_xxx.ply"
# method_name = "puma_xxx"

def main(
        pred_mesh_path:str=c_pred_mesh_path,
        gt_ply_path:str=c_gt_pcd_path,
        eval_mode:int=0,#0 for mesh2mesh,1 for mesh2pointcloud
):

    if eval_mode == 0:
        print("mesh to mesh evaluation")
        eval_metric = eval_mesh2mesh(pred_mesh_path, gt_ply_path, down_sample_res=down_sample_vox, threshold=dist_thre, 
                                truncation_acc = truncation_dist_acc, truncation_com = truncation_dist_com, gt_bbx_mask_on = True,icp_align=icp_align) 

        print(eval_metric)

        evals = [eval_metric]

        csv_columns = ['MAE_accuracy (m)', 'MAE_completeness (m)', 'Chamfer_L1 (m)', 'Chamfer_L2 (m)', \
                'Precision [Accuracy] (%)', 'Recall [Completeness] (%)', 'F-score (%)', 'Spacing (m)', \
                'Inlier_threshold (m)', 'Outlier_truncation_acc (m)', 'Outlier_truncation_com (m)']

        try:
            with open(output_csv_path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in evals:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
    elif eval_mode==1:
        print("mesh to pointcloud evaluation")
        #TODO:translation not implemented
        eval_metric = eval_mesh(pred_mesh_path, gt_ply_path, down_sample_res=down_sample_vox, threshold=dist_thre, 
                                truncation_acc = truncation_dist_acc, truncation_com = truncation_dist_com, gt_bbx_mask_on = True) 

        print(eval_metric)

        evals = [eval_metric]

        csv_columns = ['MAE_accuracy (m)', 'MAE_completeness (m)', 'Chamfer_L1 (m)', 'Chamfer_L2 (m)', \
                'Precision [Accuracy] (%)', 'Recall [Completeness] (%)', 'F-score (%)', 'Spacing (m)', \
                'Inlier_threshold (m)', 'Outlier_truncation_acc (m)', 'Outlier_truncation_com (m)']

        try:
            with open(output_csv_path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in evals:
                    writer.writerow(data)
        except IOError:
            print("I/O error")


if __name__ == "__main__":
    argh.dispatch_command(main)

