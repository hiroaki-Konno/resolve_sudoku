class Sudoku():

    def __init__(self, sudoku_ls):
        self.sudoku_ls = sudoku_ls

    # 数独のリストそのまま返す
    def get_yoko_sudoku_list(self):
        return self.sudoku_ls

    # ほぼ転置、9*9のマス目を90度回転
    def get_tate_sudoku_list(self):
        return [[self.sudoku_ls[i][j] for i in range(len(self.sudoku_ls))]
                for j in range(len(self.sudoku_ls[0]))]

    # 9*9のマス目から3*3のマス目を抜き出す
    def get33_block(self):
        # 似たコードの重複が多くて気持ち悪い
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

    # リスト内に重複がないか確認する
    def is_num_unique(self, sudoku: list):
        for _ in range(len(sudoku)):
            e = sudoku.pop()
            if (e in sudoku) and e != 0:
                return False
        return True


class TestSudoku():
    sudoku_ls = [['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                 ['0', '0', '0', '0', '0', '3', '1', '4', '0'],
                 ['0', '8', '6', '0', '0', '0', '0', '0', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '0', '2'],
                 ['0', '0', '0', '5', '0', '0', '0', '0', '8'],
                 ['4', '0', '0', '0', '0', '9', '0', '0', '0'],
                 ['1', '0', '0', '0', '4', '0', '0', '9', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '3', '0'],
                 ['0', '5', '0', '8', '0', '0', '0', '0', '6']]

    def __init__(self) -> None:
        self.sudoku = Sudoku(TestSudoku.sudoku_ls)

    def test_tate(self):
        print(self.sudoku.get_tate_sudoku_list(TestSudoku.sudoku_ls))

    def test_get33(self):
        print(*self.sudoku.get33_block(TestSudoku.sudoku_ls), sep="\n")

    def test_unique(self):
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
    # test.test_tate()
    # test.test_get33()
    test.test_unique()