import json
import sys
import tqdm
import os
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

with open('color.json', 'r') as f:
    colors = json.load(f)
    keys = tuple(colors.keys())
    values = tuple(colors.values())

def calc(r, g, b):
    return [(r - i[0])**2 + (g - i[1])**2 + (b - i[2])**2 for i in values]

def get_block(r, g, b):
    var = calc(r, g, b)
    return keys[var.index(min(var))]

def img2mcfunction(image: Image.Image, pos: tuple[int, int, int], z, mx):
    commands = []
    if image.height > 128:
        image = image.resize((128, int(image.height*128/image.width)))
    if image.mode != 'RGB':
        temp = Image.new('RGB', image.size, (0, 0, 0))
        temp.paste(image)
        image = temp
    for i in tqdm.tqdm(range(image.width)):
        for j in range(image.height):
            color = image.getpixel((i, j))
            block = get_block(*color)
            commands.append(f'setblock {pos[0]+i} {pos[1]+image.height-j} {pos[2]+z} {block}')
    clone = f"clone {pos[0]} {pos[1]} {pos[2] + z} {pos[0] + image.width-1} {pos[1] - 1 + image.height} {pos[2] + z} {pos[0]} {pos[1]} {pos[2]+mx+1}"
    with open(f"{sys.argv[4]}exe", 'a') as f:
        f.write(f"{clone}\n")
    return commands


if __name__ == '__main__':
    """print(sys.argv)
    if len(sys.argv) == 0:
        path = askopenfilename()
        img = Image.open(path)
        with open('img.txt', 'w') as f:
            f.write('\n'.join(img2mcfunction(img, tuple([int(i) for i in input().split(' ')]), 0, 0))) 已弃用"""
    if len(sys.argv) == 6:
        img = Image.open(sys.argv[1])
        with open(sys.argv[4], 'a') as f:
            f.write('\n'.join(img2mcfunction(img, tuple([int(i) for i in sys.argv[3].split('x')]), int(sys.argv[2]), int(sys.argv[5]))))