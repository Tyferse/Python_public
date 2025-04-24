import os
from PIL import Image


def sticker_convert(file):
    try:
        image = Image.open(file)
        image = image.convert("RGBA")
    except PermissionError:
        return
    
    width_ratio = 512 / image.width
    height_ratio = 512 / image.height
    if width_ratio < height_ratio:
        # Изменяем размер изображения по ширине
        new_size = (512, int(image.height * width_ratio))
        print(new_size)
        height_diff = 512 - new_size[1]
        
        # Создаем новое изображение с нужным размером и прозрачным фоном
        expanded_image = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        expanded_image.paste(image.resize(new_size), (0, height_diff // 2))
    else:
        # Изменяем размер изображения по высоте
        new_size = (int(image.width * height_ratio), 512)
        width_diff = 512 - new_size[0]
        
        # Создаем новое изображение с нужным размером и прозрачным фоном
        expanded_image = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        expanded_image.paste(image.resize(new_size), (width_diff // 2, 0))
    
    if not os.path.exists(file.rsplit('/', 1)[0] + "/converted_stickers"):
        os.mkdir(file.rsplit('/', 1)[0] + "/converted_stickers")
    
    expanded_image.save(file.rsplit('/', 1)[0] + "/converted_stickers/"
                        + file.rsplit('/', 1)[1].split('.', 1)[0] + "s.png")


sticker_dir = r"/for stickers"
for stick in os.listdir(sticker_dir):
    if not os.path.exists(sticker_dir + "/converted_stickers/"
                          + stick.split('.', 1)[0] + "s.png"):
        sticker_convert(sticker_dir + "/" + stick)
