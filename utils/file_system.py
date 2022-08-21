import shutil
from pathlib import Path


def remove_directory(path_to_remove: Path) -> None:
    """Remove a directory and all its contents.

    Args:
        path_to_remove (Path): The path to the directory to remove.
    """
    shutil.rmtree(path_to_remove)


def find_files_by_suffix(path_to_find_from: Path, file_suffix: str) -> list:
    """Find files of a directory by their file suffix.

    Args:
        path_to_find_from (Path): The path to find files from.
        file_suffix (str): The extension of the file.

    Returns:
        list: A list of files path.
    """
    return list(path_to_find_from.glob(f"*.{file_suffix}"))


def get_filename_without_suffix(file_path: Path) -> str:
    """Get the filename of a file without its suffix.

    Args:
        file_path (Path): The path of the file.

    Returns:
        str: A string showing the filename.
    """
    return file_path.stem


def get_filename_with_suffix(file_path: Path) -> str:
    """Get the filename of a file and its suffix.

    Args:
        file_path (Path): The path of the file.

    Returns:
        str: A string showing the filename and the suffix.
    """
    return file_path.name
