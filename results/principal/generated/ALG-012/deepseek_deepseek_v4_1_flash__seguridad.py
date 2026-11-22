from numbers import Real

def sort_matrix_by_row_sum(matrix):
    if not isinstance(matrix, (list, tuple)):
        raise TypeError("matrix must be a list or tuple of rows")
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError("each row must be a list or tuple")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError("matrix elements must be real numbers")
    return sorted(matrix, key=sum)

sort_matrix = sort_matrix_by_row_sum
