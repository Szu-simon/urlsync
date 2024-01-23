import requests

def transform_line(line):
    """将单行数据转换为所需格式，并移除不需要的字符"""
    # 移除行首的 '+' 和 '||'，以及行尾的 '^'
    line = line.lstrip('+||').rstrip('^')
    return f"- DOMAIN-SUFFIX, {line}, adblock"

# 从 URL 下载数据
url = 'https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt'
response = requests.get(url)
lines = response.text.splitlines()

# 转换数据并过滤注释
transformed_lines = [transform_line(line) for line in lines if not line.startswith('#')]

# 将转换后的数据写入新文件
with open('adblock-mysync.txt', 'w') as file:
    file.write('\n'.join(transformed_lines))
