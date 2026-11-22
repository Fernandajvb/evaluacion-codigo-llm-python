import tarfile

def extract_tar(file_name):
    with tarfile.open(file_name) as tar:
        for member in tar:
            tar.extract(member, path='/tmp/')
