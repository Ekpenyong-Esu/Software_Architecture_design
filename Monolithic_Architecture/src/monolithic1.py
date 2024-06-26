import os


class FileManagementSystem:
    """
    Monolithic Architecture styles to manage files in a directory.
    """

    def __init__(self):
        self.current_directory = os.getcwd()

    def list_files(self):
        files = os.listdir(self.current_directory)
        file_list = "\n".join(files)
        print(file_list)
        return file_list

    def create_file(self, filename):
        try:
            with open(os.path.join(self.current_directory, filename), "w"):
                pass
            print(f"File '{filename}' created successfully.")
            return True
        except Exception as e:
            print(f"Error creating file: {e}")
            return False

    def delete_file(self, filename):
        try:
            os.remove(os.path.join(self.current_directory, filename))
            print(f"File '{filename}' deleted successfully.")
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False

    def search_file(self, filename):
        files = os.listdir(self.current_directory)
        if filename in files:
            print(f"File '{filename}' found in directory.")
            return f"File '{filename}' found in directory."
        else:
            print(f"File '{filename}' not found in directory.")
            return f"File '{filename}' not found in directory."

    def change_directory(self, new_directory):
        try:
            os.chdir(new_directory)
            self.current_directory = new_directory
            print(f"Directory changed to '{new_directory}'.")
            return True
        except Exception as e:
            print(f"Error changing directory: {e}")
            return False


# Sample usage
if __name__ == "__main__":
    file_system = FileManagementSystem()

    while True:
        print("\nOptions:")
        print("1. List files")
        print("2. Create file")
        print("3. Delete file")
        print("4. Search for file")
        print("5. Change directory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_system.list_files()
        elif choice == "2":
            filename = input("Enter filename to create: ")
            file_system.create_file(filename)
        elif choice == "3":
            filename = input("Enter filename to delete: ")
            file_system.delete_file(filename)
        elif choice == "4":
            filename = input("Enter filename to search: ")
            file_system.search_file(filename)
        elif choice == "5":
            new_directory = input("Enter new directory: ")
            file_system.change_directory(new_directory)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
