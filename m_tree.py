import cgitb
cgitb.enable()
from bookui import *
class mtree(Ui_MainWindow):
    def settree(self,filename,tree,count):
        '''参数依次为文件名，目录树的控件名称，文章段落数（从主函数中获取）'''
        root = QTreeWidgetItem(tree)
        root.setText(0, filename)

        for i in range(0, count):
            if i == 0:
                temp = '原文'
            else:
                temp = '第' + str(i) + '段'
            self.additem(temp, tree)

        root.setExpanded(True)

    def additem(self, title, tree):
        '''参数依次为文章标题，目录树的控件名称'''
        # sum = tree.topLevelItemCount()
        root = tree.topLevelItem(0)
        new = QTreeWidgetItem()
        new.setText(0, title)
        root.addChild(new)