from CleanFolders import ProcessImage as ps
import os
import datetime


def test_copy_action():
    source_path = '/Users/chetanshinde/Documents'
    destination_path = '/Users/chetanshinde/Documents/Photos/Test'
    folder_date = datetime.datetime.today().strftime('%Y-%m-%d')
    destination_path = destination_path + "/" + folder_date

    process = ps.ProcessImage(source_path, destination_path)

    for name, dirName in process.get_image_files():
        print(dirName)
        process.move_to_target(dirName + "/" + name)

    print(destination_path)

    no_of_copied = 0
    try:
        no_of_copied = len([f for f in os.listdir(destination_path) if os.path.isfile(os.path.join(destination_path, f))])
    except Exception as e:
        pass

    print("The number of copied images are ---- ",no_of_copied)
    assert no_of_copied == 3


if __name__ == '__main__':
    test_copy_action()