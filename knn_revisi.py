lama = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2],
    [1, 0, 1, 1, 2],
]

baru = [1, 0, 1, 1]

jarak = []
for data in lama:
    d = 0
    for i in range(4):
        if baru[i] != data[i]:
            d = d + 1
    jarak.append([d, data[4]])

jarak.sort()

tetangga = jarak[:5]

label_0 = 0
label_1 = 0
label_2 = 0

for d, label in tetangga:
    if label == 0:
        label_0 = label_0 + 1
    elif label == 1:
        label_1 = label_1 + 1
    else:
        label_2 = label_2 + 1

print("label 0:", label_0)
print("label 1:", label_1)
print("label 2:", label_2)

if label_0 > label_1 and label_0 > label_2:
    print("Hasil: 0")
elif label_1 > label_0 and label_1 > label_2:
    print("Hasil: 1")
else:
    print("Hasil: 2")
