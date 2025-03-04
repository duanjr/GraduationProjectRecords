import re

# 定义源文件路径
file_path = r"littlefs代码分析—lfs.c.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

modified_lines = []
for line in lines:
    if line.startswith("- `` "):
        line = "- `" + line[4:]
    modified_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(modified_lines)

print("处理完成：所有以 -` 开头的行已在后面添加了空格。")
