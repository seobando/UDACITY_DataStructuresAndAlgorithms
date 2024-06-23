import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_with_suffix = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                files_with_suffix.append(os.path.join(root, file))

    return files_with_suffix

# Test cases
## Note: You would need to adjust the paths based on your local file system to actually run these tests.

# Test Case 1: General case
print(find_files(".txt", "./testdir"))  # Adjust the path to your test directory

# Test Case 2: Edge case with no matching files
print(find_files(".xyz", "./testdir"))  # Adjust the path to your test directory

# Test Case 3: Edge case with an empty directory
print(find_files(".txt", "./empty_directory"))  # Adjust the path to your empty test directory

# Test Case 4: Edge case with a very large directory
# This case is more conceptual as creating a very large directory structure is impractical in a script
# but you can create a reasonably large structure and test.
# print(find_files(".txt", "./large_directory"))  # Adjust the path to your large test directory

# Additional tests to consider edge cases with null or non-existent paths
try:
    print(find_files(".txt", None))  # Should handle gracefully or raise a specific exception
except Exception as e:
    print(f"Handled exception: {e}")

try:
    print(find_files(".txt", "./non_existent_directory"))  # Should handle gracefully or raise a specific exception
except Exception as e:
    print(f"Handled exception: {e}")
