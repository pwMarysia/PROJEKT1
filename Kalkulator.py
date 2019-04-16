# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:39:07 2019

@author: Maria
"""

import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QColorDialog
from math import pi, atan, sqrt
import itertools


class KALKULATOR(QWidget): #stworzenie klasy
    def __init__(self):
        super().__init__()
        self.title = 'Kalkulator3000'
        self.kol1='r'
        self.kol2='blue'
        self.initInterface()
        self.initWidgets()


    def initInterface(self): #parametry okna aplikacji
        self.setWindowTitle(self.title)
        self.setGeometry(150, 30, 1000, 680)
        self.show()
    
    def initWidgets(self): #GUI wraz z widgetami
        btn=QPushButton('oblicz', self) #przyciski
        buton=QPushButton('eksportuj dane', self)
        baton=QPushButton('wyczysc dane', self)
        zmiana1=QPushButton('zmien kolor prostej AB',self)
        zmiana2=QPushButton('zmień kolor prostej CD',self)
        label=QLabel('Wprowadź dane:', self)
        xa=QLabel('Xa', self) #etykiety
        ya=QLabel('Ya', self)
        xb=QLabel('Xb', self)
        yb=QLabel('Yb', self)
        xc=QLabel('Xc', self)
        yc=QLabel('Yc', self)
        xd=QLabel('Xd', self)
        yd=QLabel('Yd', self)
        yp=QLabel('Xp', self)
        xp=QLabel('Yp', self)
        p=QLabel('P', self)
        azymut1=QLabel('Aab', self)
        azymut2=QLabel('Acd', self)
        dlugoscab=QLabel('Dab', self)
        dlugosccd=QLabel('Dcd', self)
        xp=QLabel('Yp', self)
        self.Xa = QLineEdit() #okna edycji
        self.Ya = QLineEdit()
        self.Xb = QLineEdit()
        self.Yb = QLineEdit()
        self.Xc = QLineEdit()
        self.Yc = QLineEdit()
        self.Xd = QLineEdit()
        self.Yd = QLineEdit()
        self.Xp = QLineEdit()
        self.Yp = QLineEdit()
        self.info = QLineEdit()
        self.Az_ab= QLineEdit()
        self.Az_cd = QLineEdit()
        self.dlab = QLineEdit()
        self.dlcd = QLineEdit()
        

        
        self.figure = plt.figure() #wykres
        self.canvas = FigureCanvas(self.figure)
        
        #umiejscowienie stworzonych widgetów w oknie aplikacji
        grid = QGridLayout()
        grid.addWidget(label, 0, 0)
        grid.addWidget(xa, 1, 0)
        grid.addWidget(ya, 2, 0)
        grid.addWidget(xb, 3, 0)
        grid.addWidget(yb, 4, 0)
        grid.addWidget(xc, 5, 0)
        grid.addWidget(yc, 6, 0)
        grid.addWidget(xd, 7, 0)
        grid.addWidget(yd, 8, 0)
        grid.addWidget(yp, 10, 2)
        grid.addWidget(xp, 11, 2)
        grid.addWidget(p, 12, 2)
        grid.addWidget(dlugoscab, 15, 2)
        grid.addWidget(dlugosccd, 16, 2)
        grid.addWidget(azymut1, 13, 2)
        grid.addWidget(azymut2, 14, 2)
        grid.addWidget(self.Xa, 1, 1)
        grid.addWidget(self.Ya, 2, 1)
        grid.addWidget(self.Xb, 3, 1)
        grid.addWidget(self.Yb, 4, 1)
        grid.addWidget(self.Xc, 5, 1)
        grid.addWidget(self.Yc, 6, 1)
        grid.addWidget(self.Xd, 7, 1)
        grid.addWidget(self.Yd, 8, 1)
        grid.addWidget(self.Xp, 10, 3)
        grid.addWidget(self.Yp, 11, 3)
        grid.addWidget(self.Az_ab, 13, 3)
        grid.addWidget(self.Az_cd, 14, 3)
        grid.addWidget(self.dlab, 15, 3)
        grid.addWidget(self.dlcd, 16, 3)
        grid.addWidget(self.info, 12, 3)
        grid.addWidget(btn, 15, 0, 1, 2)
        grid.addWidget(baton, 20, 0, 1, 2)
        grid.addWidget(buton,21, 0, 1, 2)

        grid.addWidget(self.canvas,2,30,30,100)
        
        grid.addWidget(zmiana1,2,3,2,2)
        grid.addWidget(zmiana2,3,3,2,2)
        self.setLayout(grid)
        
        #przyporządkowanie funkcji do sygnałów przycisków
        btn.clicked.connect(self.punktP)
        btn.clicked.connect(self.azymut)
        btn.clicked.connect(self.dlugosc)
        btn.clicked.connect(self.kolor)
        buton.clicked.connect(self.export)
        baton.clicked.connect(self.wyczysc)
        zmiana1.clicked.connect(self.zmienKolor1)
        zmiana2.clicked.connect(self.zmienKolor2)
        


       

    def punktP(self,col_1='blue', col_2='red'): 
        #pobranie danych od użytkownika i sprawdzenie czy są to liczby
        axx=self.sprawdzWartosc(self.Xa)
        ay=self.sprawdzWartosc(self.Ya)
        bx=self.sprawdzWartosc(self.Xb)
        by=self.sprawdzWartosc(self.Yb)
        cx=self.sprawdzWartosc(self.Xc)
        cy=self.sprawdzWartosc(self.Yc)
        dx=self.sprawdzWartosc(self.Xd)
        dy=self.sprawdzWartosc(self.Yd)
        
        #obliczenie współrzędnych punktu P
        if (bx-axx)*(dy-cy)-(by-ay)*(dx-cx)==0:
            self.info.setText(str('Proste są równległe'))
            ax=self.figure.add_subplot(111)
            X_ab=[axx,bx]
            Y_ab=[ay,by]
            X_cd=[cx,dx]
            Y_cd=[cy,dy]
            #narysowanie wykresu jesli linie są równoległe (nie ma wtedy 
            #punktu P więc pętla nie jest kontynuowana)
            fontsizes = itertools.cycle([16, 16, 16, 16])
            ax.set_xlabel('x', fontsize=next(fontsizes))
            ax.set_ylabel('y', fontsize=next(fontsizes))
            ax.set_title('Położenie prostych i punktu P', fontsize=next(fontsizes))
            ax.plot(X_ab,Y_ab, self.kol1)
            ax.plot(X_cd,Y_cd, self.kol2)
            ax.plot(axx,ay,'ro')
            ax.plot(bx,by,'ro')
            ax.plot(cx,cy,'bo')
            ax.plot(dx,dy,'bo')
            ax.text(axx, ay, '  A  %d,%d' % (int(axx),int(ay)))
            ax.text(bx, by, '  B  %d,%d' % (int(bx),int(by)))
            ax.text(cx, cy, '  C  %d,%d' % (int(cx),int(cy)))
            ax.text(dx, dy, '  D  %d,%d' % (int(dx),int(dy)))
            self.canvas.draw()
            
        else:
            t1=((cx-axx)*(dy-cy)-(cy-ay)*(dx-cx))/((bx-axx)*(dy-cy)-(by-ay)*(dx-cx))
            t2=((cx-axx)*(dy-ay)-(cy-ay)*(bx-axx))/((bx-axx)*(dy-cy)-(by-ay)*(dx-cx))
        
            #współrzędne punktu i informacja gdzie się znajduje względem linii
            if (t1>=0 and t1<=1) and (t2>=0 and t2<=1):
                px=axx+t1*(bx-axx)
                py=ay+t1*(by-ay)
                pX=round(px,3)
                pY=round(py,3)
                self.Yp.setText(str(pY))
                self.Xp.setText(str(pX))
                self.info.setText(str('leży na przecięciu prostych'))
            elif (t1<0 or t1>1) and (t2<0 or t2>1):
                px=axx+t1*(bx-axx)
                py=ay+t1*(by-ay)
                pX=round(px,3)
                pY=round(py,3)
                self.Yp.setText(str(pY))
                self.Xp.setText(str(pX))
                self.info.setText(str('leży na przedłużeniu odcinków'))
            elif (t1<0 or t1>1) and (t2>=0 and t2<=1):
                px=axx+t1*(bx-axx)
                py=ay+t1*(by-ay)
                pX=round(px,3)
                pY=round(py,3)
                self.Yp.setText(str(pY))
                self.Xp.setText(str(pX))
                self.info.setText(str('leży na odcinku CD'))
            elif (t1>=0 and t1<=1) and (t2<0 or t2>1):
                px=axx+t1*(bx-axx)
                py=ay+t1*(by-ay)
                pX=round(px,3)
                pY=round(py,3)
                self.Yp.setText(str(pY))
                self.Xp.setText(str(pX))
                self.info.setText(str('leży na odcinku AB'))

#                


        axx=self.sprawdzWartosc(self.Xa)
        ay=self.sprawdzWartosc(self.Ya)
        bx=self.sprawdzWartosc(self.Xb)
        by=self.sprawdzWartosc(self.Yb)
        cx=self.sprawdzWartosc(self.Xc)
        cy=self.sprawdzWartosc(self.Yc)
        dx=self.sprawdzWartosc(self.Xd)
        dy=self.sprawdzWartosc(self.Yd)
        px=self.sprawdzWartosc(self.Xp)
        py=self.sprawdzWartosc(self.Yp)
               
        X_ab=[axx,bx]
        Y_ab=[ay,by]
        X_cd=[cx,dx]
        Y_cd=[cy,dy]
        Y_ap=[ay,py]
        X_ap=[axx,px]
        Y_cp=[cy,py]
        X_cp=[cx,px]
        #rysowanie wykresu
        ax=self.figure.add_subplot(111)
        #kod odpowiedzialny za podpisy osi, tytuł i ich wielkosc
        fontsizes = itertools.cycle([16, 16, 16, 16])
        ax.set_xlabel('x', fontsize=next(fontsizes))
        ax.set_ylabel('y', fontsize=next(fontsizes))
        ax.set_title('Położenie prostych i punktu P', fontsize=next(fontsizes))
        #linie przerywane i ciągłe
        ax.plot(X_ap,Y_ap, 'green', linestyle='dashed')
        ax.plot(X_cp,Y_cp, 'green', linestyle='dashed')
        ax.plot(X_ab,Y_ab, self.kol1)
        ax.plot(X_cd,Y_cd, self.kol2)
        #umieszczenie kropek w miejscu współrzędnych punktów
        ax.plot(axx,ay,'ro')
        ax.plot(bx,by,'ro')
        ax.plot(cx,cy,'bo')
        ax.plot(dx,dy,'bo')
        ax.plot(px,py,'yo')
        #podpisanie tych kropek nazwą pktu i współrzędnymi (liczby całkowite, 
        #x i y po przecinku)
        ax.text(axx, ay, '  A  %d,%d' % (int(axx),int(ay)))
        ax.text(bx, by, '  B  %d,%d' % (int(bx),int(by)))
        ax.text(cx, cy, '  C  %d,%d' % (int(cx),int(cy)))
        ax.text(dx, dy, '  D  %d,%d' % (int(dx),int(dy)))
        ax.text(px, py, '  P  %d,%d' % (int(px),int(py)))
        self.canvas.draw()


        
   
    def azymut(self):
        
        axx=self.sprawdzWartosc(self.Xa)
        ay=self.sprawdzWartosc(self.Ya)
        bx=self.sprawdzWartosc(self.Xb)
        by=self.sprawdzWartosc(self.Yb)
        cx=self.sprawdzWartosc(self.Xc)
        cy=self.sprawdzWartosc(self.Yc)
        dx=self.sprawdzWartosc(self.Xd)
        dy=self.sprawdzWartosc(self.Yd)
        
        dxab=bx-axx
        dyab=by-ay
        dxcd=dx-cx
        dycd=dy-cy
        #obliczenie aymutów narysowanych linii
        if dxab>0 and dyab>0:
            Azab=atan(abs(dyab)/abs(dxab))
        elif dxab<0 and dyab>0:
            Azab=pi-atan(abs(dyab)/abs(dxab))
        elif dxab<0 and dyab<0:
            Azab=pi+atan(abs(dyab)/abs(dxab))
        elif dxab>0 and dyab<0:
            Azab=2*pi-atan(abs(dyab)/abs(dxab)) 
        elif dxab==0 and dyab==0:
            Azab=0
        elif dxab>0 and dyab==0:
            Azab=pi/2
        elif dxab<0 and dyab==0:
            Azab=3*pi/2
        elif dxab==0 and dyab>0:
            Azab=2*pi
        elif dxab==0 and dyab<0:
            Azab=pi
            
        
        if dxcd>0 and dycd>0:
            Azcd=atan(abs(dycd)/abs(dxcd))
        elif dxcd<0 and dycd>0:
            Azcd=pi-atan(abs(dycd)/abs(dxcd))
        elif dxcd<0 and dycd<0:
            Azcd=pi+atan(abs(dycd)/abs(dxcd))
        elif dxcd>0 and dycd<0:
            Azcd=2*pi-atan(abs(dycd)/abs(dxcd))
        elif dxcd==0 and dycd==0:
            Azcd=0
        elif dxcd>0 and dycd==0:
            Azcd=pi/2
        elif dxcd<0 and dycd==0:
            Azcd=3*pi/2
        elif dxcd==0 and dycd>0:
            Azcd=2*pi
        elif dxcd==0 and dycd<0:
            Azcd=pi
            
        Azcd1=Azcd*(200/pi)
        Azcd11=round(Azcd1,4)
        #wywietlenie liczb w przeznaczonych do tego oknach   
        self.Az_cd.setText(str(Azcd11))            
            
         
        Azab1=Azab*(200/pi)
        Azab11=round(Azab1,4)    
        self.Az_ab.setText(str(Azab11))    
            
    
        
    def wyczysc(self):
        #wyczyszczenie podanych danych i obliczonych wyników
        axx=self.Xa
        ay=self.Ya
        bx=self.Xb
        by=self.Yb
        cx=self.Xc
        cy=self.Yc
        dx=self.Xd
        dy=self.Yd
        px=self.Xp
        py=self.Yp
        P=self.info 
        A1=self.Az_ab
        A2=self.Az_cd
        D1=self.dlab
        D2=self.dlcd
        axx.clear()
        ay.clear()
        bx.clear()
        by.clear()
        cx.clear()
        cy.clear()
        dx.clear()
        dy.clear()
        px.clear()
        py.clear()
        P.clear()
        A1.clear()
        A2.clear()
        D1.clear()
        D2.clear()
        self.figure.clf()
        self.canvas.draw()
        
        
    def dlugosc(self):
        
        axx=self.sprawdzWartosc(self.Xa)
        ay=self.sprawdzWartosc(self.Ya)
        bx=self.sprawdzWartosc(self.Xb)
        by=self.sprawdzWartosc(self.Yb)
        cx=self.sprawdzWartosc(self.Xc)
        cy=self.sprawdzWartosc(self.Yc)
        dx=self.sprawdzWartosc(self.Xd)
        dy=self.sprawdzWartosc(self.Yd)
        #obliczenie długoci obu linii
        dl_1=sqrt((bx-axx)**2+(by-ay)**2)
        dl_2=sqrt((dx-cx)**2+(dy-cy)**2)
        dl_1r=round(dl_1, 3)
        dl_2r=round(dl_2, 3)
        #wyswietlenie wyników
        self.dlab.setText(str(dl_1r))
        self.dlcd.setText(str(dl_2r))
        
            
    def zmienKolor1(self): #zmiana koloru jednej linii
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name)
            self.kol1 = color.name()
            self.punktP()
            
    def zmienKolor2(self): #zmiana koloru drugiej linii
        color2 = QColorDialog.getColor()
        if color2.isValid():
            print(color2.name)
            self.kol2=color2.name()
            self.punktP()
            
    def kolor(self): #definicja łącząca linie ze zmianą koloru
        self.punktP()

        
        
    def sprawdzWartosc(self, element): 
        #definicja sprawdzająca czy wprowadzonedane są liczbami, 
        #jeli nie wywietla odpowiedni komunikat i wymusza prawidłowe dane
        if element.text().lstrip('-').replace('.','', 1).isdigit():
            return float(element.text())
        else: 
            element.setText('wpisz liczbę')
            return None
        
    def export(self):
        #funkcja odpowiedzialna za zapisanie obliczonych wyników w pliku tekstowym
        #pobiera i definiuje dane
        px=float(self.Xp.text())
        py=float(self.Yp.text())
        axx=float(self.Xa.text())
        ay=float(self.Ya.text())
        bx=float(self.Xb.text())
        by=float(self.Yb.text())
        cx=float(self.Xc.text())
        cy=float(self.Yc.text())
        dx=float(self.Xd.text())
        dy=float(self.Yd.text())
        D_ab=float(self.dlab.text())
        D_cd=float(self.dlcd.text())
        Az1=float(self.Az_ab.text())
        Az2=float(self.Az_cd.text())
        A2='A'
        B2='B'
        C2='C'
        D2='D'
        P2='P'
        E=open('EksportDanych.txt','w')
        #zdefiniowanie formatu zapisu danych (tabela)
        E.write('\n|{:^20}|{:^20}|{:20}|'.format('punkt','X','Y'))
        E.write('\n|{:^20}|{:^20.3f}|{:20.3f}|'.format(P2,px,py))
        E.write('\n|{:^20}|{:^20.3f}|{:20.3f}|'.format(A2,axx,ay))
        E.write('\n|{:^20}|{:^20.3f}|{:20.3f}|'.format(B2,bx,by))
        E.write('\n|{:^20}|{:^20.3f}|{:20.3f}|'.format(C2,cx,cy))
        E.write('\n|{:^20}|{:^20.3f}|{:20.3f}|'.format(D2,dx,dy))
        E.write('\n')
        E.write(60*'-')
        E.write('\n|{:^20}|{:^20}|{:20}|{:^20}|'.format('długosć AB','Azymut AB','długosć CD', 'Azymut CD'))
        E.write('\n|{:^20.3f}|{:^20.4f}|{:20.3f}|{:^20.4f}|'.format(D_ab,Az1,D_cd,Az2))
        E.write('\n')
        E.write(60*'-')
        E.close()

            
def main():
    app=QApplication(sys.argv)
    window = KALKULATOR()
    app.exec()
    
if __name__=='__main__':
    main()
    
#t1=((float(Cx)-float(Ax))*(float(Dy)-float(Cy))-(float(Cy)-float(Ay))*(float(Dx)-float(Cx)))/((float(Bx)-float(Ax))*(float(Dy)-float(Cy))-(float(By)-float(Ay))*(float(Dx)-float(Cx)))
#t2=((float(Cx)-float(Ax))*(float(Dy)-float(Ay))-(float(Cy)-float(Ay))*(float(Bx)-float(Ax)))/((float(Bx)-float(Ax))*(float(Dy)-float(Cy))-(float(By)-float(Ay))*(float(Dx)-float(Cx)))