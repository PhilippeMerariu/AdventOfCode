file = open('input9.txt')
line = file.readline()

class ID:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, a):
        return isinstance(a, ID) and a.value == self.value

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

last_id = file_blocks[-1]
while last_id.get() > 1:
    idxs = []
    # Find group of file blocks to move
    for i, item in enumerate(file_blocks):
        if isinstance(item, ID) and item == last_id:
            idxs.append(i)

    # Search for space and move
    empty_idxs = []
    for i, item in enumerate(file_blocks):
        if item == '.':
            empty_idxs.append(i)
            if len(empty_idxs) >= len(idxs) and empty_idxs[-1] < idxs[0]:
                for ei in empty_idxs:
                    file_blocks[ei] = last_id
                for i in idxs:
                    file_blocks[i] = '.'
                break
        else:
            empty_idxs.clear()

    last_id = ID(last_id.get() - 1)


result = 0
for i in range(len(file_blocks)):
    if isinstance(file_blocks[i], ID):
      result += i * file_blocks[i].get()


print(f"ANSWER = {result}")
