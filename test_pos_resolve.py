""" 
x_line = self.get_tate_sudoku_list()[x]
y_row = self.get_yoko_sudoku_list()[y]
block_33 = self.get33_block()
"""
x_line = []
y_row = []
block_33 = list(range(1,9))

def pos_resolve():
    """ 縦, 横, 3*3 の全ての数字を洗い出して解決 """
    not_exists = set(range(1,10))
    
    print(not_exists)
    num_exists_set = set(x_line+y_row+block_33)
    # num_exists_set = {1, 2, 3, 4, 5, 6, 7, 8}
    not_exists.difference_update(num_exists_set)

    print(not_exists)
    
    if len(not_exists)==1:
        return not_exists.pop()
    return 0

print(pos_resolve())