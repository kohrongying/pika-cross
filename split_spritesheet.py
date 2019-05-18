from PIL import Image
import argparse
import os 
import math

def create_output_dest_if_not_found(out):
  path = os.path.join(os.getcwd(), out)
  if not os.path.exists(path) and not os.path.isdir(path):
    os.makedirs(path)

def main(params):
  filepath = params['filepath']
  region = params['region']

  image = Image.open(filepath)
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
      cropped_image = image.crop((xcoor_start, ycoor_start, xcoor_end, ycoor_end))

      serial_no = math.ceil(count/2)
      if count % 2 == 0: # if even
        version = 'v2'
      else:
        version = 'v1'

      serial_no = str(serial_no)
      filepath_to_save = f'sprites/{region}/{serial_no.zfill(3)}/{version}'
      create_output_dest_if_not_found(filepath_to_save)

      cropped_image.save(f'{filepath_to_save}/{serial_no.zfill(3)}.png')
      
      count += 1


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  
  parser.add_argument('-f','--file', dest='filepath', type=str, help='path of the sprite file to split')
  
  parser.add_argument('-r','--region', dest='region', type=str, help='pokemon region')

  args = parser.parse_args()
  params = vars(args)

  main(params)