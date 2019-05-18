from PIL import Image
import os

## Save in '001/v1/001_01.png' format
def filepath_to_save(original_path, part):
  path_array = original_path.split("/")
  serial_no = path_array[-1].split(".")[0]
  final_path = '/'.join(path_array[:-1])
  final_path += f'/{serial_no}_{str(part).zfill(2)}.png'
  return final_path

import subprocess

## Convert image to one with fewer colors
def convert_image_colors(filename):
  command = f'cp {filename} {filename[:-4]}_original.png'
  subprocess.run(command.split(" "))
  command = f'convert {filename[:-4]}_original.png +dither -colors 5 {filename}'
  subprocess.run(command.split(" "))

## Crop image into 8x16 chunks and save them
def main(filename):
  image = Image.open(filename)
  w, h = image.size #(64, 64)
  size_x = 8
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

      cropped_image = image.crop((xcoor_start, ycoor_start, xcoor_end, ycoor_end))
      cropped_image.save(filepath_to_save(filename, count))
      count += 1

if __name__ == "__main__":
  sprite_dir = os.path.join(os.getcwd(), "sprites/kanto")

  for serial_no in os.listdir(sprite_dir):
    serial_no_dir = os.path.join(sprite_dir, serial_no)

    for i in range(1, 3):
      indiv_image_dir = os.path.join(serial_no_dir, f'v{i}')
      image_path = os.path.join(indiv_image_dir, os.listdir(indiv_image_dir)[0])
      convert_image_colors(image_path)
      main(image_path)