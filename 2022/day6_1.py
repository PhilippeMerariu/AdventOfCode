file = open('input6.txt')
line = file.readline().strip()
file.close()

NB_CHARS: int = 4
start_char: int = NB_CHARS

while start_char < len(line):
    if len(list(set(line[start_char-NB_CHARS:start_char]))) == NB_CHARS:
        break
    start_char += 1

print("ANSWER = {0}".format(start_char))
