import math


def sort_matrix_by_row_sum(matrix):
    """
    Return a new matrix with the rows of `matrix` sorted in ascending
    order according to the sum of each row.

    The input matrix is not modified. Rows are returned as new lists.

    Raises:
        TypeError: if `matrix` is not a list/tuple of rows, if any row is
            not a list/tuple, or if any element is not an int or float.
        ValueError: if any element is NaN or infinite.
    """
    if not isinstance(matrix, (list, tuple)):
        raise TypeError("matrix must be a list of rows")

    validated_rows = []
    for i, row in enumerate(matrix):
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"row {i} must be a list or tuple of numbers")
        for j, value in enumerate(row):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    f"element at row {i}, column {j} must be int or float, "
                    f"got {type(value).__name__}"
                )
            if not math.isfinite(value):
                raise ValueError(
                    f"element at row {i}, column {j} must be finite, got {value!r}"
                )
        validated_rows.append(list(row))

    return sorted(validated_rows, key=sum)


if __name__ == "__main__":
    sample = [[1, 2, 3], [0, 0, 0], [10, -5, 1], [2, 2]]
    print(sort_matrix_by_row_sum(sample))
    # [[0, 0, 0], [2, 2], [1, 2, 3], [10, -5, 1]]
    print(sample)  # original matrix remains unchanged
