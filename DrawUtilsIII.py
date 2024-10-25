from PIL import Image, ImageDraw, ImageFont

# 定义字符集
ASCII_CHARS = "@%#*+=-:.  "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # 调整高度来适应字符的比例
    new_height = int(new_width * ratio)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayify(image):
    return image.convert("L")  # 转换为灰度图像

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    colors = []  # 存储每个字符的颜色

    for pixel in pixels:
        ascii_char = ASCII_CHARS[pixel // 25]  # 将像素值映射到字符
        ascii_str += ascii_char
        colors.append(pixel)  # 存储对应的像素颜色

    return ascii_str, colors

def ascii_to_image(ascii_str, colors, font_size=10):
    width = len(ascii_str.split('\n')[0]) * font_size / 1.5
    height = len(ascii_str.split('\n')) * font_size * 1.5
    width = int(width)
    height = int(height)
    image = Image.new('RGB', (width, height), (255, 255, 255))

    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)  # 提供应使用的字体文件路径
    except IOError:
        font = ImageFont.load_default()

    # 绘制文本时使用对应的颜色
    for i, (char, color) in enumerate(zip(ascii_str, colors)):
        x = (i % (width // font_size)) * font_size / 1.5
        y = (i // (width // font_size)) * font_size * 1.5
        draw.text((x, y), char, fill=color, font=font)

    return image

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"无法打开图像文件: {e}")
        return
    
    image = resize_image(image, new_width)
    image_gray = grayify(image)

    ascii_str, colors = pixels_to_ascii(image_gray)
    img_width = image_gray.width

    # 将字符分行
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    return ascii_to_image(ascii_img, colors)

if __name__ == "__main__":
        output_image = main('a.jpg')
        output_image.save("result_ascii_art.jpg")
        print("保存结果为 'result_ascii_art.jpg'")

