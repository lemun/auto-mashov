import os

class Remove:
    def img():
        folder_path = (r"./img/")
        test = os.listdir(folder_path)
        for images in test:
            if images.endswith(".png"):
                os.remove(os.path.join(folder_path, images))

