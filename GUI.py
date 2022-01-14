# All the windows for the GUI

from PyQt5 import QtCore, QtGui, QtWidgets

# MainWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QtCore.QSize(600, 700))
        MainWindow.setMaximumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.title.setObjectName("title")
        self.AddBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddBookButton.setGeometry(QtCore.QRect(150, 490, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddBookButton.setFont(font)
        self.AddBookButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddBookButton.setAutoDefault(False)
        self.AddBookButton.setObjectName("AddBookButton")
        self.DeleteBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBookButton.setGeometry(QtCore.QRect(150, 530, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DeleteBookButton.setFont(font)
        self.DeleteBookButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeleteBookButton.setAutoDefault(False)
        self.DeleteBookButton.setObjectName("DeleteBookButton")
        self.IssueBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.IssueBookButton.setGeometry(QtCore.QRect(150, 570, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.IssueBookButton.setFont(font)
        self.IssueBookButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IssueBookButton.setAutoDefault(False)
        self.IssueBookButton.setObjectName("IssueBookButton")
        self.ReturnBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnBookButton.setGeometry(QtCore.QRect(150, 610, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ReturnBookButton.setFont(font)
        self.ReturnBookButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ReturnBookButton.setAutoDefault(False)
        self.ReturnBookButton.setObjectName("ReturnBookButton")
        self.ListIssuesButton = QtWidgets.QPushButton(self.centralwidget)
        self.ListIssuesButton.setGeometry(QtCore.QRect(150, 650, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ListIssuesButton.setFont(font)
        self.ListIssuesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ListIssuesButton.setAutoDefault(False)
        self.ListIssuesButton.setObjectName("ListIssuesButton")
        self.BooksList = QtWidgets.QTableView(self.centralwidget)
        self.BooksList.setGeometry(QtCore.QRect(10, 80, 580, 380))
        self.BooksList.setObjectName("BooksList")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.875pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Welcome to our library!</span></p></body></html>"))
        self.AddBookButton.setText(_translate("MainWindow", "Add a new book"))
        self.DeleteBookButton.setText(_translate("MainWindow", "Delete a book"))
        self.IssueBookButton.setText(_translate("MainWindow", "Issue a book"))
        self.ReturnBookButton.setText(_translate("MainWindow", "Return a book"))
        self.ListIssuesButton.setText(_translate("MainWindow", "List all issues"))

# Add Book Window
class AddBookWindow(object):
    def setupUi(self, AddBookGUI):
        AddBookGUI.setObjectName("AddBookGUI")
        AddBookGUI.resize(600, 700)
        AddBookGUI.setMinimumSize(QtCore.QSize(600, 700))
        AddBookGUI.setMaximumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(AddBookGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QTextBrowser(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 602, 702))
        self.Background.setObjectName("Background")
        self.Title = QtWidgets.QTextBrowser(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.Title.setObjectName("Title")
        self.BookName = QtWidgets.QTextBrowser(self.centralwidget)
        self.BookName.setGeometry(QtCore.QRect(10, 100, 171, 51))
        self.BookName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BookName.setObjectName("BookName")
        self.BookNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.BookNameInput.setGeometry(QtCore.QRect(0, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BookNameInput.setFont(font)
        self.BookNameInput.setText("")
        self.BookNameInput.setObjectName("BookNameInput")
        self.AuthorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AuthorInput.setGeometry(QtCore.QRect(0, 290, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AuthorInput.setFont(font)
        self.AuthorInput.setObjectName("AuthorInput")
        self.Author = QtWidgets.QTextBrowser(self.centralwidget)
        self.Author.setGeometry(QtCore.QRect(10, 240, 171, 41))
        self.Author.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Author.setObjectName("Author")
        self.YearInput = QtWidgets.QLineEdit(self.centralwidget)
        self.YearInput.setGeometry(QtCore.QRect(0, 420, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.YearInput.setFont(font)
        self.YearInput.setObjectName("YearInput")
        self.Year = QtWidgets.QTextBrowser(self.centralwidget)
        self.Year.setGeometry(QtCore.QRect(10, 370, 291, 41))
        self.Year.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Year.setObjectName("Year")
        self.Quantity = QtWidgets.QTextBrowser(self.centralwidget)
        self.Quantity.setGeometry(QtCore.QRect(10, 500, 171, 51))
        self.Quantity.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Quantity.setObjectName("Quantity")
        self.QuantityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.QuantityInput.setGeometry(QtCore.QRect(0, 550, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.QuantityInput.setFont(font)
        self.QuantityInput.setObjectName("QuantityInput")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(0, 640, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Send.setFont(font)
        self.Send.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Send.setObjectName("Send")
        self.Return = QtWidgets.QPushButton(self.centralwidget)
        self.Return.setGeometry(QtCore.QRect(200, 640, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Return.setFont(font)
        self.Return.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Return.setObjectName("Return")
        AddBookGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddBookGUI)
        QtCore.QMetaObject.connectSlotsByName(AddBookGUI)

    def retranslateUi(self, AddBookGUI):
        _translate = QtCore.QCoreApplication.translate
        AddBookGUI.setWindowTitle(_translate("AddBookGUI", "MainWindow"))
        self.Title.setHtml(_translate("AddBookGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.875pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">Add a new book</span></p></body></html>"))
        self.BookName.setHtml(_translate("AddBookGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Book\'s name:</span></p></body></html>"))
        self.Author.setHtml(_translate("AddBookGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Author:</span></p></body></html>"))
        self.Year.setHtml(_translate("AddBookGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Year of publication:</span></p></body></html>"))
        self.Quantity.setHtml(_translate("AddBookGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Quantity:</span></p></body></html>"))
        self.Send.setText(_translate("AddBookGUI", "Send"))
        self.Return.setText(_translate("AddBookGUI", "Return"))

# Delete Book Window.
class DeleteBookWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QtCore.QSize(600, 700))
        MainWindow.setMaximumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.title.setObjectName("title")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1, 360, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1, 310, 530, 41))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(0, 480, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Send.setFont(font)
        self.Send.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Send.setObjectName("Send")
        self.AllBooksOption = QtWidgets.QCheckBox(self.centralwidget)
        self.AllBooksOption.setGeometry(QtCore.QRect(0, 420, 201, 60))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AllBooksOption.setFont(font)
        self.AllBooksOption.setObjectName("AllBooksOption")
        self.Return = QtWidgets.QPushButton(self.centralwidget)
        self.Return.setGeometry(QtCore.QRect(0, 540, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Return.setFont(font)
        self.Return.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Return.setObjectName("Return")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.875pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Delete a book</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Which book id do you want to delete?</span></p></body></html>"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.AllBooksOption.setText(_translate("MainWindow", "Delete All Books?"))
        self.Return.setText(_translate("MainWindow", "Return"))

# Issue Book Window
class IssueBookWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QtCore.QSize(600, 700))
        MainWindow.setMaximumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.title.setObjectName("title")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1, 260, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1, 210, 530, 41))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(1, 400, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1, 350, 530, 41))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(0, 470, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Send.setFont(font)
        self.Send.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Send.setObjectName("Send")
        self.Return = QtWidgets.QPushButton(self.centralwidget)
        self.Return.setGeometry(QtCore.QRect(0, 530, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Return.setFont(font)
        self.Return.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Return.setObjectName("Return")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.875pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Issue a book</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Which book id do you want to borrow?</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">What is the customer\'s id?</span></p></body></html>"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.Return.setText(_translate("MainWindow", "Return"))

# Return Book Window
class ReturnBookWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QtCore.QSize(600, 700))
        MainWindow.setMaximumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.title.setObjectName("title")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 250, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 200, 530, 41))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 390, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 340, 530, 41))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(-1, 460, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Send.setFont(font)
        self.Send.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Send.setObjectName("Send")
        self.Return = QtWidgets.QPushButton(self.centralwidget)
        self.Return.setGeometry(QtCore.QRect(0, 520, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Return.setFont(font)
        self.Return.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.Return.setObjectName("Return")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.875pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Return a book</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Which book id do you want to return?</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">What is the customer\'s id?</span></p></body></html>"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.Return.setText(_translate("MainWindow", "Return"))

# All Issues Window
class AllIssuesWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QTextBrowser(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.Title.setMinimumSize(QtCore.QSize(600, 700))
        self.Title.setMaximumSize(QtCore.QSize(600, 701))
        self.Title.setObjectName("Title")
        self.IssuesTable = QtWidgets.QTableView(self.centralwidget)
        self.IssuesTable.setGeometry(QtCore.QRect(50, 90, 500, 500))
        self.IssuesTable.setObjectName("IssuesTable")
        self.GoBack = QtWidgets.QPushButton(self.centralwidget)
        self.GoBack.setGeometry(QtCore.QRect(200, 620, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.GoBack.setFont(font)
        self.GoBack.setObjectName("GoBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:4.125pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">All Issues</span></p></body></html>"))
        self.GoBack.setText(_translate("MainWindow", "Go Back"))


