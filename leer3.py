import numpy
import math as mt
#Variables globales
fr = ""
FT = 0
gi=""
bi=""
go=""
bo=""
gr=""
br=""
gf=""
bf=""
yi = ""
yo = ""
yr = ""
yf = ""
yif=""
yff=""
yrf=""
yof=""
MAG = ""
k=""
c = ""
Yi = ""
Yo = ""
Gt = ""
paila=1
donde = ""
innes=0
error=0
what=0
analisis=0
todas=2

def inicio():
    global what
    what = raw_input("\n"+"En este programa usted podra convertir archivos .y2p a .s2p, "+
                      "tambien realizar un analisis de este, mirando las frecuencias "+
                      "del dispositivo, sus respectivos parametros y un analisis "+
                      "para la realizacion de un amplificador RF, tambien podra ingresar "+
                      "manualmente los parametros S o Y."+" \n"+" \n"+
                      "Programa realizado por el Grupo de trabajo GNU/Linux de la Universidad "+
                      "Distrital Francisco Jose de Caldas (GLUD)."+" \n"+" \n"+
                      "Para mas informacion:"+" \n"+" \n"+
                      "www.glud.org"+" \n"+
                      "www.semanalinuxud.com"+" \n"+
                      "www.github.com/glud "+" \n"+" \n"+"Digite 0 para ingresar un archivo .Y2P."+" \n"+
                      "Digite 1 para ingresar manualmente los parametros Y."+" \n"+" \n"+
                      "Que desea hacer? = ")
def preanali():
    global analisis
    analisis=raw_input("\nDesea analizar el archivo? (1 = Si, 0 = No) ")
def fre(string):
    s = string.split()
    if s[0] == '!':
        if s[1] in ['Hz', 'Khz', 'Ghz', 'Mhz']:

            return s[1]
        return ""
    return ""
def pregunta():
    global FT
    FT = raw_input("\nEn que frecuencia desea trabajar? (Solo valor numerico): ")
def leer():
    global yr, yf, yo, yi,yif,yrf,yof,yff, donde, error, paila
    f=open(donde, 'rb')
    ls=f.readlines()
    linea=0
    for i,j in zip (ls,range(len(ls))):
        #print(fre(i[0:5]))
        ab = fre(i[0:5])
        if ab:
            fr = ab
            linea=j
            columna=i
    for i in range(linea+1,len(ls)):
        datos =  filter(None, (ls[i].replace(" ","\t")).split("\t"))
        clean_data = filter(None, [i.replace("\r\n",'') for i in datos])
        freq=float(clean_data[0])
        Yi = complex(float(clean_data[1]),float(clean_data[2]))
        yi=Yi
        Yf = complex(float(clean_data[3]),float(clean_data[4]))
        yf=Yf
        Yr = complex(float(clean_data[5]),float(clean_data[6]))
        yr=Yr
        Yo = complex(float(clean_data[7]),float(clean_data[8]))
        yo=Yo
        #print innes
        if innes==0:
            if freq==float(FT):
                yif=yi
                yof=yo
                yrf=yr
                yff=yf
                print "Con F=",FT," yi=",yi
                print "Con F=",FT," yf=",yf
                print "Con F=",FT," yr=",yr
                print "Con F=",FT," yo=",yo
        else:
            y=(yr)*(yf)
            c=abs(y)/(2*(yi.real*yo.real)-(y.real))
            c=abs(y)/(2*(yi.real*yo.real)-(y.real))
            #print c
            if 0<c<1:
                print "\nEl amplifcador es estable a:"
                print "\nF=",freq," C=",c
                paila=1
            else:
                paila=0
