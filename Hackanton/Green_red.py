from PIL import Image


def change_pixels(image_path, image_output):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGB mode
    img_rgb = img.convert('RGB')

    width, height = img.size

    for y in range(0, height):
        for x in range(0, width):
            if img.getpixel((x, y)) >= 186:
                img_rgb.putpixel((x, y), (0,255, 0))

            if img.getpixel((x, y)) <= 100:
                img_rgb.putpixel((x, y), (255,0, 0))

    # Show the modified image
    img_rgb.show()

    # Save the modified image
    img_rgb.save('modified_image.png')


