# Warshall Algorithm to find the transisitve closure of an adjacency matrix
# I threw this code together whilst revising , so excuse the poorly written code. :I

import itertools

class matrix():
    def __init__(self, n):
        self.rows , self.column= n , n
        self.__matrix = []

    def run(self):
        self.showMatrix()
        runs = 0
        while runs != self.rows:
            run = self.__getCartesian(self.__getColumn(runs),self.__getRow(runs))
            self.__warhsallAlgorithm(run)
            runs += 1
            print("\nM%s" % (runs))
            self.showMatrix()

        print("Finished in %s runs"%(runs))

    def showMatrix(self):
        for i in self.__matrix:
            for j in i:
                print(j, end="\t")
            print("")
        print("\n")

    def __warhsallAlgorithm(self, additions):
        for cordinates in additions:
            self.__addone(cordinates[0], cordinates[1])

    def __addone(self, row, col):
        self.__matrix[row][col] = 1

    def addRow(self, row):
        self.__matrix.append(row)

    def __getRow(self,q):
        row = []
        for i in range(self.rows):
            if self.__matrix[q][i] == 1:
                row.append(i)
        return row

    def __getColumn(self,q):
        column = []
        for i in range(self.column):
            if self.__matrix[i][q] == 1:
                column.append(i)
        return column

    def __getCartesian(self, a, b):
        cartesian = []
        if (len(a) == 0 or len(b) == 0):
            return []
        else:
            for element in itertools.product(a, b):
                if element not in cartesian:
                    cartesian.append(element)
            return cartesian

def start():
    n = int(input("How many n rows/colums are there?:\t"))
    if n < 1:
        print("Only natural numbers")
        start()

    matrix1 = matrix(n)
    for i in range(n):
        rowX = input("Enter matrix row %s:\t"%(i+1))
        matrix1.addRow(list(map(int, rowX.split(" "))))
    matrix1.run()

if __name__ == '__main__':
    start()