def crear():
    global yr, yf, yo, yi,donde,error
    donde = raw_input("Ingrese la direccion del archivo: ").replace(" ", "")
    print "\nLa ruta es:", donde
    l=len(donde)
    a=".y2p"

    if donde[l-4:l]==a:
        f=open(donde, 'rb')	#Se abre el archivo .y2p
        ls=f.readlines()        	#Se lee el archivo
        linea=0
        archi=open('resultado.s2p','w')	#Se crea el archivo .s2p
        #Escritura de lineas fijas
        archi.write('!Archivo .S2P a partir de .Y2P\n')
        archi.write('!Autor: Jonnathan Sebastian Sanchez Sanabria\n')
        archi.write('!Grupo de trabajo GNU/Linux Universidad Distrital (GLUD)\n')
        archi.write('!License: GPLv3\n')
        archi.write('!Year:2017\n')

        archi.write('!Freq.(MHz) S11(Real) S11(Imag) S21(Real) S21(Imag) S12(Real) S12(Imag) S22(Real) S22(Imag)\n')
            #archi.write('Linea 3\n')
            #archi.close()

        for i,j in zip (ls,range(len(ls))):
            #print(fre(i[0:5]))
            ab = fre(i[0:5])

            if ab:
                fr = ab
                linea=j
                columna=i

        print "Archivo creado exitosamente:\nNombre del archivo:resultado.s2p\nUbicacion:Esta carpeta\n"
        #print linea,len(ls)
        compi = []
        for i in range(linea+1,len(ls)):
            datos =  filter(None, (ls[i].replace(" ","\t")).split("\t"))
            clean_data = filter(None, [i.replace("\r\n",'') for i in datos])
            #Se arregla el valor de frecuencia
            if fr=="Mhz":
                #print "\nLa frecuencia esta en Mhz"
                freq=float(clean_data[0])
                archi.write(str(freq))
                archi.write(" ")
                #print float(clean_data[0]) ," Mhz"

            elif fr=="Hz":
                #print "\nLa frecuencia esta en Hz"
                freq=float(clean_data[0])/1000000
                archi.write(str(freq))
                archi.write(" ")
                #print float(clean_data[0]) ," Hz"
            elif fr=="Khz":
                #print "\nLa frecuencia esta en Khz"
                freq=float(clean_data[0])/1000
                archi.write(str(freq))
                archi.write(" ")
                #print float(clean_data[0]) ," Khz"
            elif fr=="Ghz":
                #print "\nLa frecuencia esta en Ghz"
                freq=float(clean_data[0])*1000
                archi.write(str(freq))
                archi.write(" ")
                #print float(clean_data[0]) ," Ghz"
            Yi = complex(float(clean_data[1]),float(clean_data[2]))
            Yf = complex(float(clean_data[3]),float(clean_data[4]))
            Yr = complex(float(clean_data[5]),float(clean_data[6]))
            Yo = complex(float(clean_data[7]),float(clean_data[8]))

            vares = [Yi,Yf,Yr,Yo]
            compi.append(vares)
            #print "Parametros Y"
            #print Yi,Yr,Yf,Yo
            S11=((1-Yi)*(1+Yo)+(Yr*Yf))/((1-Yi)*(1+Yo)-(Yr*Yf))		#S11
            #archi.write(str(S11))
            s11real=S11.real
            s11imag=S11.imag
            archi.write(str(s11real))
            archi.write(" ")
            archi.write(str(s11imag))
            S12=((-2*Yr)/((1+Yi)*(1+Yo)-(Yr*Yf)))			        #S12
            s12real=S12.real
            s12imag=S12.imag
            archi.write(str(s12real))
            archi.write(" ")
            archi.write(str(s12imag))
            archi.write(" ")
            S21=((-2*Yf)/((1+Yi)*(1+Yo)-(Yr*Yf)))			        #S21
            s21real=S21.real
            s21imag=S21.imag
            archi.write(str(s21real))
            archi.write(" ")
            archi.write(str(s21imag))
            archi.write(" ")
            S22=(((1+Yi)*(1-Yo)+(Yr*Yf))/((1+Yi)*(1+Yo)-(Yr*Yf)))   #S22
            s22real=S22.real
            s22imag=S22.imag
            archi.write(str(s22real))
            archi.write(" ")
            archi.write(str(s22imag))
            archi.write("\n")
            #print "Parametros S"
            #print S11,S12,S21,S22

    else:
        print "La ruta no llega a un archivo .y2p\nError de capa 8"
        error=1
        print error
        #print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","Archivo creado con exito"
# Estabilidad Linville
def linv():
    if what==0:
        leer()
    global c,yr,yf,yi,yoyif,yrf,yof,yff
    #print "\nyi= ", yif
    #print "\nyo= ", yof
    #print "\nyr= ", yrf
    #print "\nyf= ", yff
    y=(yrf)*(yff)
    c=abs(y)/(2*(yif.real*yof.real)-(y.real))
    print "\nEl factor de estabilidad es= ", c
    if 0<c<1:
        print "\nA esta frecuencia es un amplifcador estable"
    else:
        print "\nA esta frecuencia es un amplifcador inestable"
def Sturn():
    if what==0:
        leer()
    global k,yr,yf,yi,yoyif,yrf,yof,yff,gi,bi,go,bo,gr,br,gf,bf
    #print "\nyi= ", yif
    #print "\nyo= ", yof
    #print "\nyr= ", yrf
    #print "\nyf= ", yff
    y=2(float(gi)+float(gg))*(float(go)+float(gl))
    k=(y)/(abs(yff+yrf)+(yr.real*yf.real))
    print "\nEl factor de estabilidad es= ", k
    if k<1:
        print "\nA esta frecuencia es un amplifcador estable"
    else:
        print "\nA esta frecuencia es un amplifcador inestable"
