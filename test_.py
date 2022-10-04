# x, y = (9, 2)
# block_num = 3 # 1~9
# i = 9
# def block33_num_resolve(i: int):
#     """ どこのブロックか、更新に関わる縦横の列の判定 """
#     # block_num = self.judge_block33(x, y)
#     # 縦列の範囲(x座標:0~8)
#     tate_group = ((block_num + 2) % 3)
#     print("tate_group",tate_group)
#     x_range = list(range(tate_group * 3, (tate_group+1) * 3))
#     print("x_range", x_range)
# 
#     # 横列の範囲(y座標:0~8)
#     yoko_group = 0
#     for i in range(1,4):
#         if block_num <= i*3:
#             yoko_group = i-1
#             break
#     print("yoko_group", yoko_group)
#     y_range = list(range(yoko_group * 3, (yoko_group+1) * 3))
#     print("y_range", y_range)
# 
# block33_num_resolve(i)

import pandas as pd

dataframe = pd.read_csv("data/sudoku_string.csv", delimiter=',', header=0)
value = dataframe.values

i = 0
question_string = value[i][0]
ans_string = value[i][1]
url = value[i][2]