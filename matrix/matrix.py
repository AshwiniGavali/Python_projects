class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        s = matrix_string
        sp_line= s.split("\n")
        fs = []
        for s in sp_line:
            fs.append(s.split())
        self.ref_len = len(fs[0])
        for s in fs:
            if self.ref_len != len(s):
                print("invalid array")
                return
        self.matrix = []
        for s in fs:
            temp = []
            for each in s:
                temp.append(int(each))
            self.matrix.append(temp)

    def row(self, index):
        index = index -1
        result = []
        for i in range(0,self.ref_len):
            result.append(self.matrix[index][i])
        return result

    def column(self, index):
        index = index-1
        result = []
        for i in range(0, len(self.matrix)):
            result.append(self.matrix[i][index])
        return result
