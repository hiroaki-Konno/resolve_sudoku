def tate_sudoku_list(sudoku: list):
    # tate_sudoku = [[sudoku[i][j] for i in range(len(sudoku))] 
    #                for j in range(len(sudoku[0]))]
    return [[sudoku[i][j] for i in range(len(sudoku))]
            for j in range(len(sudoku[0]))]

# print(tate_sudoku)

def is_num_unique(sudoku:list):
    for _ in range(len(sudoku)):
        e = sudoku.pop()
        if (e in sudoku) and e!=0:
            return False
    return True


ls = list(range(1,10))+[1]
print("ls", ls)
print(is_num_unique(ls))

ls2 = list(range(1,10))
print("ls2", ls2)
print(is_num_unique(ls2))

ls3 = [0]*9
print("ls3", ls3)
print(is_num_unique(ls3))

