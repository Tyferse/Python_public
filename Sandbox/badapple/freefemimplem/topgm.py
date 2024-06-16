import cv2
import numpy as np
import os
from PIL import Image


if not os.path.exists('mframes'):
    os.mkdir('mframes')

frames_dir = r"C:\Code\Python3\Sandbox#py\badapple\frames"
for frame in os.listdir(frames_dir)[45:]:
    image = Image.open(frames_dir + '\\' + frame)

    # grayscale_image = image.convert("L")

    pgm_path = frame.rsplit('.', 1)[0] + ".pgm"
    image = np.array(image)  # grayscale_image
    # print(image.shape)
    # image = cv2.copyMakeBorder(image, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    image = cv2.copyMakeBorder(image[:, :, 0], 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0.)

    Image.fromarray(image).save('mframes\\' + pgm_path)
    # grayscale_image.save('mframes\\' + pgm_path)

with open('flist.txt', 'w') as f:
    dr = os.listdir('mframes')
    f.write(str(len(dr)) + '\nmframes\\' + '\nmframes\\'.join(dr) + '\n')
