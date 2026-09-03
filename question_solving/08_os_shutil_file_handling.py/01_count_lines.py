def count_line(filename):
    with open(filename) as f:
        return len(f.readlines())

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    try:
        total_lines = count_line(file_name)
        print(f"The file '{file_name}' has {total_lines} lines.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")