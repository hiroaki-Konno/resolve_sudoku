# http://www.sudokugame.org/archive/printsudoku.php?nd=3&xh=1 より
senmon1_num = "000000000000003140086000000000000002000500008400009000100040090000000030050800006"

num = "0" * 81

# num = senmon1_num


def generate_sudoku_list(num: str):
    # sudoku = [list(map(int, num[i*9:i*9+9])) for i in range(9)]
    if len(num) != 81:
        return []
    return [list(map(int, num[i * 9:i * 9 + 9])) for i in range(9)]


sudoku = generate_sudoku_list(num)
print(sudoku)
""" 
[['0', '0', '0', '0', '0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '3', '1', '4', '0'],
 ['0', '8', '6', '0', '0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '0', '0', '0', '2'],
 ['0', '0', '0', '5', '0', '0', '0', '0', '8'],
 ['4', '0', '0', '0', '0', '9', '0', '0', '0'],
 ['1', '0', '0', '0', '4', '0', '0', '9', '0'],
 ['0', '0', '0', '0', '0', '0', '0', '3', '0'],
 ['0', '5', '0', '8', '0', '0', '0', '0', '6']]
  """


def tate_sudoku_list(sudoku: list):
    # tate_sudoku = [[sudoku[i][j] for i in range(len(sudoku))] 
    #                for j in range(len(sudoku[0]))]
    return [[sudoku[i][j] for i in range(len(sudoku))]
            for j in range(len(sudoku[0]))]

def is_unique(sudoku:list):
    


# print(tate_sudoku)