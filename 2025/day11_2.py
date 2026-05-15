file = open('input11.txt')
line = file.readline()

result = 0

devices = {}
start_node = 'svr'

while line:
    line = line.strip('\n')
    d, l = line.split(':')
    ods = [od for od in l.split(' ') if od]
    devices.update({d: ods})
    line = file.readline()
file.close()


#for k, v in devices.items():
#    print(f"DEVICE={k} ==> OUTPUTS={v}")

memo = {}
def find_paths(node: str, has_fft: bool, has_dac: bool) -> int:
    global count

    if node == 'fft':
        has_fft = True
    if node == 'dac':
        has_dac = True
    if node == 'out':
        return 1 if (has_fft and has_dac) else 0

    state = (node, has_fft, has_dac)
    if state in memo:
        return memo[state]

    total_paths = 0
    children = devices.get(node, [])
    for child in children:
        total_paths += find_paths(child, has_fft, has_dac)

    memo[state] = total_paths
    return total_paths

result = find_paths(start_node, False, False)

print(f"ANSWER = {result}")
