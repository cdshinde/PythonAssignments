
"""
This is a simple class that will copy the files from the source to the destination folder.
We are copying the files to the destination folder that is date as the folder name.
So every time a copy is made, if it is a different day it will be copied to a new folder.

"""
import os
import shutil
import datetime


class ManageImages:

    def __init__(self, source_path, destination):
        print("This is the constructor method.")
        self.path = source_path
        self.destination = destination


    def get_image_files(self):
        """ get files of type images from the path """
        for dirName, subdirList, fileList in os.walk(self.path):
            if dirName == self.destination or dirName.startswith(self.destination):
                print("###### This is the same directory as the destination directory ######### " + dirName)
                continue
            if "apache" in dirName:
                print("##### This is a software no need to enter this directory ###### " + dirName)
                continue
            if dirName.endswith("numbers") or dirName.endswith("pages"):
                print("#### This is a mac based numbers app that has a preview jpg image that need not be copied #### "
                + dirName)
                continue
            # print('Found directory: %s' % dirName)
            for fname in fileList:
                # ignoring the png extension as they are images used by softwares
                if fname.lower().endswith(('.jpg', '.jpeg')):
                    yield fname, dirName

    def move_to_target(self, sourcefile):
        """
            move a file to the destination directory, check if error handling is required.
         """
        print('The destination folder is ', self.destination)
        try:
            if not os.path.exists(self.destination):
                os.makedirs(self.destination, exist_ok=True)
            if os.path.exists(self.destination):
                print("copying images")
                shutil.move(sourcefile, self.destination)
        except OSError:
            print("Catch Error, while creating file")



def main():

    source_path = '/Users/chetanshinde/Documents'
    destination_path = '/Users/chetanshinde/Documents/Photos'
    folder_date = datetime.datetime.today().strftime('%Y-%m-%d')
    destination_path = destination_path + "/" + folder_date

    process = ManageImages(source_path, destination_path)

    for name, dirName in process.get_image_files():
        print(dirName)
        process.move_to_target(dirName + "/" + name)


if __name__ == "__main__":
    main()


