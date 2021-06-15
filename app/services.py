from typing import List
import os
import random
import time
import fastapi


def get_image_filenames(directory_name: str) -> List[str]:
    return os.listdir(directory_name)


def select_random_image(directory_name: str) -> str:
    images = get_image_filenames(directory_name)
    random_image = random.choice(images)
    path = f"{directory_name}/{random_image}"
    return path


def _is_image(filename: str):
    valid_extensions = (".png", ".jpg", ".jpeg", ".gif")
    return filename.endswith(valid_extensions)


def upload_image(directory_name: str, image: fastapi.UploadFile):
    if _is_image(image.filename):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        image_name = timestr + image.filename.replace(" ", "-")
        with open(f"{directory_name}/{image_name}", "wb+") as image_upload:
            image_upload.write(image.file.read())

        return f"{directory_name}/{image_name}"
    return None
