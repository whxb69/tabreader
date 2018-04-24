# -*- coding:utf-8 -*-
import sys
import chardet
from bookui import *
from m_trans import tfunction
from m_tree import mtree
import cgitb
import re
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

cgitb.enable()

tabnum = 2
addpos = 1
textnum = 1


# class Tree(QTreeWidget):
#     def dragLeaveEvent(self, e):
#         print(e)
#         if e.MimeData().hasText():
#             e.accept()
#         else:
#             e.ignore()
#
#     def dropEvent(self, e):
#         tree = win.treeWidget
#         item = win.treeWidget.currentItem()
#         root = tree.topLevelItem(0)
#         num = root.indexOfChild(item)
#         edit = 'win.textEdit_' + str(num) + '_1'
#
#         print(eval(edit + '.toPlainText'))
#
#     def keyPressEvent(self, e):
#         if e.modifiers() & Qt.ControlModifier:
#             item = win.treeWidget.currentItem()
#             item.setSelected(True)
#             print('!')


class Mainwindow(QMainWindow, Ui_MainWindow ):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.clicked.connect(self.link_tree)
        self.pro_tabWidget.currentChanged.connect(self.tabchanged)
        self.button_merge.clicked.connect(self.merge_go)
        self.action_merge.triggered.connect(self.merge)
        self.action_super.triggered.connect(self.super)
        self.action_alter.triggered.connect(self.alter)
        self.action_save.triggered.connect(self.save)
        self.action_Open.triggered.connect(self.open)
        self.action_trans.triggered.connect(self.Totrans)
        # self.splitter.addWidget(self.treeWidget)
        # self.splitter.addWidget(self.pro_tabWidget)


    def open(self):
        FileName, filetype = QFileDialog.getOpenFileName \
            (self,
             "选取文件",
             "E:",
             "Text Files (*.txt);;Subtitle File(*.srt);;All File(*.*)")

        global edittext

        currenttab = self.pro_tabWidget.currentIndex()
        print(str(currenttab))
        textEditnum = 'self.textEdit_' + str(currenttab) + '_1'

        if FileName:
            try:
                f = open(FileName, 'r')
                eval(textEditnum).setText("")
                text = f.read()
            except UnicodeDecodeError:
                try:
                    f = open(FileName, 'rb')
                    eval(textEditnum).setText("")
                    text = f.read().decode('utf-8')
                except UnicodeDecodeError:
                    f = open(FileName, 'r')
                    eval(textEditnum).setText("")
                    text = f.read()
                    print(chardet.detect(text)['encoding'])
            print(textEditnum)
            eval(textEditnum).setText(text)

            global filename
            end = 0
            filename = os.path.basename(f.name)

            for i in range(len(filename)):
                if filename[i] == '.':
                    end = i

            filename = filename[:end]
            f.close()

            self.tabWidget.setCurrentIndex(0)
            # self.tabWidget.currentIndex()

    def save(self):
        pro_tab = self.pro_tabWidget.currentIndex()
        tab = self.tabWidget.currentIndex()
        print(str(pro_tab) + '_' + str(tab))
        edit = 'win.textEdit_' + str(pro_tab) + '_' + str(tab + 1)
        text = eval(edit).toPlainText()
        global filename

        FileName, filetype = QFileDialog.getSaveFileName \
            (self,
             "选取文件",
             "E:",
             "Text Files (*.txt);;Subtitle File(*.srt);;All File(*.*)")

        if FileName:
            f = open(FileName, 'w')
            f.write(text)
            f.close()

    def alter(self):
        text_1 = ''
        text_2 = ''
        j = 0

        currenttab = self.pro_tabWidget.currentIndex()
        temp = eval('self.textEdit_' + str(currenttab) + '_1').toPlainText()

        temp_1 = temp.replace('，', '，*').replace('。', '。*').replace('；', '；*').replace('？', '？*').replace('！', '！*')
        temp_2 = temp.replace('。', '。*').replace('；', '；*').replace('？', '？*').replace('！', '！*')

        pattern = re.compile('\*', re.S)

        word_1 = pattern.split(temp_1)
        word_2 = pattern.split(temp_2)

        print(word_1)
        print(word_2)

        for i in range(len(word_1) - 1):
            if word_1[i][0] == '”':
                word_1[i] = word_1[i][1:]
                word_1[i - 1] = word_1[i - 1] + '”'

        for i in range(len(word_2) - 1):
            if word_2[i][0] == '”':
                word_2[i] = word_2[i][1:]
                word_2[i - 1] = word_2[i - 1] + '”'

        i = 0

        try:
            while word_1[i] != '' and i < len(word_1):
                text_1 += word_1[i] + '\n\n'
                i = i + 1

            while word_2[j] != '' and j < len(word_2):
                text_2 += word_2[j] + '\n\n'
                j = j + 1
        except:
            pass

        eval('self.textEdit_' + str(currenttab) + '_2').setText(text_1)
        self.tabWidget.setCurrentIndex(1)
        eval('self.textEdit_' + str(currenttab) + '_3').setText(text_2)


    def addtab(self, flag, sign):
        tabtotal = self.pro_tabWidget.count() - 1
        currenttab = self.pro_tabWidget.currentIndex()
        num = 0        #添加合并页时用于计数
        if flag == 0:
            if tabtotal == currenttab:
                flag = 1

        if flag == 1:
            global tabnum
            global addpos
            global textnum


            if sign == 0:
                textnum_1 = 'self.textEdit_' + str(textnum) + '_1'
                textnum_2 = 'self.textEdit_' + str(textnum) + '_2'
                textnum_3 = 'self.textEdit_' + str(textnum) + '_3'
                textnum_4 = 'self.textEdit_' + str(textnum) + '_4'

                tabnum_2 = 'self.tab_' + str(tabnum) + '_2'
                tabnum_3 = 'self.tab_' + str(tabnum) + '_3'
                tabnum_4 = 'self.tab_' + str(tabnum) + '_4'
                tabnum_5 = 'self.tab_' + str(tabnum) + '_5'

                tabname = 'untitled' + str(tabnum)
            elif sign == -1:
                num = self.pro_tabWidget.count() - 1
                textnum_1 = 'self.textEdit_' + str(num) + '_1'
                textnum_2 = 'self.textEdit_' + str(num) + '_2'
                textnum_3 = 'self.textEdit_' + str(num) + '_3'
                textnum_4 = 'self.textEdit_' + str(num) + '_4'

                tabnum_2 = 'self.tab_' + str(num) + '_2'
                tabnum_3 = 'self.tab_' + str(num) + '_3'
                tabnum_4 = 'self.tab_' + str(num) + '_4'
                tabnum_5 = 'self.tab_' + str(num) + '_5'

                tabname = '合并页'
            else:
                textnum_1 = 'self.textEdit_' + str(sign) + '_1'
                textnum_2 = 'self.textEdit_' + str(sign) + '_2'
                textnum_3 = 'self.textEdit_' + str(sign) + '_3'
                textnum_4 = 'self.textEdit_' + str(sign) + '_4'

                tabnum_2 = 'self.tab_' + str(sign) + '_2'
                tabnum_3 = 'self.tab_' + str(sign) + '_3'
                tabnum_4 = 'self.tab_' + str(sign) + '_4'
                tabnum_5 = 'self.tab_' + str(sign) + '_5'
                tabname = '第' + str(sign) + '段'

            font = QtGui.QFont()
            font.setPointSize(12)

            self.pro_tab = QtWidgets.QWidget()
            self.pro_tab.setObjectName("protab")
            self.pro_tabWidget.addTab(self.pro_tab, tabname)

            self.tabWidget = QtWidgets.QTabWidget(self.pro_tab)
            self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
            self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
            self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
            self.tabWidget.setObjectName("tabWidget")

            exec(tabnum_2 + ' = QtWidgets.QWidget()')
            eval(tabnum_2).setObjectName("tab_2")
            exec(textnum_1 + ' = QtWidgets.QTextEdit(' + tabnum_2 + ')')
            eval(textnum_1).setGeometry(QtCore.QRect(0, 0, 1545, 1151))
            self.tabWidget.addTab(eval(tabnum_2), "原文")
            eval(textnum_1).setFont(font)

            exec(tabnum_3 + ' = QtWidgets.QWidget()')
            eval(tabnum_3).setObjectName("tab_3")
            exec(textnum_2 + ' = QtWidgets.QTextEdit(' + tabnum_3 + ')')
            eval(textnum_2).setGeometry(QtCore.QRect(0, 0, 1545, 1151))
            self.tabWidget.addTab(eval(tabnum_3), "逗号")
            eval(textnum_2).setFont(font)

            exec(tabnum_4 + ' = QtWidgets.QWidget()')
            eval(tabnum_4).setObjectName("tab_4")
            exec(textnum_3 + ' = QtWidgets.QTextEdit(' + tabnum_4 + ')')
            eval(textnum_3).setGeometry(QtCore.QRect(0, 0, 1545, 1151))
            self.tabWidget.addTab(eval(tabnum_4), "句号")
            eval(textnum_3).setFont(font)

            exec(tabnum_5 + ' = QtWidgets.QWidget()')
            eval(tabnum_5).setObjectName("tab_5")
            exec(textnum_4 + ' = QtWidgets.QTextEdit(' + tabnum_5 + ')')
            eval(textnum_4).setGeometry(QtCore.QRect(0, 0, 1545, 1151))
            self.tabWidget.addTab(eval(tabnum_5), "翻译")
            eval(textnum_4).setFont(font)

            # self.addButton.move(210 + addpos * 150, 105)

            tabnum = tabnum + 1
            addpos = addpos + 1
            textnum = textnum + 1

            print(tabtotal)
            self.pro_tabWidget.setCurrentIndex(0)

            if sign == -1:
                return eval('self.textEdit_' + str(num) + '_1')
        self.pro_tabWidget.setCurrentIndex(tabtotal + 1)


    def tabchanged(self):
        print(self.pro_tabWidget.currentIndex())

    def super(self):
        # for i in range(1,self.pro_tabWidget.count()):
        #     self.pro_tabWidget.removeTab(i)
        tab = self.pro_tabWidget.currentIndex()
        textname = 'self.textEdit_' + str(tab) + '_1'
        text = eval(textname + '.toPlainText()')
        text_org = text
        print(textname + '.text()', text)

        line = 0  # 文章分段模式时做换行符计数用
        for i in range(len(text)):
            if text[i] == '\n':
                line = line + 1
        if line == 0:
            text_seg = text.split('。')
            k = 0
            for i, x in enumerate(text_seg):
                if i == 0:
                    text[k] = x
                else:
                    text[k] = text[k] + x
                    if (i + 1) % 5 == 0:
                        k = k + 1
            text_seg = text

        else:
            text_seg = text.split('\n')

        print('text_seg', text_seg)
        text = [''] * len(text_seg)  # 设置新的列表存储二次分段后的的文本
        k = 0
        flag = 0
        for i in range(len(text_seg)):
            sum = 0
            if text_seg[i] != '':
                for j in range(len(text_seg[i])):
                    if text_seg[i][j] == '。':
                        sum = sum + 1
                if k > 0 and sum >= 3:
                    k = k + 1
                    text[k] = text_seg[i]
                else:
                    text[k] = text[k] + '\r' + text_seg[i]
                    flag = flag + 1
                    if flag == 6:  # 最多6个短分段为一组
                        k = k + 1
                        flag = 0

        print('1', text)

        self.pro_tabWidget.setTabText(0, '原文')
        self.textEdit_0_1.setText(text_org)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_0_1.setFont(font)

        num = 0
        for i in range(len(text)):
            if text[i] != '':
                try:
                    textname = eval('self.textEdit_' + str(num + 1) + '_1')
                    print(textname)
                except:
                    self.addtab(1, num + 1)

                eval('self.textEdit_' + str(num + 1) + '_1' + '.setText(text[i])')
                num = num + 1

        global filename
        global pre_filename
        catalog = mtree()
        count = self.pro_tabWidget.count()  # 标签 即段落数量
        catalog.settree(filename,self.treeWidget,count)

    # def additem(self, title):
    #     tree = self.treeWidget
    #     # sum = tree.topLevelItemCount()
    #     root = tree.topLevelItem(0)
    #     new = QTreeWidgetItem()
    #     new.setText(0, title)
    #     root.addChild(new)

    def link_tree(self):
        item = self.treeWidget.currentItem()
        if item:
            root = item.parent()
            num = root.indexOfChild(item)
            self.pro_tabWidget.setCurrentIndex(num)

    def merge(self):
        tree = self.treeWidget
        root = tree.topLevelItem(0)
        for i in range(root.childCount()):
            if i != 0 and root.child:
                root.child(i).setCheckState(0, Qt.Unchecked)
        self.button_merge.setEnabled(True)

    def merge_go(self):
        tree = self.treeWidget
        root = tree.topLevelItem(0)
        text = ''
        remove = ['']
        for i in range(root.childCount()):
            if root.child(i).checkState(0) == Qt.Checked:
                item = root.child(i)
                num = root.indexOfChild(item)
                if remove[0] == '':
                    remove[0] = num
                else:
                    remove.append(num)
                no = item.text(0)[1]
                edit = 'self.textEdit_' + no + '_1'
                text = text + eval(edit + '.toPlainText()')

        if remove[0] == '':
            QMessageBox.information(self, "提示",
                                    self.tr("未选中需合并段落!"))

        else:
            # layout = QMessageBox.question(self,'询问','是否保留原标签页？',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            # print(layout)
            print('remove', remove)
            rflag = 1
            # if layout == QMessageBox.Yes:
            #     pass
            # elif layout == QMessageBox.No:
            for i in range(len(remove), 0, -1):
                self.pro_tabWidget.removeTab(remove[i - 1])

            self.newedit = self.addtab(1,-1)

            if rflag == 1:
                for i in range(root.childCount() - 1, 0, -1):
                    if root.child(i).checkState(0) == Qt.Checked:
                        root.removeChild(root.child(i))

                for i in range(root.childCount()):
                    if i != 0:
                        root.child(i).setCheckState(0, Qt.Unchecked)

            else:
                for i in range(root.childCount()):
                    if i != 0:
                        root.child(i).setCheckState(0, Qt.Unchecked)

            # self.newedit = QtWidgets.QTextEdit(self.newtab)
            # self.newedit.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
            self.newedit.setText(text)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.newedit.setFont(font)
            self.pro_tabWidget.setCurrentIndex(self.pro_tabWidget.count() + 1)

            self.additem('合并页')  # 将新页面加入目录

    def Totrans(self):
        cur = self.pro_tabWidget.currentIndex()
        temp = eval('self.textEdit_' + str(cur) + '_1.toPlainText()')               #待翻译内容
        f_trans = tfunction()
        String = f_trans.trans(temp)                                                #翻译结果
        # print(temp)
        eval('self.textEdit_' + str(cur) + '_4').setText("")
        eval('self.textEdit_' + str(cur) + '_4').setText(String)
        self.tabWidget.setCurrentIndex(3)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())