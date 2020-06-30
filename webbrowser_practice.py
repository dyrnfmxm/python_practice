import webbrowser
import time

list1 = {
    "https://github.com/dyrnfmxm",
    "https://www.naver.com/",
    "https://www.google.com/"
    }
for url in list1:
    webbrowser.open(url)
    time.sleep(10)
