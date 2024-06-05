from PIL import Image, ImageFilter


def motion_blur(n):
    image = Image.open("./assets/image.jpg")
    image = image.rotate(270, expand=True)
    filtered = image.filter(ImageFilter.GaussianBlur(radius=n))
    filtered.save("res_2.jpg")


motion_blur(10)