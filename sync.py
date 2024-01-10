import requests

url = 'https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt'

response = requests.get(url)
text = response.text

domains = []
for line in text.splitlines():
  domain = line.split()[0]
  domains.append(domain)

payload = '\n'.join(['- ' + domain for domain in domains])
print(payload)
