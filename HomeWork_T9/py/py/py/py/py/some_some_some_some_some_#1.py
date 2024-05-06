
import os
import shutil

print("Операционная система:", os.name)

print("Текущая папка:", os.getcwd())

files_by_extension = {}

for file in os.listdir():

    _, extension = os.path.splitext(file)

    if extension:
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)

for extension, files in files_by_extension.items():

    folder_name = extension[1:]
    os.mkdir(folder_name)

    for file in files:
        shutil.move(file, os.path.join(folder_name, file))

    total_size = sum(os.path.getsize(os.path.join(folder_name, file)) for file in files)
    print(
        f"В папке с файлами {extension} перемещено {len(files)} файлов, их суммарный размер - "
        f"{total_size / (1024 * 1024):.2f} МБ")

for folder in os.listdir():
    if os.path.isdir(folder):
        files = os.listdir(folder)
        if files:
            file_to_rename = files[0]
            new_name = f"some_{file_to_rename}"
            os.rename(os.path.join(folder, file_to_rename), os.path.join(folder, new_name))
            print(f"Файл {file_to_rename} был переименован в {new_name}")