import os
from pathlib import Path


dirpath = r"\\192.168.1.102\人財開発\派遣管理\スタッフ契約書\2020年上期　（新様式になります）\ダイエットクック小田原\岡本さんから　8-9"
paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
file = open("testdir list.txt","a",encoding="UTF-8",newline="")
for i in paths:
    i = str(i)
    i= i[76:]+str(r"n")
    file.writelines(i)
file.close()