with open("./test_input.txt", "r") as f:
    matrix = [[int(n) for n in list(line)] for line in f.read().split("\n")]

    #
    # constant visible_trees: 2 * len(matrix) + 2 * len(matrix[0]) - 4
    #
    # iteration table:
    # checking     | outer loop             | inner loop             | access
    # -------------|------------------------|------------------------|--------------
    # top->bottom: | i = 1                  | j = 1                  | matrix[j][i]
    # -------------|------------------------|------------------------|--------------
    # left->right: | i = 1                  | j = 1                  | matrix[i][j]
    # -------------|------------------------|------------------------|--------------
    # right->left: | i = 1                  | j = len(matrix[0]) - 2 | matrix[i][j]
    # -------------|------------------------|------------------------|--------------
    # bottom->top: | i = len(matrix[0]) - 2 | j = 1                  | matrix[j][i]
    #

    
