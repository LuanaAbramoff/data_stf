import chardet

with open("marco_aurelio.html", "rb") as f:
    encoding = chardet.detect(f.read())['encoding']
    print(encoding)