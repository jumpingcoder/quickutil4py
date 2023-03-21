from collections.abc import Iterable
import os


def get_home_path():
    return os.environ['HOME']


def get_current_path():
    os.getcwd()


def file_exists(file_path: str):
    return os.path.exists(file_path)


def file_delete(file_path: str):
    if file_exists(file_path):
        os.remove(file_path)


def file_2_byte(file_path: str):
    with open(file_path, "rb") as file:
        return file.read()


def file_2_string(file_path: str):
    with open(file_path, "r") as file:
        return file.read()


def file_2_lines(file_path: str):
    with open(file_path, "r") as file:
        return file.readlines()


def byte_2_file(file_path: str, data: bytes):
    with open(file_path, "wb") as file:
        file.write(data)


def string_2_file(file_path: str, string: str, append: bool):
    write_type = "w"
    if append:
        write_type = "a"
    with open(file_path, write_type) as file:
        file.write(string)


def lines_2_file(file_path: str, lines: Iterable[str], append: bool):
    write_type = "w"
    if append:
        write_type = "a"
    with open(file_path, write_type) as file:
        for line in lines:
            file.write(line+'\n')
