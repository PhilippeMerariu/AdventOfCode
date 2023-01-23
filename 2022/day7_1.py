from typing import List, Dict
from bigtree import Node, print_tree, find_name, find_attrs
from bigtree.utils.exceptions import TreeError

MAX_SIZE: int = 100000

root_node: Node = Node("root", type="dir")

current_dir: str = "root"
parent_dir: str = ""

file = open('input7.txt')
line = file.readline()


def create_node(name: str, node_type: str, parent: str = "", file_size: int = -1) -> None:
    try:
        if node_type == "dir":
            if parent != "":
                Node(name, type=node_type, parent=find_name(root_node, parent))
            else:
                Node(name, type=node_type)
        elif node_type == "file":
            Node(name, type=node_type, f_size=file_size, parent=find_name(root_node, parent))
    except TreeError:
        pass  # node already exists


def change_dir(d: str) -> None:
    global current_dir
    global parent_dir
    if d == "/":
        create_node("root", "dir")
        current_dir = "root"
        parent_dir = ""
    else:
        create_node(d, "dir", current_dir)
        parent_dir = current_dir
        current_dir = d


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
            create_node(line[1], "dir", current_dir)
        else:
            create_node(line[1], "file", current_dir, int(line[0]))
    line = file.readline().strip()
file.close()

print_tree(root_node, attr_list=["type", "f_size"])

for node in find_name(root_node, "root").children:
    for child_dir in find_attrs(node, "type", "file"):
        pass


print("ANSWER = {0}".format())
