#coding = utf-8


"""
Description: PDF文件转化TXT文本
Author：yangxiaoqiang
Prompt: code in Python3 env
"""
import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch 



def PdfToTxt(filePath, savePath = ''):
    #1 切分文件的目录及文件名称
    dirs,filename = os.path.split(filePath)
    print(filename)

    #2 修改对应的转换后的名称
    new_name = ''
    if fnmatch.fnmatch(filename,'*.PDF') or fnmatch.fnmatch(filename,'*.pdf'):
        new_name = filename[:-4]+'.txt'
    else:
        return
    print('->>',new_name)

    #3 文件转换后要保存的路径
    if savePath == '':
        savePath = dirs
    pdf_to_txt = os.path.join(savePath,new_name)
    print('->',pdf_to_txt)


    #4 加载处理应用 pdf转换txt
    appl = wc.Dispatch('Word.Application')
    myData = appl.Documents.Open(filePath)
    myData.SaveAs(pdf_to_txt,4)
    myData.Close()


if __name__ == "__main__":
   