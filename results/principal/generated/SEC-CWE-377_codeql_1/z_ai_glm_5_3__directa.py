from tempfile import mktemp


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    filename = mktemp()
    with open(filename, 'w') as tmp_file:
        if isinstance(results, (list, tuple, set)):
            tmp_file.write('\n'.join(str(item) for item in results))
        else:
            tmp_file.write(str(results))
    return filename
