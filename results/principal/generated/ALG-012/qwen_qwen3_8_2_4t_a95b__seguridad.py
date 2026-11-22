import math

def sort_matrix_by_row_sum(matrix):
    if not isinstance(matrix, (list, tuple)):
        raise TypeError("matrix must be a list or tuple")

    rows_with_sums = []

    for row_index, row in enumerate(matrix):
        if not isinstance(row, (list, tuple)):
            raise TypeError("each matrix row must be a list or tuple")

        row_sum = 0

        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("matrix elements must be integers or floats")

            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError("matrix elements must be finite")

            row_sum += value

        row_copy = list(row) if isinstance(row, list) else tuple(row)
        rows_with_sums.append((row_sum, row_index, row_copy))

    rows_with_sums.sort(key=lambda item: (item[0], item[1]))

    return [row for _, _, row in rows_with_sums]

sort_matrix = sort_matrix_by_row_sum
