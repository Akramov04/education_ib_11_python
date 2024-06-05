from PIL import Image


def transparency(filename1, filename2):
    im_1 = Image.open(filename1)
    im_2 = Image.open(filename2)
    pixel_1 = im_1.load()
    pixel_2 = im_2.load()
    x, y = im_1.size
    for i in range(x):
        for j in range(y):
            r_1, g_1, b_1 = pixel_1[i, j]
            r_2, g_2, b_2 = pixel_2[i, j]
            red = int(0.5 * r_1 + 0.5 * r_2)
            green = int(0.5 * g_1 + 0.5 * g_2)
            blue = int(0.5 * b_1 + 0.5 * b_2)
            pixel_1[i, j] = red, green, blue
    im_1.save('res.jpg')


