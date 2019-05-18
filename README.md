## Python Scripts

```
python split_spritesheet.py -f "kanto_sprite.png" -r kanto
python split_sprite.py
python run.py
```

### Convert color
```
convert sample.png +dither -colors 5 sample_reduced_colors.png
```

### Resize
```
convert sample_2.png -filter point -resize 63 sample_2_small2.png
convert sample_2.png -sample 48x48  sample_2_small2.png

convert sample_2.png -adaptive-resize 48x48 sample_2_small.png
```

## Credits
Kanto Pokemon sprite image from [Spriters-Resource](https://www.spriters-resource.com/game_boy_advance/pokemonemerald/sheet/21230/)