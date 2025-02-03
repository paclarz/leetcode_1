import os
import sys
import time


class myPath:
    rootPath = os.getcwd()  # the root path of the project
    path = rootPath  # the core path

    def __init__(self, path=None):
        if path is not None:
            self.path = path

    def __add__(self, other: str = None):
        if isinstance(other, myPath):
            str = str()
        if other is not None:
            os.path.join(self.path, other)
        return myPath(os.path.join(self.path, other))

    def __call__(self, *args, **kwargs) -> str:
        if args:
            self.__add__(args[0])

        return self.path


class FileManager:
    rootPath = myPath()  # the root path of the project
    problemPath = myPath() + "problems"  # the path of the problems folder
    checkPath = myPath() + "problems" + "check"  # the default path of the check folder
    solvePath = myPath() + "problems" + "solve"  # the default path of the solve folder

    # 如果这些路径不存在，则创建它们
    def __init__(self):
        if not os.path.exists(self.problemPath()):
            os.makedirs(self.problemPath())
        if not os.path.exists(self.checkPath()):
            os.makedirs(self.checkPath())
        if not os.path.exists(self.solvePath()):
            os.makedirs(self.solvePath())

    dirs = os.listdir(rootPath())  # the list of the directories in the problems folder

    def createFile(self, path, content):
        if isinstance(path, myPath):
            path = path()
        assert path.endswith(".py"), "file extension should be .py"
        with open(path, "w") as f:
            f.write(content)
            f.close()

    def moveFile(self, src, dst):
        if isinstance(src, myPath):
            src = src()
        if isinstance(dst, myPath):
            dst = dst()

        os.rename(src, dst)

    def checkExists(self, path: myPath):
        path = path()
        assert path.endswith(".py"), "file extension should be .py"
        if os.path.exists(path):
            return True
        else:
            return False


class SetupProblems(FileManager):
    thisTime = time.localtime()  # the current time
    problemName = ""  # the number of the problem e.g. 0001
    content = ""  # the content of the file
    fileName = ""  # the full name of the file

    def __init__(self, problemName):
        super().__init__()
        self.problemName = problemName
        self.initVars(problemName)
        print((myPath() + "problems" + "solve" + self.fileName)())

        if self.checkExists(myPath() + "problems" + "solve" + self.fileName):
            print("file already exists , please select the destination folder \n")
            dst = input()
            if dst in self.dirs:
                self.moveDoneFiles(dst)
            else:
                print("destination folder not found")

        else:
            self.initFiles()

    def initFiles(self):
        print("about to create files" + self.fileName + '\n' + "are you sure? (y/n) \n")
        confirm = input()
        if confirm == "y":
            self.createFile(myPath() + "problems" + "check" + self.fileName, self.content + "\n" \
                            + "from solve import " + self.fileName[:-3] + " as Solution")
            self.createFile(myPath() + "problems" + "solve" + self.fileName, self.content)
            print("files created")
        else:
            print("files not created")
        pass

    def moveDoneFiles(self, dst):
        print("about to move the files" + self.fileName + '\n' + "please select the destination folder \n")

        self.moveFile(myPath() + "problems" + "solve" + self.fileName,
                      myPath() + dst + "solve" + self.fileName)

        self.moveFile(myPath() + "problems" + "check" + self.fileName,
                      myPath() + dst + "check" + self.fileName)

    def initVars(self, problemName):
        self.problemName = problemName
        self.fileName = time.strftime("%b_%d_", time.localtime()) + self.problemName + ".py"
        self.content = "# problem No." + problemName + "\n" \
                       + "# created by setup.py at " \
                       + time.strftime("%Y-%m-%d %H:%M:%S", self.thisTime) + "\n"


def exe():
    name = sys.argv[1]
    assert len(name) == 4, "incorrect filename"
    SetupProblems(name)


exe()
