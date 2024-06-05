from PIL import Image


def twist_image(input_file_name, output_file_name):
    image = Image.open(input_file_name)
    pixel = image.load()
    x, y = image.size
    for i in range(x // 2):
        for j in range(y):
            pixel[(x // 2 + i), j], pixel[i, j] = pixel[i, j], pixel[(x // 2 + i), j]
    image.save(output_file_name)

