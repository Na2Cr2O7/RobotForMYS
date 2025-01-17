from PIL import Image,ImageDraw,ImageFont,ImageEnhance
import CopyTest
# 定义字符集
ASCII_CHARS = "@%#*+=-:.  "
def enhance_contrast(image, factor=3):
    """
    提高图像的对比度
    :param image: 输入的图像
    :param factor: 对比度增强因子，1.0表示无变化，<1.0表示降低对比度，>1.0表示增强对比度
    :return: 对比度增强后的图像
    """
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(factor)
    return enhanced_image

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
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  # 将像素值映射到字符
    return ascii_str
def asciiToImage(ascii_str,font_size=10):
    width=len(ascii_str.split('\n')[0])*font_size/1.5
    height=len(ascii_str.split('\n'))*font_size*1.5
    width=int(width)
    height=int(height)
    image = Image.new('RGB', (width, height), (255, 255, 255))

    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)  # 你可能需要提供字体文件的路径
    except IOError:
        font = ImageFont.load_default()   
    draw.text((0, 0), ascii_str, fill="black", font=font)
    return image
def saveImage(image,filename='result.jpg'):
    image.save(filename)
def main(image_path, new_width=300):
    try:
        image = Image.open(image_path)
    except Exception as e:
        image=image_path
    
    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    # 将字符分行
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    # 输出结果
    #print(ascii_img)
    return asciiToImage(ascii_img)

# 调用主函数，替换为你的图片路径


def tojpg(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert('RGBA')  # 确保图像是 RGBA
    except Exception as e:
        print(e)
        return
    
    # 创建一个白色背景
    background = Image.new('RGBA', image.size, (255, 255, 255, 255))
    
    # 将原始图像粘贴到背景上
    background.paste(image, (0, 0), image)
    
    # 转换为 RGB
    background = background.convert('RGB')
    
    # 保存为 JPG 格式
    background.save('tmp.jpg')
    return 'tmp.jpg'
def openImage(image_path):
    return Image.open(image_path)
import os 
def drawPicture(name='temp.jpg')->Image:
        CopyTest.getNetImage('ReadyToConvert.jpg')
        os.system('DrawUtilsIV.py --input ReadyToConvert.jpg --output A.jpg')
        Picture=openImage('A.jpg')
        return Picture

if __name__ == "__main__":
    from sys import argv
    try:
        X=drawPicture(argv[1])
        X.save(argv[1].split('.')[0]+'result.jpg')
    except:
        o=drawPicture()
        o.save('Xs.jpg')
