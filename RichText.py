import imgkit
import markdown
code=['cpp','python','java','javascript','html','css']
def replacecode(s):
    for i in code:
        s=s.replace('```'+i,'```')
    return s
def markdownToImage(md:str):
    html = markdown.markdown(md)

    imgkit.from_string(html, 'markdownImage.png')
def indent(text: str, indent: str = '    ') -> str:
    """
    对被```包裹的代码块的每一行添加缩进

    :param text: 原始文本
    :param indent: 想要添加的缩进内容，默认为四个空格
    :return: 添加缩进后的文本
    """
    text=replacecode(text)
    # 以` ``` `分割文本
    parts = text.split("```")
    
    # 检查是否有代码块
    if len(parts) > 1:
        # 对每个代码块进行处理
        for i in range(1, len(parts), 2):
            # 对代码行添加缩进
            code_lines = parts[i].splitlines()
            indented_code = '\n'.join([indent + line for line in code_lines])
            parts[i] = indented_code

    # 重新拼接文本
    return "```".join(parts)
def containsRichText(text:str):
    if "```" in text:
        markdownToImage(indent(text.replace('```','```\n')).replace('```',''))
        
        pass
        return ['markdownImage.png','']
    return False
debugText='''
当然可以！快速排序是一种高效的排序算法，由C. A. R. Hoare在1960年提出。它采用分治法的策略来把一个序列分成两个子序列。以下是一个简单的快速排序实现示例：

```cpp
#include <iostream>

// 函数原型声明
void quickSort(int arr[], int left, int right);
int partition(int arr[], int left, int right);
void swap(int &a, int &b);

int main() {
    int data[] = {8, 7, 6, 1, 0, 9, 2};
    int n = sizeof(data) / sizeof(data[0]);
    std::cout << "Unsorted Array" << std::endl;
    for (int i = 0; i < n; ++i)
        std::cout << data[i] << " ";
    std::cout << std::endl;

    quickSort(data, 0, n - 1);

    std::cout << "Sorted Array in Ascending Order:" << std::endl;
    for (int i = 0; i < n; ++i)
        std::cout << data[i] << " ";
    return 0;
}

// 快速排序函数
void quickSort(int arr[], int left, int right) {
    int index; // 分区后的索引
    if (left < right) {
        index = partition(arr, left, right); // 获取分区后的基准元素索引
        quickSort(arr, left, index - 1); // 对左子数组进行递归排序
        quickSort(arr, index + 1, right); // 对右子数组进行递归排序
    }
}

// 分区函数
int partition(int arr[], int left, int right) {
    int pivot = arr[right]; // 取最右侧的元素作为基准元素
    int i = left - 1;
    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]); // 小于等于基准元素的交换到左边
        }
    }
    swap(arr[i + 1], arr[right]); // 把基准元素放到中间位置
    return i + 1;
}

// 交换函数
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
```

这段代码首先定义了一个`quickSort`函数来执行快速排序算法，并且使用了一个辅助函数`partition`来将数组分成两部分。此外，还有一个`swap`函数用于交换数组中的元素。

在`main`函数中，我们创建了一个数组并打印了排序前的结果，然后调用`quickSort`对数组进行排序，最后打印排序后的结果。
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
    #highlight_code(code,'python','pyCode')
    #textToLaTeXImage(r'水水水水水Hello $\frac{1}{2}$ World!','textCode')