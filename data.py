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
        # 高さ yの横列
        y_high = self.get_yoko_sudoku_list()[y-1]
        # 横座標 xの縦列
        x_width = self.get_tate_sudoku_list()[x-1]
        # 3 * 3 のブロック
        block_33 = self.get33_block()[self.judge_block33(x,y)]

        print("y_high", y_high)
        print("x_width", x_width)
        print("block_33", block_33)

        def pos_resolve():
            """ 縦, 横, 3*3 の全ての数字を洗い出して解決 """
            not_exists = set(range(1,10))
            num_exists_set = set(x_width+y_high+block_33)
            not_exists.difference_update(num_exists_set)
            if len(not_exists)==1:
                return not_exists.pop()
            return 0

        def yoko_num_resolve(i:int):
            """ 縦列の刺さり具合と横にあるブロックの中に iがあるかどうかの確認 """
            y_high_flag = [1]*9 # y_high_flag[x]のみ1になってほしい
            for m, num in enumerate(y_high):
                if num:
                    y_high_flag[m] = 0
            y_block33 = [] # ブロック列 格納用
            
            """ どこのブロック列か判定 """
            for k in range(1,4):
                if self.judge_block33(x,y) <= 3*k:
                    y_block33 = self.get33_block()[3*(k-1):3*k]
                    break
            
            """ ブロック列による可能性の更新 """
            for n, bl in enumerate(y_block33):
                if i in bl:
                    y_high_flag[n*3:(n+1)*3] = [0]*3
            
            """ 縦列による可能性の更新 """
            for n, x_flag in enumerate(y_high_flag):
                if (not x_flag) or (n == x):
                    pass
                if i in self.get_tate_sudoku_list()[n]:
                    y_high_flag[n] = 0

            print("i:", i, "yflags:", y_high_flag, "sum:", sum(y_high_flag))
            
            """ 判定返す y_high_flag[x] のみ1ならその数 iで確定 """
            if sum(y_high_flag) == 1:
                return i
            elif sum(y_high_flag) == 0:
                print("error: 数独あってる？")
            else:
                # 確定せず
                return 0
        
        def tate_num_resolve(i:int):
            """ 横列の刺さり具合と縦にあるブロックの中に iがあるかどうかの確認 """
            x_width_flag = [1]*9 # x_width_flag[y]のみ1になってほしい
            for m, num in enumerate(x_width):
                if num:
                    x_width_flag[m] = 0
            x_block33 = [] # ブロック列 格納用
            
            """ どこのブロック列か判定 """
            block_num = self.judge_block33(x,y) % 3
            x_block33 = self.get33_block()[(block_num+2)%3::3]
            #print(*x_block33, sep="\n")
            
            """ ブロック列による可能性の更新 """
            for n, bl in enumerate(x_block33):
                if i in bl:
                    x_width_flag[n*3:(n+1)*3] = [0]*3
            
            """ 横列による可能性の更新 """
            for n, y_flag in enumerate(x_width_flag):
                if (not y_flag) or (n == y):
                    pass
                if i in self.get_yoko_sudoku_list()[n]:
                    x_width_flag[n] = 0

            print("i:", i, "xflags:", x_width_flag, "sum:", sum(x_width_flag))
            
            """ 判定返す y_high_flag[x] のみ1ならその数 iで確定 """
            if sum(x_width_flag) == 1:
                return i
            elif sum(x_width_flag) == 0:
                print("error: 数独あってる？")
            else:
                # 確定せず
                return 0
      
        def num_resolve():
            """ 任意の数字の存在場所が一か所に絞り込めるかで解決 """
            for i in range(1,10):
                """ 被るならその数字パス """
                if (i in y_high) or (i in x_width) or (i in block_33):
                    continue
                # 横列に対して
                result = yoko_num_resolve(i)
                if result:
                    return result
                
                # 縦列に対して 
                result = tate_num_resolve(i)
                if result:
                    return result
                
                # 3*3に対して 
        
        can_solve_pos = pos_resolve()
        if can_solve_pos:
            return can_solve_pos
        
        can_solve_num = num_resolve()
        if can_solve_num:
            return can_solve_num
        return 0


class TestSudoku():
    """ sudoku_ls = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 3, 1, 4, 0],
                 [0, 8, 6, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 5, 0, 0, 0, 0, 8],
                 [4, 0, 0, 0, 0, 9, 0, 0, 0],
                 [1, 0, 0, 0, 4, 0, 0, 9, 0],
                 [0, 0, 0, 0, 0, 0, 0, 3, 0],
                 [0, 5, 0, 8, 0, 0, 0, 0, 6]] """
    
    """ tst_yk_rl = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 9, 0, 0, 3, 1, 4, 0],
                 [0, 8, 6, 0, 9, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 9, 0, 2],
                 [0, 9, 0, 5, 0, 0, 0, 0, 8],
                 [4, 0, 0, 0, 0, 9, 0, 0, 0],
                 [1, 0, 0, 0, 4, 0, 0, 0, 9],
                 [0, 0, 0, 9, 0, 0, 0, 3, 0],
                 [9, 5, 0, 8, 0, 0, 0, 0, 6]]
    sudoku_ls = tst_yk_rl # (x, y)=(8, 1)
    """
    
    tst_tt_rl = [[0, 0, 9, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 3, 1, 4, 0],
                 [0, 8, 6, 0, 9, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 5, 0, 0, 0, 0, 8],
                 [4, 0, 0, 0, 0, 9, 0, 0, 0],
                 [1, 0, 0, 0, 4, 0, 0, 9, 0],
                 [0, 0, 0, 0, 0, 0, 0, 3, 0],
                 [0, 5, 0, 8, 0, 0, 0, 0, 6]]
    sudoku_ls = tst_tt_rl #(x, y)=(9, 2)

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
    
    def test_judge33(self):
        print("---judge---")
        print(self.sudoku.judge_block33(9,2))

    def test_yoko_resolve(self):
        print("---yoko_resolve---")
        print(self.sudoku.resolve(8,1))

    def test_tate_resolve(self):
        print("---tate_resolve---")
        print(self.sudoku.resolve(9,2))

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
    # test.test_judge33()
    # test.test_unique()
    # test.test_yoko_resolve()
    test.test_tate_resolve()
