import os,time

def getPathCurrentFile(path):

    files = os.listdir(path)
    for file in files:
        if(os.path.isdir(file)==True):
            getPathCurrentFile(os.path.join(os.getcwd(),file))
        print("文件名称", file)


def getPathCurrentFile01(path):
    for file in os.scandir(path):
        print(file.name,time.ctime(file.stat().st_mtime))


if __name__ == '__main__':
    #获取当前控制台的路径
    print(os.getcwd())

    #获取当前路径并创建一个新的文件夹路径
    print(os.path.join(os.getcwd(),'first'))

    #获取当前文件目录
    print(os.listdir(os.getcwd()))

    #获取指定路径的文件
    getPathCurrentFile(os.getcwd())

    print("++++++++++++++++++++++++")

    getPathCurrentFile01(os.getcwd())