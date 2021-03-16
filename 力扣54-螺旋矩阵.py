def spiralOrder(matrix):
    '''
    可以将矩阵看成若干层，首先输出最外层的元素，其次输出次外层的元素，直到输出最内层的元素。
    定义矩阵的第 kk 层是到最近边界距离为 kk 的所有顶点。例如，下图矩阵最外层元素都是第 11 层，次外层元素都是第 22 层，剩下的元素都是第 33 层。

    [[1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1]]

    时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是输入矩阵的行数和列数。矩阵中的每个元素都要被访问一次。

    空间复杂度：O(1)O(1)。除了输出数组以外，空间复杂度是常数。
    '''
    if not matrix:
        return list()
    # 定义矩阵的行数和列数
    rows, columns = len(matrix), len(matrix[0])
    # 申请4个节点，储存上下左右的4个边界
    left = 0
    right = columns - 1
    top = 0
    bottom = rows - 1
    # 初始化空列表，保存遍历的结果，用于输出
    res = []
    # 设定终止条件，开始遍历
    while left <= right and top <= bottom:
        # 遍历上
        for column in range(left, right + 1):
            res.append(matrix[top][column])
        # 遍历右
        for row in range(top + 1, bottom + 1):
            res.append(matrix[row][right])
        # 当有左右或者上下相等时，只剩一列，用上述的遍历
        if left < right and top < bottom:
            # 遍历下
            for column in range(right - 1, left, -1):
                res.append(matrix[bottom][column])
            # 遍历左
            for row in range(bottom, top, -1):
                res.append(matrix[row][left])
        # 设定遍历条件
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return res

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))