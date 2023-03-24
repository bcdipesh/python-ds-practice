def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # create a variable called total and initialize it to 0
    total = 0

    # loop over matrix from the start index
    for index in range(0, len(matrix)):
        # for each list inside matrix get the number diagonally and sum it with total
        total += matrix[index][index]

    # loop over each list inside the matrix
    for index in range(0, len(matrix)):
        # for each list reverse it
        matrix[index] = matrix[index][::-1]

    # loop over matrix from the start index
    for index in range(0, len(matrix)):
        # for each list inside matrix get the number diagonally and sum it with total
        total += matrix[index][index]

    # return total
    return total
