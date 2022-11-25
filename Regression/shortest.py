def getValue(m):
    pathInfo = [[]]

    pathInfo[1][2] = 4
    pathInfo[1][3] = 2
    pathInfo[1][4] = 3

    pathInfo[2][5] = 9
    pathInfo[2][6] = 8

    pathInfo[3][5] = 6
    pathInfo[3][6] = 7
    pathInfo[3][7] = 8
    pathInfo[3][8] = 7

    pathInfo[4][6] = 4
    pathInfo[4][7] = 7

    pathInfo[5][8] = 5
    pathInfo[5][9] = 6

    pathInfo[6][8] = 8
    pathInfo[6][9] = 6

    pathInfo[7][8] = 6
    pathInfo[7][9] = 5

    pathInfo[8][10] = 7
    pathInfo[9][10] = 3

    if m == 2: return pathInfo[1][2]
    if m == 3: return pathInfo[1][3]
    if m == 4: return pathInfo[1][4]
