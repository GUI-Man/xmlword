# 导入sys
import os.path
import sys
import xmlword
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog
# 导入我们生成的界面
from ui_main import Ui_MainWindow
import xmlword2
# 继承QWidget类，以获取其属性和方法
class MyWidget(QMainWindow):
    #绑定槽使用
    def start(self):
        self.ui.selectFirstTitle.currentIndexChanged.connect(self.ChangeTextfirst)
        self.ui.selectSecondTitle.currentIndexChanged.connect(self.ChangeTextSecond)
        #self.ui.selectThirdTitle.currentIndexChanged.connect(self.ChangeTextThird)
        self.ui.fileBtn.clicked.connect(self.opnefile)
        self.ui.pushButton_xml_header.clicked.connect(self.xmlinfoHeader)
        self.ui.ExcuteResult.clicked.connect(self.Output)
        self.ui.pushButton_auto_produce.clicked.connect(self.AutoOutput)
        print(self.doc_file_name)
    def AutoOutput(self):
        self.ui.textEdit.setText("正在生成中")
        outputfilename="\\"+self.ui.ResultName.text()+".xls"
        path=os.getcwd()+outputfilename
        print(path)
        whetherexist=os.path.exists(path)
        if(whetherexist):
            self.ui.textEdit.setText("文件已存在，请删除或重新命名！")
            return
        try:
            self.xmlSuperiorXmlTool.filename=path
            self.xmlSuperiorXmlTool.xmlfile=self.doc_file_name
            self.xmlSuperiorXmlTool.main()
        except Exception as e:
            self.ui.textEdit.setText("生成失败")
            return
        self.ui.textEdit.setText("生成成功")
    def Output(self):
        self.ui.textEdit.setText("正在生成中")
        outputfilename="\\"+self.ui.ResultName.text()+".xls"
        path=os.getcwd()+outputfilename
        print(path)
        whetherexist=os.path.exists(path)
        if(whetherexist):
            self.ui.textEdit.setText("文件已存在，请删除或重新命名！")
            return
        try:
            self.xmlTool.Output(self.ui.lineEdit_first_title.text(),self.ui.lineEdit_second_title.text(),path)
        except Exception as e:
            self.ui.textEdit.setText("生成失败")
            return
        self.ui.textEdit.setText("生成成功")
    def ChangeTextSecond(self):
        self.ui.lineEdit_second_title.setText(self.ui.selectSecondTitle.currentText())
    # def ChangeTextThird(self):
    #     self.ui.lineEdit_third_title.setText(self.ui.selectThirdTitle.currentText())
    def ChangeTextfirst(self):
        self.ui.lineEdit_first_title.setText(self.ui.selectFirstTitle.currentText())
    #解析doc里的全部标题
    def xmlinfoHeader(self):
        self.xmlTool=xmlword.MyXmlFunc(self.doc_file_name)
        result=self.xmlTool.xmlinfo()
        if(result==-1):
            self.ui.xml_title_info("请选择正确的doc文件！")
        for i in result:
            self.ui.xml_title_info.append(i)
            print(i)
            self.ui.selectFirstTitle.addItem(i)
            self.ui.selectSecondTitle.addItem(i)
            self.ui.selectThirdTitle.addItem(i)
    def opnefile(self):
        filePath=QFileDialog.getOpenFileName()
        print(str(filePath[0]))
        self.ui.lineEdit_FilePath.setText(filePath[0])
        self.doc_file_name=str(filePath[0])
    def __init__(self):
        super().__init__()
        self.doc_file_name=""
        self.xmlTool=xmlword.MyXmlFunc("")
        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start()
        self.xmlSuperiorXmlTool=xmlword2.Main("","")
# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
