import matplotlib.pyplot as plt
import numpy as np
import os
from joblib import Parallel, delayed
from PIL import Image


def gen_wireframe(frame):
    image = Image.open("frames/" + frame)
    image = image.resize((image.width // 4, image.height // 4))
    pixels = np.array(image)
    image = pixels.copy() / 255

    # average_colors = []
    colors_array = np.zeros(image.shape[:2])
    for y in range(image.shape[1]):
        for x in range(image.shape[0]):
            colors_array[x, y] = sum(pixels[x, y]) // image.shape[2]
            # if isinstance(pixel_color, int):
            #     average_colors.append(pixel_color)
            # else:
                # average_colors.append(sum(pixel_color) // len(pixel_color))

    # colors_array = np.array(average_colors).reshape(image.shape[0], image.shape[1])
    # color_ratio = sum(1 for p in colors_array.flatten() if p >= 128) / (sum(1 for p in colors_array.flatten() if p < 128) + 0.1)

    X = np.linspace(-3, 3, image.shape[1])
    Y = np.linspace(-4, 4, image.shape[0])
    X, Y = np.meshgrid(X, Y)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    fig.set_size_inches((14.4, 10.8))

    ax.set_box_aspect([4,3,3])
    # ax.set_facecolor('white')
    # ax.autoscale(enable=True, axis='both')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.view_init(elev=90, azim=90)
    ax.dist = 6.9

    ax.set_axis_off()
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')

    # if color_ratio >= 1:
    ax.plot_wireframe(-X, Y, 255 - colors_array, color='black', rstride=4, cstride=3)
    # ax.plot_surface(-X, Y, 255 - colors_array, facecolors=image, rstride=4, cstride=4, antialiased=True)

    # plt.show()
    plt.savefig('wframes/' + frame)
    ax.clear()
    plt.close()

# gen_wireframe('output_1650.jpg')
Parallel(n_jobs=-1)(delayed(gen_wireframe)(frame) for frame in os.listdir('frames')[1:])
