import os
from PIL import Image

path = "/Users/simon/Documents/Developpement/65PassionMontagne/src/Controllers/data/Menu"


def reduce_image_size(path: str, width: int, height: int):
    try:
        folder = os.listdir(path)
        for file in folder:
            if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg'):
                print(file)
                image = Image.open(f"{path}/{file}")
                image.thumbnail((height, width), Image.LANCZOS)
                image.save(f"{path}/{file}")

        print("success")
    except Exception as e:
        print(f"Failed with message: {e}")


def delete_old_version(path_name):
    try:
        folders = os.listdir(path_name)
        for folder_name in folders:
            try:
                if folder_name != 'default.png':
                    folder = os.listdir(f"{path_name}/{folder_name}")
                    for file in folder:
                        if file.split(".")[0].isdigit() and f"c{file}" in folder:
                            os.remove(f"{path_name}/{folder_name}/{file}")
                            print(f"{path_name}/{folder_name}/{file}  -- Remove success")
            except Exception as e:
                print(f"Error in folder `{folder_name}`: ${e}")
    except Exception as e:
        print(f"Failed with message: {e}")


# reduce_image_size(path, 1000, 1000)