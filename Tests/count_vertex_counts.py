def get_vertex_count_from_ply_header(ply_file_path):
    with open(ply_file_path, 'rb') as f:  # 使用二进制模式打开文件
        header = f.readline()
        while header:
            if b"end_header" in header:
                break  # 读到头部结束标志
            if b"element vertex" in header:
                return int(header.split()[2])  # 获取点云数量
            header = f.readline()
    return None  # 如果文件格式不正确或找不到点云数量，则返回None

# 使用示例
ply_file_path = 'D:\\3dgs\\outputs\\tandt\\truck\\baseline\\latest\\point_cloud\\iteration_40000\\point_cloud.ply'  # 替换为你的PLY文件路径
vertex_count = get_vertex_count_from_ply_header(ply_file_path)
print(f"Point cloud count: {vertex_count}")
