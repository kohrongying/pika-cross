from PIL import Image
import os
import json

def rgb_to_hex(rgb):
  return '%02x%02x%02x' % rgb

def main(filename):
  image = Image.open(filename)

  w, h = image.size # (32, 16)
  pixels = image.convert('RGB')

  # get color counts per col and per row
  cols = [{} for i in range(w)]
  rows = [{} for j in range(h)]
  seenColors = []

  for i in range(w):
    for j in range(h):
      rgb = pixels.getpixel((i,j))
      hex = rgb_to_hex(rgb)

      hex = rgb_to_hex(rgb)
      if hex not in seenColors: 
        seenColors.append(hex)
      
      if hex in cols[i]:
        cols[i][hex]["count"] += 1
        if j - cols[i][hex]["lastIndex"] != 1:
          cols[i][hex]["consec"] = "False"
        cols[i][hex]["lastIndex"] = j
      else: 
        cols[i][hex] = {
          "count": 1,
          "lastIndex": j,
          "consec": "True"
        }

  for i in range(h):
    for j in range(w):
      rgb = pixels.getpixel((j,i))
      hex = rgb_to_hex(rgb)
      
      if hex in rows[i]:
        rows[i][hex]["count"] += 1
        if j - rows[i][hex]["lastIndex"] != 1:
          rows[i][hex]["consec"] = "False"
        rows[i][hex]["lastIndex"] = j
      else: 
        rows[i][hex] = {
          "count": 1,
          "lastIndex": j,
          "consec": "True"
        }

  sample = {"rows": rows, "cols": cols, "uniqColors": seenColors}
  
  path, ext = filename.split('.')
  with open(f'{path}.json', 'w') as fp:
    json.dump(sample, fp)

if __name__ == "__main__":
  sprite_dir = os.path.join(os.getcwd(), "sprites/kanto")

  # Loop through all pokemons
  for serial_no in os.listdir(sprite_dir):
    serial_no_dir = os.path.join(sprite_dir, serial_no)

    # Loop through 2 different versions
    for i in range(1, 3):
      indiv_image_dir = os.path.join(serial_no_dir, f'v{i}')

      # Loop through 32 different cropped parts
      for png in os.listdir(indiv_image_dir):
        image_path = os.path.join(indiv_image_dir, png)
        main(image_path)
