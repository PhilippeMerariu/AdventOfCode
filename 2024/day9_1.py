file = open('input9.txt')
line = file.readline()

class ID:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def __repr__(self):
        return str(self.value)

data = ""
file_blocks = []

while line:
    line = line.strip('\n')
    data = line
    line = file.readline()
file.close()

is_block = True
id = 0
for d in data:
    if is_block:
        file_blocks += [ID(id)] * int(d)
        id += 1
    else:
        file_blocks += ['.'] * int(d)
    is_block = not is_block

while file_blocks.count('.'):
    idx = file_blocks.index('.')
    file_blocks[idx] = file_blocks[-1]
    file_blocks.pop()

result = 0
for i in range(len(file_blocks)):
    result += i * file_blocks[i].get()


print(f"ANSWER = {result}")
