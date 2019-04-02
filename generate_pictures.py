import os
from PIL import Image

folders = [['esine', 'E'], ['hattu', 'H'], ['juoma', 'J'], ['vaate', 'V']]

count = 0
for folder, t in folders:
    for filename in os.listdir('assets/'+folder):
        print(filename)
        background = Image.open(os.path.join('assets', os.path.join(folder, filename)))
        background.save(os.path.join('result', os.path.join(folder, filename.replace(".", "0."))))
        count += 1

        for i in range(4):
            count += 1
            background = Image.open(os.path.join('assets', os.path.join(folder, filename)))
            foreground = Image.open(os.path.join('assets', os.path.join('sparkle', str(i) + t + '.png')))

            background.paste(foreground, (0, 0), foreground)
            background.save(os.path.join('result', os.path.join(folder, filename.replace(".", str(i+1) + "."))))

print(count)
