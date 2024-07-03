import open3d as o3d
import numpy as np
import argh

class CustomDraw:
    def __init__(self,mesh_file) -> None:

        if isinstance(mesh_file, str):
            # 读取网格文件
            mesh = o3d.io.read_triangle_mesh(mesh_file)  # 替换为实际的文件路径
        elif isinstance(mesh_file, o3d.geometry.TriangleMesh):
            mesh = mesh_file
        else:
            print("invalid input!should be mesh or file path")
            return
        # 使用法线信息生成颜色数组
        mesh.compute_vertex_normals()
        colors = (np.asarray(mesh.vertex_normals) + 1.0) / 2.0
        mesh.vertex_colors = o3d.utility.Vector3dVector(colors)

        # 创建可视化窗口并添加网格
        visualizer = o3d.visualization.Visualizer()
        visualizer.create_window()
        visualizer.add_geometry(mesh)

        # 设置渲染选项
        render_option = visualizer.get_render_option()
        render_option.light_on = False
        render_option.mesh_show_wireframe = False
        render_option.mesh_show_back_face = True

        # 运行可视化窗口
        visualizer.run()
        visualizer.destroy_window()
    
# 函数定义，用于在新线程中显示点云
def visualize_cloud(points, window_name):
    cloud=color_point_cloud_by_normals(points)
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name=window_name)
    render_option = vis.get_render_option()
    render_option.light_on = False
    vis.add_geometry(cloud)
    vis.run()
    vis.destroy_window()

def color_point_cloud_by_position(points):
    """
    根据点云的x, y, z坐标对点云进行着色。

    参数:
    points (numpy.ndarray): 点云的坐标数组，形状为(N, 3)，其中N是点的数量。

    返回:
    open3d.geometry.PointCloud: 着色后的点云对象。
    """
    # 创建点云对象
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(points)

    # 获取点云的x, y, z坐标
    x_values = points[:, 0]
    y_values = points[:, 1]
    z_values = points[:, 2]

    # 标准化坐标到0-1范围
    x_min, x_max = x_values.min(), x_values.max()
    y_min, y_max = y_values.min(), y_values.max()
    z_min, z_max = z_values.min(), z_values.max()

    x_normalized = (x_values - x_min) / (x_max - x_min)
    y_normalized = (y_values - y_min) / (y_max - y_min)
    z_normalized = (z_values - z_min) / (z_max - z_min)

    # 使用标准化的坐标作为颜色值
    colors = np.zeros((points.shape[0], 3))
    colors[:, 0] = x_normalized  # 红色通道
    colors[:, 1] = y_normalized  # 绿色通道
    colors[:, 2] = z_normalized  # 蓝色通道

    # 将颜色赋给点云
    cloud.colors = o3d.utility.Vector3dVector(colors)

    return cloud
def color_point_cloud_by_normals(points, normals=None):
    """
    根据点云的法线对点云进行着色。

    参数:
    points (numpy.ndarray): 点云的坐标数组，形状为(N, 3)，其中N是点的数量。
    normals (numpy.ndarray, optional): 点云的法线数组，形状为(N, 3)。如果未提供，将自动计算法线。

    返回:
    open3d.geometry.PointCloud: 着色后的点云对象。
    """
    # 创建点云对象
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(points)

    # 如果未提供法线，则计算法线
    if normals is None:
        cloud.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
        normals = np.asarray(cloud.normals)
    else:
        cloud.normals = o3d.utility.Vector3dVector(normals)

    # 标准化法线到0-1范围
    normals_min = normals.min(axis=0)
    normals_max = normals.max(axis=0)
    normals_normalized = (normals - normals_min) / (normals_max - normals_min)

    # 使用法线作为颜色值
    cloud.colors = o3d.utility.Vector3dVector(normals_normalized)

    return cloud
def main(
        mesh_file: str = "/home/zoratt/3D/vdbfusion/examples/python/results/fastlio_rgb_pts_hkust_01.bag_1504_scans.ply"
):
   CustomDraw(mesh_file)

if __name__ == "__main__":
    argh.dispatch_command(main)