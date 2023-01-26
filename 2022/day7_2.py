import sys
from typing import List, Dict
from bigtree import Node, print_tree, find_children
from bigtree.utils.exceptions import TreeError

MAX_SIZE: int = 70000000
MIN_SIZE: int = 30000000

root_node: Node = Node("root", type="dir")
current_dir: Node = root_node
dir_sizes: Dict[str, int] = {}

file = open('input7.txt')
line = file.readline()


def get_parent_paths(p_path: str) -> List[str]:
    parent_paths: List[str] = []
    parent_names: List[str] = p_path.split("/")[1:]
    nb_paths: int = len(parent_names)
    for _ in range(nb_paths):
        path: str = "/".join(parent_names)
        parent_paths.append(path)
        del parent_names[-1]
    return parent_paths


def create_node(name: str, node_type: str, file_size: int = -1) -> Node:
    global current_dir
    try:
        if node_type == "dir":
            if current_dir is not None:
                return Node(name, type=node_type, parent=current_dir)
            else:
                return Node(name, type=node_type)
        elif node_type == "file":
            f_node: Node = Node(name, type=node_type, f_size=file_size, parent=current_dir)
            p_node: Node = f_node.parent
            all_parents: List[str] = get_parent_paths(p_node.path_name)  # p_node.path_name.split("/")[1:]
            for p in all_parents:
                if p in dir_sizes:
                    dir_sizes[p] = dir_sizes.get(p) + file_size
                else:
                    dir_sizes.update({p: file_size})
            return f_node
    except TreeError as err:
        print(err)  # node already exists


def change_dir(d_name: str) -> None:
    global current_dir
    if d_name == "/":
        current_dir = root_node
    elif d_name == "..":
        current_dir = current_dir.parent
    else:
        current_dir = find_children(current_dir, d_name)


line = line.strip()
while line:
    if line.startswith("$"):
        line = line.split(" ")
        cmd: str = line[1]
        if cmd == "cd":
            directory: str = line[2]
            change_dir(directory)
        elif cmd == "ls":
            pass  # do nothing
    else:
        line = line.split(" ")
        if line[0] == "dir":
            create_node(line[1], "dir")
        else:
            create_node(line[1], "file", int(line[0]))
    line = file.readline().strip()
file.close()

# print_tree(root_node, attr_list=["type", "f_size"])

unused_space: int = MAX_SIZE - dir_sizes["root"]
missing_space: int = MIN_SIZE - unused_space

size_dir_to_delete: int = sys.maxsize
for d, s in dir_sizes.items():
    if missing_space < s < size_dir_to_delete:
        size_dir_to_delete = s

print("ANSWER = {0}".format(size_dir_to_delete))
