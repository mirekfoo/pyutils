import os
import shutil

"""File operations utilities."""

def fbak(filename: str, archive_subdir: str = None, copy: bool = False) -> None:
    """If the file exists, create a backup copy of a file by appending '-i' to its name (before extension).
        If filename-i.ext already exists, increment i until an unused filename is found.
        If archive_subdir short name is provided:
            create such subdir in the directory of the file (if not exists already),
            put the buckup file into the subdir.
    """
    if not os.path.exists(filename):
        return
    
    base, ext = os.path.splitext(filename)
    i = 1
    while True:
        backup_name = f"{base}-{i}{ext}"
        if archive_subdir:
            dir_name = os.path.dirname(filename)
            archive_dir = os.path.join(dir_name, archive_subdir)
            os.makedirs(archive_dir, exist_ok=True)
            backup_name = os.path.join(archive_dir, os.path.basename(backup_name))
        if not os.path.exists(backup_name):
            break
        i += 1

    if copy:
        shutil.copyfile(filename, backup_name)
    else:
        os.rename(filename, backup_name)
