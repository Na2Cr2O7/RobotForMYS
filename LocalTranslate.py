
import Constant
if  not Constant.DOTRANSLATE:
    def translate(text):
        return text
    
import argostranslate.package
import argostranslate.translate
from_code = "en"
to_code = "zh"
 # 加载已安装的语言包
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
     filter(
         lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
     )
 )
 # 获取翻译模型（例如，从英语到西班牙语）
argostranslate.package.install_from_path(package_to_install.download())
  
 # 执行翻译
def translate(text):
    global from_code, to_code
    translatedText = argostranslate.translate.translate(text, from_code, to_code)
    print(translatedText)
    return translatedText
if __name__ == '__main__':
    from sys import argv
    if len(argv)==1:
        print("Usage: LocalTranslate.py [text]")
        exit()
    text = argv[1]
    if len(argv)>2:
        text=' '.join(argv[1:])
    translate(text)