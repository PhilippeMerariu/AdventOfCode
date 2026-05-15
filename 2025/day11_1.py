file = open('input11.txt')
line = file.readline()

result = 0

devices = {}

while line:
    line = line.strip('\n')
    d, l = line.split(':')
    ods = [od for od in l.split(' ') if od]
    devices.update({d: ods})
    line = file.readline()
file.close()

#for k, v in devices.items():
#    print(f"DEVICE={k} ==> OUTPUTS={v}")

def find_paths(node: str) -> None:
    global result

    for child in devices.get(node, []):
        #print(f"from {node} to {child}")
        if child == 'out':
            result += 1
        find_paths(child)

find_paths('you')


print(f"ANSWER = {result}")
