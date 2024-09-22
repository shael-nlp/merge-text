import os

# --- Settings ---
output_file_name = "OUTPUT_FILE.txt"
file_encoding = "utf-8"
# --- Settings ---


def merging_txt_files(output_file, encoding):
    files = os.listdir()
    # checking if it is an actual txt file and not a directory named .txt or anything else
    txt_files = [f for f in files if f.endswith('.txt') and os.path.isfile(f)]

    if not txt_files or len(txt_files) == 1:
        print("Not enough text files found... Is 'merge-txt.py' in the right directory ?")
        input("Press 'Enter' to quit ...")
        return 0

    txt_files.sort()

    with open(output_file, 'w', encoding=encoding) as output_file:
        for f in txt_files:
            with open(f, 'r', encoding=encoding) as readfile:
                output_file.write(readfile.read())
                output_file.write(' ')

    print(f"Successfully merged {len(txt_files)} files into '{output_file.name}'.")
    input("Press 'Enter' to quit ...")
    return 1


merging_txt_files(output_file_name, file_encoding)
