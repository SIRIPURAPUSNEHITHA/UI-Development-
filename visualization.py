import open3d as o3d

def visualize_point_cloud(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    print(f"Loaded {file_path} with {len(pcd.points)} points.")
    
    o3d.visualization.draw_geometries([pcd], window_name="Point Cloud Viewer")

