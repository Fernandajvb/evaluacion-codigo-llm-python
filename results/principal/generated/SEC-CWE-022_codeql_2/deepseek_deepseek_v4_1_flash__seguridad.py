import os
import shutil
import tarfile

def extract_tar(file_name):
    base_dir = '/tmp'
    os.makedirs(base_dir, exist_ok=True)
    base_real = os.path.realpath(base_dir)
    with tarfile.open(file_name, 'r:*') as tar:
        for member in tar.getmembers():
            name = member.name
            if not name or '\0' in name:
                continue
            if os.path.isabs(name):
                raise ValueError(f"Absolute path not allowed: {name}")
            normalized = os.path.normpath(name)
            if normalized.startswith('..') or normalized == '..' or os.path.isabs(normalized):
                raise ValueError(f"Path traversal not allowed: {name}")
            target = os.path.join(base_dir, normalized)
            target_real = os.path.realpath(target)
            if os.path.commonpath([base_real, target_real]) != base_real:
                raise ValueError(f"Path outside base directory: {name}")
            if member.isdir():
                os.makedirs(target, exist_ok=True)
            elif member.isfile():
                os.makedirs(os.path.dirname(target), exist_ok=True)
                src = tar.extractfile(member)
                if src is not None:
                    with src, open(target, 'wb') as dst:
                        shutil.copyfileobj(src, dst)
            else:
                raise ValueError(f"Unsupported file type: {name}")
