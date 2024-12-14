import os
from tkinter.filedialog import askopenfilename

from PIL import Image

path = askopenfilename(filetypes=[("gif", "*.gif")])
gif = Image.open(path)

frames = []
try:
    os.mkdir("tmp")
except:
    pass
for i in os.listdir('./tmp/'):
    os.remove(f"./tmp/{i}")
while True:
    gif.save(f"tmp/{gif.tell()}.png")
    if not gif.info.get("duration"):
        break
    try:
        gif.seek(gif.tell()+1)
    except EOFError:
        break

with open("output", "w") as f:
    f.write("")
with open("outputexe", "w") as f:
    f.write("")

pos = f"{input('x')}x{input('y')}x{input('z')}"
for item in (os.listdir("tmp")):
    os.system(f"python ./convert.py {os.path.dirname(__file__)+'/tmp/'+item} {os.path.basename(item).split('.')[0]} {pos} output {len(os.listdir('./tmp/'))}")

with open("outputexe", "r") as f:
    c = f.read().split("\n")
print(c)
tmp = []
for i in c:
    tmp.append(i.split(" "))
tmp.pop(-1)
print(tmp)
tmp.sort(key=lambda x:int(x[3]))
for i, j in enumerate(tmp):
    tmp[i] = " ".join(j)
with open("outputexe", "w") as f:
    f.write('\n'.join(tmp))