import numpy as np

LIM_ZERO = 10 ** -6
LIM_CALC = 100000


def take_diagonal(array):
    j = 0
    new_arr = []
    for k in array:
        if abs(k[j]) < LIM_ZERO:
            continue
        new_arr.append(k[j])
        j += 1
    return new_arr


print("Enter matrix by rows separating with ;\nExample\n1 2; 3 4 --> [1, 2]\n", " " * 11, "[3, 4]\nEnter matrix:")
A = np.array(np.mat(input()))
for i in range(LIM_CALC):
    Q, R = np.linalg.qr(A)
    A = R @ Q

print("Full result: ", np.diagonal(A))
print("Result: ", take_diagonal(A))
