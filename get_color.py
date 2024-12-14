import json

from PIL import Image
import os

blocks = ['stone.png', 'cobblestone.png', 'deepslate.png']

color_dict = {}
if __name__ == '__main__':
    for block_path in os.listdir('block'):
        if block_path.endswith(('wool.png', 'terracotta.png', 'concrete.png', 'planks.png', '_wood.png', '_ore.png')) or block_path in blocks:
            image = Image.open('block/'+block_path)
            r = 0
            g = 0
            b = 0
            image.convert('RGB')
            for w in range(image.width):
                for h in range(image.height):
                    color = image.getpixel((w, h))
                    if len(color) > 3:
                        color = (color[0], color[1], color[2])
                    ir, ig, ib = color
                    r += ir
                    g += ig
                    b += ib
            count = image.width*image.height
            r /= count
            g /= count
            b /= count
            color_dict[block_path[0:-4]] = (r, g, b)

with open('color.json', 'w') as f:
    json.dump(color_dict, f)