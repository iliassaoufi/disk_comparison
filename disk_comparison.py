import os
import numpy as np


def scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(scandir(dirname))

    return subfolders


def scanfile(path, main_path):
    files = []

    for file in os.listdir(path):
        files.append(os.path.join(path.replace(main_path, ""), file))

    return files


def get_all_path(main_path):
    list_sub_path = scandir(main_path)
    list_sub_path.append(main_path)

    list_file = []
    for path in list_sub_path:
        list_file.extend(scanfile(path, main_path))

    nbr_sub_dir = len(list_sub_path)-1

    return list_file, nbr_sub_dir


def write_file(file_name, file_content):
    try:
        file = open(file_name, "w+")
        content = str(file_content)
        file.write(content)
        file.close()
    except Exception as e:
        print("The error is: ", e)


def get_result_difference(path1, path2):
    try:

        result1, nbr_sub_dir1 = get_all_path(path1)
        result2, nbr_sub_dir2 = get_all_path(path2)

        difference1 = np.setdiff1d(result1, result2)
        difference2 = np.setdiff1d(result2, result1)

        # dir1 = path1.split("\\")[-1]
        # difference = []
        # difference = [np.concatenate((difference1, difference2))][0]

        print("The results are ready")

        file = open("scan.txt", "w+", encoding="utf-8")

        txt = f"Disk1 path => {path1}\n"
        txt += f"Disk2 path => {path2}\n"
        txt += "\n--------------\n"
        txt += f"\nNumbre of dolders: \t disk1 => {
            nbr_sub_dir1} \t disk2 => {nbr_sub_dir2} \n"
        txt += f"\nNumbre of files: \t disk1 => {len(result1) - nbr_sub_dir1} \t disk2 => {
            len(result2) - nbr_sub_dir2} \n"
        txt += f"\nTotal: \n - disk1 => {len(result1)} \n - disk2 => {
            len(result2)}\n"
        txt += "\n--------------\n\n"
        file.writelines(txt)

        if len(difference1) == 0 and len(difference2) == 0:
            file.writelines("All folders and files are on both disks")

        if len(difference1) > 0:
            file.writelines(
                "Folders and files on disk1 are not on disk2: \n\n")

            for i in difference1:
                file.writelines(str("- "+path1 + " => " + i + "\n"))

            file.writelines("\n--------------\n\n")

        if len(difference2) > 0:
            file.writelines(
                "Folders and files on disk2 are not on disk1: \n\n")

            for i in difference2:
                file.writelines(str("- "+path2 + " => " + i + "\n"))

        file.close()
        print("Done, go to scan.text")
    except Exception as e:
        print("error : ", e)
        write_file("error.txt", e)


if __name__ == "__main__":

    path1 = input("Please enter first disk path : ")
    print(path1)
    path2 = input("Please enter secend disk path : ")
    print(path2)

    if path1 and path2:
        get_result_difference(str(path1), str(path2))
    else:
        print(
            f"error: check arguments \n\t--disk1 => {path1} \n\t--disk2 => {path2}")

    os.system("pause")

    # import argparse
    # parser = argparse.ArgumentParser(description="Simple Python script for ")
    # parser.add_argument("-d1", "--disk1")
    # parser.add_argument("-d2", "--disk2")
    # args = parser.parse_args()

    # if args.disk1 and args.disk2:
    #     get_result_difference(str(args.disk1), str(args.disk2))
    # else:
    #     print(
    #         f"error: check arguments \n\t--disk1 => {args.disk1} \n\t--disk2 => {args.disk2}")
