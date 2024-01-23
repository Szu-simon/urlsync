import requests

def transform_line(line):
    """将单行数据转换为所需格式"""
    return f"- DOMAIN-SUFFIX, {line}, adblock"

# 步骤 1: 从 URL 下载数据
url = 'https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt'
response = requests.get(url)
lines = response.text.splitlines()

# 步骤 2: 将每行数据转换为新格式
transformed_lines = [transform_line(line) for line in lines]

# 步骤 3: 将转换后的数据写入新文件
with open('adblock-mysync.txt', 'w') as file:
    file.write('\n'.join(transformed_lines))
