from PIL import Image

image = Image.open('sample.png')
# print(image.size) # (64, 64)
w, h = image.size
size_x = 32
size_y = 16

cols = int(w / size_x)
rows = int(h / size_y)

count = 1
for i in range(rows):
  for j in range(cols):
    xcoor_start = j * size_x
    ycoor_start = i * size_y
    xcoor_end = (j+1) * size_x
    ycoor_end = (i+1) * size_y
    image.crop((xcoor_start, ycoor_start, xcoor_end, ycoor_end)).save('{}.png'.format(count))
    # print(f"Created num {count}")
    count += 1
