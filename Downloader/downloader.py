from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys

import urllib.request


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton('DOWNLOAD')

        self.url.setPlaceholderText('enter URL')
        self.save_location.setPlaceholderText('select save location')

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle('Py Downloader')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFocus()

        download.clicked.connect(self.download)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(self, url, save_location, self.report)

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        percent = readsofar * 100 / totalsize

        self.progress.setValue(int(percent))


app = QApplication(sys.argv)
dl = Downloader()
dl.show()
dl.exec_()
