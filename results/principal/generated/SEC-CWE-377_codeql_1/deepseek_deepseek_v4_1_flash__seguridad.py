from tempfile import NamedTemporaryFile


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    if not isinstance(results, str):
        raise TypeError("results must be a string")

    with NamedTemporaryFile(mode="w", encoding="utf-8", newline="", delete=False) as temp_file:
        temp_file.write(results)
        return temp_file.name
