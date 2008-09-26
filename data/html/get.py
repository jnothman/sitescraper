import os


urls = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

for i, url in enumerate(urls):
    os.system("""wget "%s" --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre" -O %d.html""" % (url, i+1))
