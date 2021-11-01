
class person:
    def __init__(self,p,q,e=7):
        self.n=p*q
        self.e = e
        phi = (p - 1) * (q - 1)
        #print(phi)
        obr_e = fev(self.e, phi)[1]
        self.d = obr_e % phi
        #print(self.n,' ',self.e)
        #Тут все по формулам, нечиго добавить
        pass


    def shifr(self,m): #Шифровка текста в массив чисел по буквам
        x=[]
        for ch in m:
            dobx = (ord(ch)**self.e) % self.n
            x.append(dobx)
        return x

    def deshifr(self,x): #Дешифровка массива в буквы
        m = ''
        for num in x:
            dobm = (num**self.d) % self.n
            m+=chr(dobm)
        return m



def fev(A,B):   #Версия алгоритма Евклида для шифрования
    yx=[0,1]    #Базовый случай
    if A<B:     #Гарантировать, что А больше
        P=A
        A=B
        B=P
    ost=A%B     #Остаток и результат целочисленного деления
    res=A//B
    #print(A, ' ', B, ' ', ost, ' ', res)
    if(ost!=0): #Если остаток не равен нулю

        yxn=fev(B,ost)  #...То вызовем функцию от меньшего из чисел и остатка
        yx[0]=yxn[1]    #...А результат обработаем по формуле
        yx[1]=yxn[0]-(yxn[1]*res)

    #print(yx)
    return (yx) 
