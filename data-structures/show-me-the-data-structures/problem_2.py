import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []
        
    if not os.path.isdir(path):
        return []
    
    result: list[str] = []
    for fileOrFoler in os.listdir(path):
        filepath = os.path.join(path, fileOrFoler)
        if os.path.isfile(filepath) and fileOrFoler.endswith(suffix):
            result += [filepath] 
        elif os.path.isdir(filepath):
            result += find_files(suffix, filepath) 

    return result




if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
    assert set(result) == set(['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c'])

    # Test Case 2
    # test folder that doesnt' exist
    result = find_files(".c", "nope")
    assert result == []

    # Test Case 3
    result = find_files(".h", "./testdir")
    assert set(result) == set(['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h','./testdir/t1.h'])

    # Test case 4
    result = find_files(".c",'./testdir/subdir1/a.c')
    assert result == ['./testdir/subdir1/a.c']

    # test case 5
    result = find_files(".c", "./testdir/subdir1/a.h")
    assert result == []