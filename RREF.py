def getMatrix(filename):
    f = open(filename, "rt")
    rows = f.readlines()
    mat = []
    for row in rows:
        row = row.replace("\n", '').split()
        mat.append(row)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = int(mat[i][j])
    return mat

def display(mat):
    row = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == 0:
                row += "| " + str(mat[i][j])
            elif j == len(mat[0]) - 1:
                row += " | " + str(mat[i][j]) + " |" 
            else:
                row += "  " + str(mat[i][j])
        print(row)
        row = ""
 
def rref(mat):
    for i in range(len(mat)):
        if mat[i][i] == 0:
            continue
        mat[i] = [cell / mat[i][i] for cell in mat[i]]
        for r, row in enumerate(mat):
            if r != i:
                scale = -1 * row[i]
                mat[r] = [curr + scale * other for curr, other in zip(mat[r], mat[i])]
    return mat

def toInt(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = int(mat[i][j])
    return mat

if __name__ == "__main__":
    while True:
        filename = input("Type File Name : ")
        matrix = getMatrix(filename)

        print("--- Augmented Matrix ---")
        display(matrix)
        print()

        print("--- RREF Matrix ----")
        matrix_rref = toInt(rref(matrix))
        display(matrix_rref)

        print()
        opt = input("Continue?(Y/N) : ")
        print()
        if opt == "Y" or opt == "y" or opt == "Yes" or opt == "yes" or opt == "YES":
            continue
        else:
            break