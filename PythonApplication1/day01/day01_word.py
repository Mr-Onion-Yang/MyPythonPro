#conding=utf-8

"""
Description: Word文件转化TXT文本
Author：yangxiaoqiang   
Prompt: code in Python3 env
Install package： pip install pypiwin32
"""

import os,fnmatch
from win32com import client as wc 
from win32com.client import Dispatch

'''
    功能描述：word 文件转换为Txt格式，默认存储在当前的路径下，用户可以自行定义存在文件的路径即可
    参数描述：filePath :文件路径   savaPath ：指定要存放文件的位置
'''
def WordToTxt(filePath,savePath = ''):
    #1 切分文件的上级目录及文件名称 split()
    dirs,filename = os.path.split(filePath)

    #2 修改转换后的文件名称
    # fnmatch.fnmatch(filename, pattern)   测试filename，是否符合pattern。
    new_name  = ''
    if fnmatch.fnmatch(filename,'*.doc'):
        new_name = filename[:-4]+'.txt'
    elif fnmatch.fnmatch(filename,'*.docx'):
        new_name = filename[:-5]+'.txt'
    else:return
    print('->>',new_name)

    #3 文件转换后进行保存的路径
    if savePath == '':
        savePath = dirs
    else: savePath = savePath
    word_to_txt = os.path.join(savePath,new_name)
    print('->',word_to_txt)

    #4 加工对应的文件操作，将word转换为txt
    wordApp = wc.Dispatch('Word.Application')
    mytxt  = wordApp.Documents.Open(filePath) #打开文件进行读写
    mytxt.SaveAs(word_to_txt,4)
    mytxt.Close()

if __name__ == "__main__":
    filepath = os.path.abspath(r'../dataFileForm/dataFile/测试的文件.docx')
    print(filepath)
    WordToTxt(filepath)



