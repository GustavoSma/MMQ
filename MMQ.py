'''
#ALGORITMO  MINIMOS DISCRETOS
'''

def soma_xi(lst_xi,m): #somatorio xi
    soma=0
    for i in range(m):
        soma+=lst_xi[i]
    return soma

def soma_yi(lst_yi,m): #somatorio yi
    soma=0
    for i in range(m):
        soma+=lst_yi[i] 
    return soma

def soma_xi2(lst_xi,m): #somatorio xi^2
    soma=0
    lst_xi2=[]
    for i in range(m):
        lst_xi2.append(lst_xi[i]**2)
        soma+=lst_xi2[i]
    return soma
        
def soma_xiyi(lst_xi,lst_yi,m): #somatorio xi*yi
    soma=0
    lst_xiyi=[]
    for i in range(m):
        lst_xiyi.append(lst_xi[i]*lst_yi[i])
        soma+=lst_xiyi[i]
    return soma

def MMQ(soma_x,soma_y,soma_x2,soma_xy,m): #aplicando aproximacao de funcao
    a0=((soma_x2*soma_y)-(soma_x*soma_xy))/((m*soma_x2)-(soma_x**2))
    a1=(m*soma_xy - soma_x*soma_y)/(m*soma_x2-soma_x**2)
    if(a0<0):
        return str(a1)+"x"+str(a0)  #montando string de acordo com sinal de a0
    return str(a1)+"x+"+str(a0)

def main():
    m=int(input("M: "))
    lst_x=[]
    lst_y=[]
    
    for i in range(m):
        elemento_x=float(input("x"+str(i)+": "))
        elemento_y=float(input("y"+str(i)+": "))
        lst_x.append(elemento_x)
        lst_y.append(elemento_y)
        print('\n')
        
    soma_x=soma_xi(lst_x,m)
    soma_y=soma_yi(lst_y,m)
    soma_x2=soma_xi2(lst_x,m)
    soma_xy=soma_xiyi(lst_x,lst_y,m)
    print("y=",MMQ(soma_x,soma_y,soma_x2,soma_xy,m))
    
main()
