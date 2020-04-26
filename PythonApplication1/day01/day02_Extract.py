#conding = utf-8

"""
Description: 多文档格式转换工具
Author：yangxiaoqiang
Prompt: code in Python3 env

1.做一个通过pdf及word文件通用的筛选方法，同时能够一起处理多个不同类型的文件
"""

import os,fnmatch
from win32com import client as wc 
from win32com.client import Dispatch


def fileToTxt(filePath,savePath = ''):

    try:
        #1 进行分割文件目录及文件名称
        dirs,filename = os.path.split(filePath)

        #2 进行加工并判断文件类型转换对应的文件名称及格式
        typename = os.path.splitext(filename)[-1].lower()

        #调用校验文件信息
        new_name = translFormt(typename,filename)
        print('新的名字->',new_name)

        #3 要转换并保存导致指定的文件路径下
        if savePath == '':
            savePath = dirs
        else:
            return
        new_save_path = os.path.join(savePath,new_name)
        print('保存的路径->',new_save_path)

        #4 进行文件预加工处理
        app = wc.Dispatch('Word.Application')
        myData = app.Documents.Open(filePath)   # -> 打开文件的路径
        myData.SaveAs(new_save_path)            # -> 保存要转换的文件信息
        myData.Close()

    except Exception as exc:
        exc.args

    

def translFormt(typeName,fileName):
    new_name = '' 

    if typeName == '.pdf':
        if fnmatch.fnmatch(fileName,'*.pdf'):
            new_name = fileName[:-4]+'.txt'
        else:return
    elif typeName == '.doc' or typeName == '.docx':
        if fnmatch.fnmatch(fileName,'*.doc'):
            new_name = fileName[:-4]+'.txt'
        elif fnmatch.fnmatch(fileName,'*.docx'):
            new_name = fileName[:-5]+'.txt'
    else:
        print('警告：\n您输入[',typeName,']不合法，本工具支持pdf/doc/docx格式,请输入正确格式。')
        return
    return new_name




if __name__ == "__main__":
    filePath1 = os.path.abspath(r'../dataFileForm/dataFile/碧桂园NC采购系统应用讲解2017.pdf')
    filepath2 = os.path.abspath(r'../dataFileForm/dataFile/测试的文件.docx')
    print(filePath1)
    fileToTxt(filePath1)