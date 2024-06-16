import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
# from concurrent.futures import ThreadPoolExecutor
from joblib import Parallel, delayed
from PIL import Image
from wordcloud import WordCloud


def gen_frame(frame_name, word_text):
    # global words, prev_mask
    
    mask = np.array(Image.open("frames/" + frame_name))
    # if np.array_equal(mask, prev_mask):
    #     plt.savefg('wframes/' + frame)
    #     print(frame, 'is done from previous frame')
    #     return
    
    plt.figure(figsize=(9.6, 7.2))
    plt.subplots_adjust(0, 0, 1, 1)
    try:
        wc = WordCloud(width=960, height=720, background_color="white",
                       max_words=1000, mask=mask, contour_width=1,
                       scale=1, contour_color='white',
                       color_func=lambda word, font_size, position,
                                         orientation, random_state=None,
                                         **kwargs: "rgb(0, 0, 0)")
        wc.generate(word_text)
        plt.imshow(wc, interpolation='bilinear')
    except ValueError:
        shutil.copy('frames/' + frame_name, 'wframes')
        print('Empty file was processed')
        return
    
    plt.axis("off")
    plt.savefig('wframes/' + frame_name)
    # prev_mask = mask.copy()
    print(frame_name, 'is done')
    plt.close()


# for frame in os.listdir('frames')[1163:]:
#     gen_frame(frame)

# Initialize the executor
# with ThreadPoolExecutor() as executor:
#     # Process frames in parallel
#     futures = [executor.submit(gen_frame, frame, words, prev_mask)
#                for frame in os.listdir('frames')[1163:]]
#
#     # Wait for all tasks to complete
#     for future in futures:
#         future.result()

if __name__ == "__main__":
    words = open('chat_text.txt', 'r', encoding='utf-8').read()
    if not os.path.exists('wframes'):
        os.mkdir('wframes')

    plt.figure(figsize=(9.6, 7.2))
    # plt.subplots_adjust(0, 0, 1, 1)
    # prev_mask = np.array(Image.open("frames/output_0500.jpg"))

    Parallel(n_jobs=-1)(delayed(gen_frame)(frame, words)
                        for frame in os.listdir('frames'))
