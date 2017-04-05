import os


def rename_files():

# get all file name from folder

    file_list = os.listdir(r"/Users/apexa/Desktop/Python Basic/img")
    print file_list


save_path = os.getcwd()
print 'my current working directory' + save_path
os.chdir(r"/Users/apexa/Desktop/Python Basic/img")

  # rename all file from folder

for file_name in file_list:
    os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)
    rename_files()