# Evaluacion de los parametros de transitor estable
def yio():
    global MAG, Yi, Yo, Gt
    y=yr*yf
    sq=((2*yi.real*yo.real-(y.real)))**2-((abs(y))**2)
    #print sq
    N=mt.sqrt(sq)
    Gi=N/(2*yo.real)
    Go=N/(2*yi.real)
    Bo=yo.imag-y.imag/(2*yi.real)
    Bi=yi.imag-y.imag/(2*yo.real)
    Yi=Gi+Bi*1j
    Yo=Go+Bo*1j
    MAG=((abs(yf))**2)/(4*yi.real*yo.real)
    print "\nLa MAG es= ", MAG
    print "\nLas impedancias de entrada y salida son:"
    print "\nYi= ", Yi
    print "\nYo= ", Yo
    Gt=((abs(yf))**2)/(((2*yi.real*yo.real-(y.real)))+N)
#Se analiza el archivo
def analizar():
    #print "Entro"
    f=open(donde, 'rb')	#Se abre el archivo .y2p
    ls=f.readlines()        	#Se lee el archivo
    linea=0
    for i,j in zip (ls,range(len(ls))):
        #print(fre(i[0:5]))
        ab = fre(i[0:5])

        if ab:
            fr = ab
            linea=j
            columna=i
    compi = []
    for i in range(linea+1,len(ls)):
        datos =  filter(None, (ls[i].replace(" ","\t")).split("\t"))
        clean_data = filter(None, [i.replace("\r\n",'') for i in datos])
        #Se arregla el valor de frecuencia
        if fr=="Mhz":
            #print "\nLa frecuencia esta en Mhz"
            freq=float(clean_data[0])
            print float(clean_data[0]) ," Mhz"

        elif fr=="Hz":
            #print "\nLa frecuencia esta en Hz"
            freq=float(clean_data[0])/1000000
            print float(clean_data[0]) ," Hz"
        elif fr=="Khz":
            #print "\nLa frecuencia esta en Khz"
            freq=float(clean_data[0])/1000
            print float(clean_data[0]) ," Khz"
        elif fr=="Ghz":
            #print "\nLa frecuencia esta en Ghz"
            freq=float(clean_data[0])*1000
            print float(clean_data[0]) ," Ghz"





#program
inicio()
evalu=what.isdigit()
if str(evalu)=="True":
    if float(what)==0 or float(what)==1:
        if float(what)==0:
            crear()
            if error==0:
                preanali()
                #print " Valor de error=",error
                if float(analisis)==1:
                    analizar()
                    #innes=1
                    pregunta()
                    linv()
                    #print "Valor de c=",c,"  Valor de error=",error
                    if 0<c<1:
                        print "\nAnalisis del amplificador estable\n"
                        yio()
                    else:
                        rta=raw_input("\nDesea saber a que frecuencias el amplificador es estable? (1 = Si, 0 = No) ")
                        if float(rta)==1:
                            innes=1
                            leer()
                            if float(paila)==0:
                                print "\nEl amplificador es inestable para todas las frecuencias."
                        else:
                            print "\nBueno, como quiera!"
                    #Sturn()
                else:
                    print "\nFin"
        if float(what)==1:
            print "\nIngrese los datos de la siguiente forma: (ejm) gi=1.25  bi=-2\n"
            gi=raw_input("\ngi= ").replace(" ", "")
            bi=raw_input("bi= ").replace(" ", "")
            gr=raw_input("gr= ").replace(" ", "")
            br=raw_input("br= ").replace(" ", "")
            gf=raw_input("gf= ").replace(" ", "")
            bf=raw_input("bf= ").replace(" ", "")
            go=raw_input("go= ").replace(" ", "")
            bo=raw_input("bo= ").replace(" ", "")
            yif=complex(float(gi),float(bi))
            yof=complex(float(go),float(bo))
            yff=complex(float(gf),float(bf))
            yrf=complex(float(gr),float(br))
            print "\nLos parametros son:\n"
            print "yi= ", yif
            print "yr= ", yrf
            print "yo= ", yof
            print "yf= ", yff
            linv()
            #Sturn()
            print "\nBueno"
    else:
        print "\nJa Ja Ja... NO"
else:
    print "\n\n...No sabes leer?"
