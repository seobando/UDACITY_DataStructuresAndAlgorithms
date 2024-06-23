Explanation of the implementation:

- The find_files function takes two arguments: suffix and path.
- It initializes an empty list files_with_suffix to store the paths of files that match the suffix.
- Using os.walk, it traverses the directory tree starting from the given path. os.walk returns three values: the current directory path (root), the directories in the current directory (dirs), and the files in the current directory (files).
- For each file in the files list, it checks if the file name ends with the given suffix. If it does, it constructs the full file path using os.path.join(root, file) and appends it to the files_with_suffix list.
- Finally, it returns the list of files with the specified suffix.