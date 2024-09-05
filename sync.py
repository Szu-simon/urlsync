import requests

# 定义原始链接
url = "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt"

# 获取规则内容
response = requests.get(url)
rules = response.text.splitlines()

# 存放转换后的规则
converted_rules = []

# 转换规则格式
for rule in rules:
    if rule.startswith('||') and rule.endswith('^'):
        domain = rule[2:-1]
        converted_rule = f"- DOMAIN-SUFFIX,{domain},🆎 AdBlock"
        converted_rules.append(converted_rule)

# 将转换后的规则写入文件
with open('converted_rules.txt', 'w') as f:
    f.write("\n".join(converted_rules))

print("Rules converted successfully!")
