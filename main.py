import PyPDF2
output = open('C:/Users/user/Downloads/work.txt', "w" , encoding='utf-8')
reader = PyPDF2.PdfReader('C:/Users/user/Downloads/123.pdf')
work = []
zagolovki = []
mid = []
mgn = []
for i in range(1174,1187):
    text = reader.pages[i].extract_text()

    lines = text.split("\n")
    print(lines , i)
    for i in lines:
        print(len(i))
        if i[0].isdigit() and i.isdigit() != 1:
            kek = str(i + "\n")
            output.write(kek)
