class Sudoku():

    def __init__(self, sudoku_ls):
        self.sudoku_ls = sudoku_ls

    def get_yoko_sudoku_list(self):
        """ 数独のリストそのまま返す """
        return self.sudoku_ls

    def get_tate_sudoku_list(self):
        """ ほぼ転置、9*9のマス目を90度回転 """
        return [[self.sudoku_ls[i][j] for i in range(len(self.sudoku_ls))]
                for j in range(len(self.sudoku_ls[0]))]

    def get33_block(self):
        """
        9*9のマス目から3*3のマス目を抜き出す
        似たコードの重複が多くて気持ち悪い
        """
        result = []
        tmp1 = []
        tmp2 = []
        tmp3 = []
        for line in self.sudoku_ls:
            tmp1 += line[0:3]
            tmp2 += line[3:6]
            tmp3 += line[6:9]
            if len(tmp1) == 9:
                result.append(tmp1)
                result.append(tmp2)
                result.append(tmp3)
                tmp1 = []
                tmp2 = []
                tmp3 = []
        return result
    
    def judge_block33(self, x, y):
        """ 
        座標からブロックいくつに相当するか判断
        座標の定義域は 1~9
        """
        block_num = 0
        for i in range(1,4): # 1, 2, 3
            if y <= i*3:
                block_num += i*3
                break
        for i in range(1,4): # 1, 2, 3
            if x <= i*3:
                block_num -= 3-i
                break
        return block_num

    def is_num_unique(self, sudoku: list):
        """ 
        リスト内に重複がないか確認する
        """
        for _ in range(len(sudoku)):
            e = sudoku.pop()
            if (e in sudoku) and e != 0:
                return False
        return True
    
    def resolve(self, x, y):
        x_line = self.get_tate_sudoku_list()[x]
        y_row = self.get_yoko_sudoku_list()[y]
        block_33 = self.get33_block()
        def pos_resolve():
            """ 縦, 横, 3*3 の全ての数字を洗い出して解決 """
            not_exists = set(range(1,10))
            num_exists_set = set(x_line+y_row+block_33)
            not_exists.difference_update(num_exists_set)
            if len(not_exists)==1:
                return not_exists.pop()
            return 0
        
        def num_resolve():
            """ 任意の数字の存在場所が一か所に絞り込めるかで解決 """
            for num in range(1,10):
                """ 3*3に対して """

                """ 横列に対して """

                """ 縦列に対して """
                pass
        if pos_resolve():
            return pos_resolve()
        if num_resolve():
            return num_resolve()
        return 0


class TestSudoku():
    sudoku_ls = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 3, 1, 4, 0],
                 [0, 8, 6, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 5, 0, 0, 0, 0, 8],
                 [4, 0, 0, 0, 0, 9, 0, 0, 0],
                 [1, 0, 0, 0, 4, 0, 0, 9, 0],
                 [0, 0, 0, 0, 0, 0, 0, 3, 0],
                 [0, 5, 0, 8, 0, 0, 0, 0, 6]]

    def __init__(self) -> None:
        self.sudoku = Sudoku(TestSudoku.sudoku_ls)

    def test_yoko(self):
        print("---yoko---")
        print(*self.sudoku.get_yoko_sudoku_list(), sep="\n")
    
    def test_tate(self):
        print("---tate---")
        print(*self.sudoku.get_tate_sudoku_list(), sep="\n")

    def test_get33(self):
        print("---get33---")
        print(*self.sudoku.get33_block(), sep="\n")

    def test_unique(self):
        print("---is_unique---")
        ls = list(range(1, 10)) + [1]
        print("ls", ls)
        print(self.sudoku.is_num_unique(ls))

        ls2 = list(range(1, 10))
        print("ls2", ls2)
        print(self.sudoku.is_num_unique(ls2))

        ls3 = [0] * 9
        print("ls3", ls3)
        print(self.sudoku.is_num_unique(ls3))


if __name__ == "__main__":
    test = TestSudoku()
    test.test_yoko()
    test.test_tate()
    test.test_get33()
    test.test_unique()
