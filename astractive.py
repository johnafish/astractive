from PIL import Image 

TRANSPARENT = (0, 0, 0, 0)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
INK = (165, 6, 39, 255)
INK2 = (50, 155, 199, 255)

study = Image.open("images/bg.png")
result = Image.new("RGBA", study.size)

study_data = study.getdata()
res_data = []

for pixel in study_data:
    pix_sum = sum(pixel[:-1])
    threshold = 450
    if pix_sum > threshold:
        # Highlights
        res_data.append(INK2)
    elif pix_sum > 100:
        # Shadows
        res_data.append(INK)
    else:
        res_data.append(INK2)

result.putdata(res_data)
result.show()
result.save("images/bg_print.png")
