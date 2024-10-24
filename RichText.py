from pygments import highlight
from pygments.lexers import PythonLexer, JavaLexer, CLexer, CppLexer, RubyLexer, GoLexer, JavascriptLexer
from pygments.formatters import ImageFormatter
import matplotlib.pyplot as plt
def highlight_code(code, lexer:str, outfile:str):
    if lexer=='python':
        lexer=PythonLexer()
    elif lexer=='java':
        lexer=JavaLexer()
    elif lexer=='c':
        lexer=CLexer()
    elif lexer=='cpp':
        lexer=CppLexer()
    elif lexer=='ruby':
        lexer=RubyLexer()
    elif lexer=='go':
        lexer=GoLexer()
    elif lexer=='javascript':
        lexer=JavascriptLexer()
    img = highlight(
        code,
        lexer,
        ImageFormatter(style='monokai', font_size=70, font='A.ttf'),  # 确保字体支持中文
        outfile=outfile + '.jpg'
    )
    
    return outfile + '.jpg'
def textToLaTeXImage(text:str, outfile:str,fontSize=16):
    #换个字体,否则中文会显示为方框
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    imageSize=(len(text)/10,2)
    fig=plt.figure(figsize=imageSize)
    ax=fig.add_axes([0,0,1,1])
    ax.axis('off')
    ay=fig.add_axes([0,0,1,1])
    ay.axis('off')
    ax.text(0.5,0.5,text,fontsize=fontSize,ha='center',va='center')
    fig.savefig(outfile+'.jpg',bbox_inches='tight',pad_inches=0)
    return outfile+'.jpg'
def containsRichText(text:str):
    if 'cpp' in text or 'python' in text or 'java' in text or 'ruby' in text or 'go' in text or 'javascript' in text:
        a=text.find('```')
        c=text.find('\n',a+3)
        b=text.find('```',a+3)
        code=text[c+1:b]
        whatcode=text[a+3:c]
        leftText=text[:a]
        rightText=text[b+3:]
        return [highlight_code(code,whatcode,'code'),leftText+rightText]

    elif '$' in text:
        temp=text
        text=''
        count=0
        iiS=False
        for i in temp:
            count+=1
            if count>20:
                text+=i+'\n'
            else:
                text+=i
            if i=='$':
                if  not iiS:
                    text+='\n$'
                    iiS=True
                else:
                    text+='$'
                    iiS=False
        return [textToLaTeXImage(text,'LaTeXImage'),'']
    else:
        return False
debugText='''
在Windows系统中，你可以使用`system()`函数来执行命令行的关机操作。下面是一个简单的C++程序，它会设置一个倒计时关机的功能。请注意，这个程序仅适用于Windows，并且使用`system()`函数有一定的风险，因为它直接执行了命令行指令。

```cpp
#include <iostream>
#include <windows.h> // 需要包含这个头文件来使用Sleep函数

void shutdownComputer(int seconds) {
    std::cout << "您的电脑将在 " << seconds << " 秒后自动关机。\n";
    
    // 倒计时显示
    while (seconds > 0) {
        std::cout << seconds << "秒后关机..." << std::endl;
        Sleep(1000); // 暂停一秒
        seconds--;
    }

    // 执行关机命令
    system("shutdown /s /t 0");
}

int main() {
    int delay = 60; // 设置延迟时间，单位为秒
    shutdownComputer(delay);
    return 0;
}
```

在这个示例中，我们定义了一个`shutdownComputer`函数，它接受一个整数参数`seconds`，表示多少秒之后执行关机操作。在主函数`main`中，我们设置了延迟时间为60秒，并调用了`shutdownComputer`函数。

请注意：
- 使用`system()`函数存在安全隐患，因为它允许直接执行命令行指令。如果可能的话，最好避免在生产代码中使用`system()`函数。
- 关机操作应该谨慎使用，因为这可能会导致数据丢失或损坏。
- 如果你想要取消关机操作，可以使用命令`shutdown /a`来取消正在进行的关机进程。

如果你需要在其他操作系统（如Linux或macOS）上实现类似的功能，或者需要更安全的方式来处理系统级操作，请告诉我，我可以提供相应的解决方案。
'''
debugText2=r'''
你好你好你好你好
Hello $\frac{1}{2}$ World!
'''
if __name__=='__main__':
    code='''
    for i in range(10):
        print(i)
    '''
    print(  containsRichText(debugText))
    containsRichText(debugText2)
    #highlight_code(code,'python','pyCode')
    #textToLaTeXImage(r'水水水水水Hello $\frac{1}{2}$ World!','textCode')