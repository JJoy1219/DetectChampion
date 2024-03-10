from capture_screenshot import capture_screenshot
import cv2
from PIL import Image
import time

def create_minimap(minimap_scale):
    while True:
        screenshot = capture_screenshot()
        #875/1080 at 0.0 minimap scale
        #670/1080 at 3.0 minimap scale
        base_minimap_size = 0.185
        h, w, c = screenshot.shape
        minimap_ratio = base_minimap_size * ((minimap_scale/3)+1)

        minimap_size = int(minimap_ratio * h)
        minimap = screenshot[-minimap_size:, -minimap_size:]
        
        minimap = cv2.resize(minimap, dsize=(256, 256), interpolation=cv2.INTER_LINEAR)
        im = Image.fromarray(minimap)
        
        return im
        
