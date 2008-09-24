import os


urls = [
    "http://ubuntuforums.org/showthread.php?t=928561",
    "http://ubuntuforums.org/showthread.php?t=762900",
    "http://ubuntuforums.org/showthread.php?t=925736",
    "http://ubuntuforums.org/showthread.php?t=928641",
    "http://ubuntuforums.org/showthread.php?t=923976",
    "http://ubuntuforums.org/showthread.php?t=928618",
]

for i, url in enumerate(urls):
    os.system("""wget "%s" --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre" -O %d.html""" % (url, i+1))
