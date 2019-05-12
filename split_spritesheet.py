from PIL import Image

image = Image.open('sprite.png')
# print(image.size) # (695, 2144)
w, h = image.size
border = 5
size = 64
count = 1

cols = int(w / (border+size))
rows = int(h / (border+size))

for i in range(rows):
  for j in range(cols):
    xcoor_start = j * (size+border) + border
    ycoor_start = i * (size+border) + border
    xcoor_end = (j+1) * (size+border)
    ycoor_end = (i+1) * (border+size)
    image.crop((xcoor_start, ycoor_start, xcoor_end, ycoor_end)).save('img/{}.png'.format(count))
    # print(f"Created num {count}")
    count += 1