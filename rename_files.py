import os


def rename_files():

    # get all file name from folder

        folder = os.listdir(r"/Users/apexa/Desktop/Python Basic/img")

        # r is stands for rawpack,it tells python "hey take this string as it is
        # and dont interpret it any other way

        print folder


    # cwd for current working directory

        save_path = os.getcwd()

        print 'my current working directory' + save_path

    # chdir stands for change directory

        os.chdir(r"/Users/apexa/Desktop/Python Basic/img")

      # rename all file from folder

        for file_name in folder:
            print 'old name -' + file_name
            print 'new name -' + file_name.translate(None, '0123456789')

            # rename the file list

            os.rename(file_name, file_name.translate(None, '0123456789'))

            # return to my original path

        os.chdir(save_path)
rename_files()

			
