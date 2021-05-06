def Descobrir_Hipotenusa():
  
 cateto = float(input('Primeiro Cateto '))
 cateto2 = float(input('Segundo Cateto '))

 quadrado = cateto * cateto
 quadrado2 = cateto2 * cateto2 

 soma_dos_quadrados = quadrado + quadrado2 

 raiz = soma_dos_quadrados ** 0.5

 print('O Valor da Hipotenusa é:')        # A soma dos quadrados dos catetos têm o mesmo valor que o quadrado da hipotenusa

 print(raiz)          
