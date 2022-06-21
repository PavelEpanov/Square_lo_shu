def main():
    square_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    index_str = 0
    index_col = 0

    index_show_col = 1


    while index_str != 3:
        while index_col != 3:
            square_list[index_str][index_col] = (int(input(f"Число в строке {index_str + 1}  в столбце {index_show_col} : ")))
            index_col += 1
            index_show_col += 1
        index_str += 1
        index_col = 0
        index_show_col = 1

    one = square_list[0][0] + square_list[0][1] + square_list[0][2]
    two = square_list[1][0] + square_list[1][1] + square_list[1][2]
    three = square_list[2][0] + square_list[2][1] + square_list[2][2]
    top = square_list[2][0] + square_list[1][1] + square_list[0][2]
    down = square_list[0][0] + square_list[1][1] + square_list[2][2]

    if one == two == three == top == down:
        print("Это магический квадрат Ло Шу")
    else:
        print("Это НЕ магический квадрат Ло Шу")




main()





