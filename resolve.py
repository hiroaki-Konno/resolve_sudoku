import pandas as pd
from sudoku import Sudoku as sd
from gene_array import generate_sudoku_list as gsl

#question_string = "000000000000000027400608000071000300238506419964100750395027800182060974046819205"
#ans_string = "619732548853941627427658193571294386238576419964183752395427861182365974746819235"
dataframe = pd.read_csv("data/sudoku_string.csv", delimiter=',', header=0)
value = dataframe.values

i = 0 # csvのi番目の数独を解くように指定
question_string = value[i][0]
ans_string = value[i][1]
url = value[i][2]

q_sudoku_ls = gsl(question_string)
""" 
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 2, 7]
[4, 0, 0, 6, 0, 8, 0, 0, 0]
[0, 7, 1, 0, 0, 0, 3, 0, 0]
[2, 3, 8, 5, 0, 6, 4, 1, 9]
[9, 6, 4, 1, 0, 0, 7, 5, 0]
[3, 9, 5, 0, 2, 7, 8, 0, 0]
[1, 8, 2, 0, 6, 0, 9, 7, 4]
[0, 4, 6, 8, 1, 9, 2, 0, 5]
"""
ans_sudoku_ls = gsl(ans_string)


sudoku = sd(q_sudoku_ls)

if __name__ == "__main__":
    print("before",*sudoku.sudoku_ls, sep="\n")
    is_improve = True
    count = 0
    while is_improve:
        count += 1
        is_improve = False
        for x in range(1,10):
            for y in range(1,10):
                tmp = sudoku.resolve(x, y)
                tmp2 = sudoku.sudoku_ls[y-1][x-1]
                if tmp and not tmp2:
                    sudoku.sudoku_ls[y-1][x-1] = tmp
                    is_improve = True
                    #print(x, y)
        print(count)
    print("after", *sudoku.sudoku_ls, sep="\n")
    print("---")
    print(*ans_sudoku_ls, sep="\n")
    print("\n", sudoku.sudoku_ls == ans_sudoku_ls)
    
