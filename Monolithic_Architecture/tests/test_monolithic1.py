import os

import pytest

from src.monolithic1 import FileManagementSystem


@pytest.fixture
def file_system():
    return FileManagementSystem()


def test_create_file(file_system):
    filename = "test_file.txt"
    file_system.create_file(filename)
    assert os.path.exists(filename)


def test_delete_file(file_system):
    filename = "test_file.txt"
    file_system.create_file(filename)
    file_system.delete_file(filename)
    assert not os.path.exists(filename)


def test_search_file_existing(file_system):
    filename = "test_file.txt"
    file_system.create_file(filename)
    # fmt: off
    assert (
            file_system.search_file(filename) ==
            f"File '{filename}' found in directory."
    )
    # fmt: on


def test_search_file_non_existing(file_system):
    filename = "non_existing_file.txt"
    # fmt: off
    assert (
            file_system.search_file(filename) ==
            f"File '{filename}' not found in directory."
    )
    # fmt: on


def test_change_directory(file_system):
    new_directory = "test_directory"
    try:
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
        file_system.change_directory(new_directory)
        assert file_system.current_directory == new_directory
    finally:
        # Clean up the directory if it was created during the test
        if os.path.exists(new_directory):
            os.rmdir(new_directory)


def test_list_files(file_system, capsys):
    file_system.list_files()
    captured = capsys.readouterr()

    # fmt: off
    assert (
            captured.out ==
            "\n".join(os.listdir(file_system.current_directory)) + "\n"
    )
    # fmt: on
