import os

ml=input("请输入文件目录：")
wj=[]
count=0

def getfile(file_dir): #使用os模块识别一个目录下的所有文件名
    for root,dirs,files in os.walk(file_dir):
        global wj
        wj=files

def N1(ml,wj): #用于为大量文件名最前有序号接空格的文件补全序号 如： 文件夹里有 0-112 标准日本语 这个程序可以为0-9前添加2个0 为10-99前添加1个0 使数字序号的位数和最大的位数相等
    max=0#用于记录最后一个文件前面的序号有多少位
    c1=0
    c2=0#c1,c2中间参数
    l1=len(wj)
    for w1 in range(0,l1):
        for s in wj[w1]:
            if s!=' ':
                c1+=1
            else:
                break;
        if c1>max:
            max=c1
        c1=0

    for i in range(0,l1):
      for strs in wj[i]:
          if strs!=' ':
            c2+=1
          else:
            break;
      if c2!=max:
          tem1=wj[i]
          wj[i]='0'*(max-c2)+wj[i]
          os.rename(ml+'\\'+tem1,ml+'\\'+wj[i])
      c2=0
