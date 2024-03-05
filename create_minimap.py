from capture_screenshot import capture_screenshot
import cv2
from PIL import Image
import time

def create_minimap():
    while True:
        screenshot = capture_screenshot()
        
        h, w, c = screenshot.shape
        minimap_ratio = 650 / 1080
        minimap_x = int(minimap_ratio * h)

        minimap_size = h - minimap_x
        minimap = screenshot[-minimap_size:, -minimap_size:]
        
        #im = Image.fromarray(minimap)
        #im.save('trialimage2.png')
        

        h, w, c = minimap.shape
        #print(minimap.shape)
        left = 0
        right = 0
        top = 0
        bottom = 0
        # 24/33/33
        for x in range(w):
            y = int(h / 2)
            r, g, b = minimap[y][x]
            print(r,g,b)
            if r == 24 and g == 33 and b == 33:
                left = x
                break

        for x in range(w - 1, 0, -1):
            y = int(h / 2)
            r, g, b = minimap[y][x]
            
            if r == 24 and g == 33 and b == 33:
                right = x
                break

        for y in range(h):
            x = int(w / 2)
            r, g, b = minimap[y][x]
            
            if r == 24 and g == 33 and b == 33:
                top = y
                break

        for y in range(h - 1, 0, -1):
            x = int(w / 2)
            r, g, b = minimap[y][x]
            
            if r == 24 and g == 33 and b == 33:
                bottom = y
                break
        
        print(left, right, top, bottom)
        minimap = minimap[top - 1:bottom + 1, left - 1:right + 1]

        h, w, c = minimap.shape
        if h == 0 or w == 0:
            print('Could not detect game map')
            continue

        minimap = cv2.resize(minimap, dsize=(256, 256), interpolation=cv2.INTER_LINEAR)
        im = Image.fromarray(minimap)
        #im.save('trialimage1.png')
        return im
        
#time.sleep(15)
#create_minimap()