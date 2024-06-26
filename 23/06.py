from PIL import Image


def make_preview(size, n_colors):
    image = Image.open("./assets/image.jpg")
    image = image.resize(size)
    image = image.quantize(n_colors)
    image.save("res.bmp")


make_preview((400, 200), 64)