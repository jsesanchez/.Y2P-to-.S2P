import numpy
import math as mt
#Variables
fr = ""
FT = 0
yi = ""
yo = ""
yr = ""
yf = ""
MAG = ""
c = ""
Yi = ""
Yo = ""
Gt = ""
donde = ""
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
    global yr, yf, yo, yi, donde
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
        #Se arregla el valor de frecuencia
        if fr=="Mhz":
            freq=float(clean_data[0])
            #print freq ," Mhz"
        elif fr=="Hz":
            freq=float(clean_data[0])/1000000
            #print freq," Hz"
        elif fr=="Khz":
            freq=float(clean_data[0])/1000
            #print freq," Khz"
        elif fr=="Ghz":
            freq=float(clean_data[0])*1000
            #print freq," Ghz"
        Yi = complex(float(clean_data[1]),float(clean_data[2]))
        if freq==float(FT):
            yi=Yi
            print "Con F=",FT," yi=",yi
        Yf = complex(float(clean_data[3]),float(clean_data[4]))
        if freq==float(FT):
            yf=Yf
            print "Con F=",FT," yf=",yf
        Yr = complex(float(clean_data[5]),float(clean_data[6]))
        if freq==float(FT):
            yr=Yr
            print "Con F=",FT," yr=",yr
        Yo = complex(float(clean_data[7]),float(clean_data[8]))
        if freq==float(FT):
            yo=Yo
            print "Con F=",FT," yo=",yo

def crear():
    global yr, yf, yo, yi,donde
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

        print "Archivo creado exitosamente:\nNombre del archivo:resultado.s2p\nUbicacion:Esta carpeta\n\nFrecuencias="
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
                print freq ," Mhz"

            elif fr=="Hz":
                #print "\nLa frecuencia esta en Hz"
                freq=float(clean_data[0])/1000000
                archi.write(str(freq))
                archi.write(" ")
                print freq," Hz"
            elif fr=="Khz":
                #print "\nLa frecuencia esta en Khz"
                freq=float(clean_data[0])/1000
                archi.write(str(freq))
                archi.write(" ")
                print freq," Khz"
            elif fr=="Ghz":
                #print "\nLa frecuencia esta en Ghz"
                freq=float(clean_data[0])*1000
                archi.write(str(freq))
                archi.write(" ")
                print freq," Ghz"
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
        #print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","Archivo creado con exito"

# Estabilidad Linville
def linv():
    leer()
    #print yr, "     " ,yf
    y=(yr)*(yf)
    c=abs(y)/(2*(yi.real*yo.real)-(y.real))
    print "\nEl factor de estabilidad es= ", c

# Evaluacion de los parametros de transitor estable

def yio():
    global MAG, Yi, Yo, Gt
    y=yr*yf
    sq=((2*yi.real*yo.real-(y.real)))**2-((abs(y))**2)
    print sq
    N=mt.sqrt(sq)
    Gi=N/(2*yo.real)
    Go=N/(2*yi.real)
    Bo=yo.imag-ym.imag/(2*yi.real)
    Bi=yi.imag-ym.imag/(2*yo.real)
    Yi=Gi+Bi*1j
    Yo=Go+Bo*1j
    MAG=((abs(yf))**2)/(4*yi.real*yo.real)
    print "\nLa MAG es= ", MAG
    Gt=((abs(yf))**2)/(((2*yi.real*yo.real-(y.real)))+N)



# Diseno de amplifcador inestabeles
def sturn():
    global MAG, Yi, Yo, Gt
    k=int(input("digite el valor de estabilidad K deseado: "))
    Rs=int(input("Digite el valor de Rs para mejor figura de ruido: "))
    y=yr*yf
    c=abs(y)/(2*(yi.real*yo.real)-(y.real))
    gl=(k*(abs(y)+y.real)/(2*((yi.real)+1000/Rs)))-yo.real
    Yo=yo
    Yi=yi-(y/(yo+(gl-Yo.imag*1j)))
    i=int(input("Indique el No. de iteraciones: "))

    while i!=0:
            Yo=yo-(y/(yi+(1000/Rs-Yi.imag*1j)))
            Yi=yi-(y/(yo+(gl-Yo.imag*1j)))
            i-=1
            #print("Yi,Yo", Yi, Yo)

    Ys=(Yi.real-Yi.imag*1j)
    Yl=(gl-Yo.imag*1j)
    D=abs((yi+Ys)*(yo+Yl)-y)
    Gt=4*gl*(Yi.real)*(abs(yf)**2)/(D**2)
    return Ys, Yl, Gt

crear()
pregunta()
linv()
if 0<c<1:
    print "Es un amplifcador estable"
    yio()
else:
    print "El transitor es inestable"
