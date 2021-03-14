import requests as rqst
import re
get_links = input()
get_lnk = rqst.get(get_links)


links = []

if get_lnk.status_code == 200:
    for url in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", get_lnk.text):
        links.append(url)

print(*links, sep ='\n')