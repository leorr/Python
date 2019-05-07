import matplotlib.pyplot as plt
import numpy as np
#TODO given optional argument order or degree do the regression according
def lineregression(x,y):
    n = np.size(y)                          #tamanho amostral
    ym=0                                    #y medio
    for i in range(0,n):             
        ym=ym+y[i]
    ym=ym/n
    xm=0                                    #x medio
    for i in range(0,n):             
        xm=xm+x[i]
    xm=xm/n                                 
    sxx=0                                   #hipotese(metodo dos mínimos quadrados)
    sxy=0                                   #y = ax + b
    for i in range(0,n):                    #a = sxy/sxx
        sxx=(x[i]-xm)**2 + sxx              #b = ym - a * xm

    for i in range(0,n):
        sxy=(x[i]-xm)*(y[i]-ym) + sxy
    a=sxy/sxx
    b=ym-(a*xm)
    
    ye=[]
    for i in range(0,n):
        ye.append(a*x[i]+b)


    fig = plt.figure()                      
    ax = fig.add_subplot(111)               #preparando plots

    ax.plot(x,y,'.',label='pontos obtidos',color='magenta')
    ax.plot(x,ye,label='linha de regressão')
    SQres = 0
    for i in range(0,n):
        SQres= (y[i]-ye[i])**2 + SQres

    SQexp = 0
    for i in range(0,n):
        SQexp = (ye[i]-ym)**2 + SQexp
    SQtot = SQexp + SQres 
    R2=SQexp/SQtot
    #chisq=sum((y[i]-ye[i])/si)**2
    stdm=np.std(y)/np.sqrt(n)
    chisq=0
    for i in range(0,n,1):
        chisq=(((y[i]-ye[i])/stdm)**2) + chisq
    c2='χ²=' + str("{:.3f}".format(chisq))                          #convertendo chi quadrado para ser mostrado em texto
    R2='R²='+str("{:.3f}".format(R2))                               #coeficiente de correlação² em texto
    eq='y='+str(a) + 'x + ' + str(b) #equaçao da reta tem texto
    print(c2,R2,eq)

    plt.legend()
    plt.show()
#FIM DA FUNÇÃO
