from PIL import Image, ImageDraw


def main():
    for r in range(0, 256):
        print(f"Plotting layer {r}")
        img = Image.new('RGB', (2550, 2550), (255, 255, 255))
        for g in range(0, 256):
            for b in range(0, 256):
                print(f'\t({r:03d}, {g:03d}, {b:03d})')
                draw = ImageDraw.Draw(img)
                shape = [(b * 10, g * 10), (10 + b * 10, 10 + g * 10)]
                draw.rectangle(shape, fill=(r, g, b), outline=(0, 0, 0))

        img.save(fp=f"c:\\rgb_images\\layer_{r}.png", bitmap_format="png")


if __name__ == '__main__':
    main()
