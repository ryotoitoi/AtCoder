# coding: UTF-8
 
f = open('text.txt')
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
 
while line:
    print(line)
    line = f.readline()
f.close