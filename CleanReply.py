def retain_last_n_lines(file_name, n, overwrite=False):
    """
    保留文件的最后n行。

    :param file_name: 文件名
    :param n: 保留的行数
    :param overwrite: 是否覆盖原文件
    """
    with open(file_name, 'r', encoding='ansi') as file:
        lines = file.readlines()

    last_n_lines = lines[-n:]

    output_file_name = file_name if overwrite else 'Replied_last_100_lines.txt'
    with open(output_file_name, 'w', encoding='ansi') as output_file:
        output_file.writelines(last_n_lines)

# 使用函数保留Replied.txt的最后100行，并覆盖原文件
retain_last_n_lines('Replied.txt', 100, overwrite=True)

# 如果不想覆盖原文件，而是想生成一个新的文件，可以这样调用
# retain_last_n_lines('Replied.txt', 100, overwrite=False)
