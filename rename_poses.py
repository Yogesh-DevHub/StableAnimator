import os

def rename_images(folder_path):
    files = os.listdir(folder_path)
    png_files = [f for f in files if f.endswith('.png')]
    index_number = 0
    for index, filename in enumerate(png_files):
        if index_number != 0:
            index_number += 1
            new_name = f'frame_{index_number}.png'
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')
            continue
        
        new_name = f'frame_{index}.png'
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} to {new_file}')


folder_path = './rename_poses'
rename_images(folder_path)