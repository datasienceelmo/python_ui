# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QBoxLayout, QDialog, QMenuBar, QMenu, \
    QVBoxLayout, QGroupBox, QGridLayout, QLineEdit, QTextEdit


class Bildschirm(QDialog):

    def __init__(self):
        super(Bildschirm, self).__init__()

        self.createHeader()
        self.createBody()


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.gridHeader)
        mainLayout.addWidget(self.gridBody)
        self.setLayout(mainLayout)

        self.showFullScreen()

        self.setWindowTitle("Information Produktion")

    def createHeader(self):
        self.gridHeader = QGroupBox("Maschine 1: Status")
        layout = QGridLayout()

        ##### Label Status #####
        labelStatus = QLabel()
        labelStatusFont = QFont("CorpoS", 20, QFont.Normal)
        labelStatus.setText("Produkt in Arbeit ...")
        labelStatus.setFont(labelStatusFont)
        labelStatus.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        labelStatus.setAutoFillBackground(True)
        greenColor = QColor(0, 255, 0)
        yellowColor = QColor(255, 255, 0)
        redColor = QColor(255, 0, 0)
        alpha = 150
        values = "{r}, {g}, {b}, {a}".format(r=yellowColor.red(),
                                             g=yellowColor.green(),
                                             b=yellowColor.blue(),
                                             a=alpha
                                             )
        labelStatus.setStyleSheet("QLabel { background-color: rgba(" + values + "); }")
        layout.addWidget(labelStatus, 0, 0)


        ##### Label Countdown #####
        labelCountdown = QLabel()
        labelCountdownFont = QFont("CorpoS", 20, QFont.Bold)
        labelCountdown.setText("12 sec")
        labelCountdown.setFont(labelCountdownFont)
        labelCountdown.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        layout.addWidget(labelCountdown, 0 , 1)


        layout.setColumnStretch(0, 20)
        layout.setColumnStretch(1, 10)
        self.gridHeader.setLayout(layout)


    def createBody(self):
        self.gridBody = QGroupBox("Produktdatenblatt")
        layout = QGridLayout()

        ##### Artikelnummer #####
        labelArtikelnummer = QLabel()
        lineEditArtikelnummer = QLineEdit()

        labelArtikelnummerFont = QFont("CorpoS", 14, QFont.Bold)
        labelArtikelnummer.setText("Artikelnummer:")
        labelArtikelnummer.setFont(labelArtikelnummerFont)
        labelArtikelnummer.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        lineEditArtikelnummer.setReadOnly(True)
        lineEditArtikelnummerFont = QFont("CorpoS", 12, QFont.Normal)
        lineEditArtikelnummer.setText("1234567890")
        lineEditArtikelnummer.setFont(lineEditArtikelnummerFont)

        layout.addWidget(labelArtikelnummer, 0, 0)
        layout.addWidget(lineEditArtikelnummer, 0, 1)


        ##### Bezeichnung #####
        labelBezeichnung = QLabel()
        textEditBezeichnung = QTextEdit()

        labelBezeichnungFont = QFont("CorpoS", 14, QFont.Normal)
        labelBezeichnung.setText("Bezeichnung:")
        labelBezeichnung.setFont(labelBezeichnungFont)
        labelBezeichnung.setAlignment(Qt.AlignTop | Qt.AlignRight)

        textEditBezeichnung.setReadOnly(True)
        textEditBezeichnungFont = QFont("CorpoS", 12, QFont.Normal)
        textEditBezeichnung.setText("Das ist ein blaues Produkt. Die Fertigungszeit betraegt Sekunden")
        textEditBezeichnung.setFont(textEditBezeichnungFont)

        layout.addWidget(labelBezeichnung, 1, 0)
        layout.addWidget(textEditBezeichnung, 1, 1)


        ##### Status #####
        labelStatus = QLabel()
        lineEditStatus = QLineEdit()

        labelStatusFont = QFont("CorpoS", 14, QFont.Normal)
        labelStatus.setText("Status:")
        labelStatus.setFont(labelStatusFont)
        labelStatus.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        lineEditStatus.setReadOnly(True)
        lineEditStatusFont = QFont("CorpoS", 12, QFont.Normal)
        lineEditStatus.setText("Statuscode: 2")
        lineEditStatus.setFont(lineEditStatusFont)

        layout.addWidget(labelStatus, 2, 0)
        layout.addWidget(lineEditStatus, 2, 1)


        ##### Durchlaufzeit #####
        labelDurchlaufzeit = QLabel()
        lineEditDurchlaufzeit = QLineEdit()

        labelDurchlaufzeitFont = QFont("CorpoS", 14, QFont.Normal)
        labelDurchlaufzeit.setText("Durchlaufzeit:")
        labelDurchlaufzeit.setFont(labelDurchlaufzeitFont)
        labelDurchlaufzeit.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        lineEditDurchlaufzeit.setReadOnly(True)
        lineEditDurchlaufzeitFont = QFont("CorpoS", 12, QFont.Normal)
        lineEditDurchlaufzeit.setText("30 sec")
        lineEditDurchlaufzeit.setFont(lineEditDurchlaufzeitFont)

        layout.addWidget(labelDurchlaufzeit, 3, 0)
        layout.addWidget(lineEditDurchlaufzeit, 3, 1)


        ##### Qualitaet #####
        labelQualitaet = QLabel()
        lineEditQualitaet = QLineEdit()

        labelQualitaetFont = QFont("CorpoS", 14, QFont.Normal)
        labelQualitaet.setText("Qualitaet")
        labelQualitaet.setFont(labelQualitaetFont)
        labelQualitaet.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        lineEditQualitaet.setReadOnly(True)
        lineEditQualitaetFont = QFont("CorpoS", 12, QFont.Normal)
        lineEditQualitaet.setText("100 %")
        lineEditQualitaet.setFont(lineEditQualitaetFont)

        layout.addWidget(labelQualitaet, 4, 0)
        layout.addWidget(lineEditQualitaet, 4, 1)


        self.gridBody.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Bildschirm()
    sys.exit(d.exec_())