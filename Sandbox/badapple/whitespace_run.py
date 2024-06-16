from PIL import Image
import numpy as np
import os
import time
# from selenium.common import exceptions
from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By


driver = Chrome(r"C:\Users\Jrytoeku Qtuhtc\.wdm\drivers\chromedriver"
                r"\win64\124.0.6367.155\chromedriver.exe")
driver.get("https://ideone.com/GUkbgR")
for frame in os.listdir('frames')[1:]:
    start = time.time()
    print(frame)
    img = Image.open('frames/' + frame)
    img = np.array(img.resize((2*img.height, img.height)))
    # print(img[0])
    # print(img.shape)
    # Image.fromarray(img).save('pretest.jpg')
    new_img = np.zeros((26, 52))
    h = img.shape[0] // 26
    for y in range(new_img.shape[0]):
        for x in range(new_img.shape[1]):
            if img[y*h:(y + 1)*h,
                   x*h:(x + 1)*h].mean() > 127:
                new_img[y, x] = 1
    
    # print(new_img)
    # Image.fromarray(new_img * 255, mode='L').save('test.jpg')
    
    wscode = ''
    for y in range(new_img.shape[0]):
        wscode += '<li class="li1"><div class="de1">'
        for x in range(new_img.shape[1]):
            if x % 2 == 1 and new_img[y, x-1] == 1:
                continue
            
            if new_img[y, x] == 0 and x % 2 == 0:
                wscode += '<span class="re3">\t</span>'
            # elif x > 0 and new_img[y, x-1] == 0 and x % 2 == 0:
            #     continue
            elif new_img[y, x] == 1:
                wscode += '<span class="re2">  '
                wscode += '  </span>' if x % 2 == 0 else '</span>'
        
        wscode += '</div></li>'

    driver.execute_script('document.querySelector'
                          '("#source > pre > ol").innerHTML = '
                          'arguments[0];', wscode)
    end = time.time()
    time.sleep(end - start if end - start < 1/40 else 0.)


# driver.quit()
