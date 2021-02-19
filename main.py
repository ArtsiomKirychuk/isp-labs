def printMatrix(matrix, row, cols):
    for i in range(row):
        line = ""
        for j in range(cols):
            line += str(matrix[i][j]) + '\t'
            if j == cols - 1:
                line += '| '
        print(line)
    print('')

def gauss(matrix):
    for i in range(len(matrix)):
        maxElement = abs[matrix[i][i]]
        maxRow = i
        for k in range(i+1, len(matrix)):
            if abs(matrix[k][i]) > maxElement:
                maxElement = abs(matrix[k][i])
                maxRow=k
        for k in range(i, len(matrix) + 1):
            temp = matrix[maxRow][k]
            matrix[maxRow][k] = matrix[i][k]
            matrix[i][k]= temp
        for k in range(i + 1, len(matrix)):
            invCoefficien = -matrix[k][i] / matrix[i][i]
            for j in range(i, len(matrix) + 1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += invCoefficien * matrix[i][j]
    return findResultVector(matrix)



def findResultVector(matrix):
    x = [0 for i in range(len(matrix))]
    for i in range(len(matrix) -1, -1, -1):
        x[i] = matrix[i][len(matrix)] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][len(matrix)] -= matrix[k][i] * x[i]
    return x



def main():
    rows = int(input('Enter the numbers of rows: '))
    columns = int(input('Enter the number of columns: '))
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    printMatrix(matrix,rows,columns)

if __name__ == '__main__':
    main()
