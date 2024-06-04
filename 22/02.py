from PIL import Image

image = Image.open('./assets/p_22_01.jpg')

w, h = image.size

r_values = []
g_values = []
b_values = []

for x in range(w):
    for y in range(h):
        r, g, b = image.getpixel((x, y))
        r_values.append(r)
        g_values.append(g)
        b_values.append(b)

avr_r = sum(r_values) // len(r_values)
avr_g = sum(g_values) // len(g_values)
avr_b = sum(b_values) // len(b_values)

print(' '.join(str(x) for x in [avr_r, avr_g, avr_b]))