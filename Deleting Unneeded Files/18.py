import os
def del_unneeded(folder):
    # Walk the folder tree with os.walk() and search for files of more than 100MB using os.path.getsize()
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if os.path.getsize(full_path) > 100000000:
                print('Deleting {}...'.format(full_path))
                os.unlink(full_path)

del_unneeded('/Users/georgeghelase/delete')
print("Done")
