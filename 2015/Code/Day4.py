import hashlib

input = 'yzbqklnj'
nb = 1
data = input + str(nb)

hash = hashlib.md5(data.encode())
hex = hash.hexdigest()

while hex[0:5] != '00000':
    nb += 1
    data = input + str(nb)
    hash = hashlib.md5(data.encode())
    hex = hash.hexdigest()

    print(data + ' --> ' + hex)

print("Result: " + str(nb))



