import struct

def parse_binary_ply(file_path):
    """
    Parse the header and binary data of a PLY file to extract vertex data as text.
    """
    with open(file_path, 'rb') as file:
        # Read header
        header = []
        while True:
            line = file.readline().strip().decode('ascii')
            header.append(line)
            if line == "end_header":
                break

        # Read body
        vertices = []
        while True:
            line = file.read(100)  # Read blocks of 100 bytes
            if not line:
                break
            vertices.append(line)

        return header, vertices

def parse_vertex_data(binary_data, header):
    """
    Parse the vertex data from binary to human-readable text format based on the header definition.
    """
    # Determine the format from the header
    format_string = '<'  # Little endian
    property_names = []
    for line in header:
        if line.startswith("property"):
            parts = line.split()
            prop_type = parts[1]
            prop_name = parts[2]
            property_names.append(prop_name)
            if prop_type == "float":
                format_string += 'f'  # Float (4 bytes)
            elif prop_type == "uchar":
                format_string += 'B'  # Unsigned byte (1 byte)

    # Size of one vertex data block in bytes
    vertex_size = struct.calcsize(format_string)
    
    # Parse each vertex
    vertices = []
    for i in range(0, len(binary_data), vertex_size):
        vertex_block = binary_data[i:i+vertex_size]
        if len(vertex_block) == vertex_size:
            values = struct.unpack(format_string, vertex_block)
            vertex_str = ", ".join(f"{prop_name}={value:.3f}" for prop_name, value in zip(property_names, values))
            vertices.append(vertex_str)

    return vertices

def create_ply_from_text(text_path, output_ply_path, header):
    """
    Create a PLY file from a text file containing vertex data.
    """
    with open(text_path, 'r') as file:
        vertices = file.readlines()

    with open(output_ply_path, 'wb') as file:
        # Write header
        for line in header:
            file.write((line + '\n').encode('ascii'))

        # Write vertex data
        for vertex in vertices:
            values = [float(v.split('=')[1]) for v in vertex.split(', ')]
            data = struct.pack('<' + 'f' * len(values), *values)
            file.write(data)


file_path = 'D:\\downloads\\demo_fox_gs.ply'

# TODO： 转换过来
# Parse PLY file and extract header and vertices
# header, binary_vertices = parse_binary_ply(file_path)

# # Concatenate binary vertex data
# full_binary_data = b''.join(binary_vertices)

# # Parse the vertex data
# parsed_vertices = parse_vertex_data(full_binary_data, header)

# # Save parsed vertices to a text file
# output_path = 'parsed_vertices.txt'
# with open(output_path, 'w') as file:
#     for vertex in parsed_vertices:
#         file.write(vertex + "\n")

# TODO: 转换回去
header, _ = parse_binary_ply(file_path)
create_ply_from_text('parsed_vertices.txt', 'output.ply', header)
