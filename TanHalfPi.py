from decimal import Decimal,getcontext,Overflow
import math as m
import time
#TanHalfPi([x])
#x값을 형식으로 바꾸기
#TanHalfPi([x,y])
#x가 곱값
#y가 지수값
#a.getnum()
#a의 숫자값을 decimal로 출력을시도
#실패시 TanHalfPi형태로 출력
#a.getex()
#a를 지수형으로 출력
getcontext().prec=100
class TanHalfPi(object):
    def __init__(self,array):
        if type(array[0])!=Decimal:
            array[0]=Decimal(array[0])
        if len(array)==1:
            self.index = Decimal(m.floor(array[0].log10()))
            self.number = array[0]/10**self.index
            self.log = array[0].log10()
            self.array = [self.number,self.index]
        else:
            if type(array[1])!=Decimal:
                array[1]=Decimal(array[1])
            self.index = array[1]
            self.number = array[0]
            self.log = array[1]+array[0].log10()
            self.array = [self.number,self.index]
            
    def getnum(self):
        try:
            return self.number * 10**Decimal(self.index)
        except Overflow:
            print("경고:getnum()를 하기엔 수가 너무 큽니다. ")
            print("값을 출력하려면 getex()를 쓰거나 연산자로 계산하세요.")
            return TanHalfPi([self.number,self.index])
    def getex(self):
        result=str(self.number)+"E+"+str(Decimal(self.index)+1-1)
        return result

    def __add__(self,a):
        result=self
        if result.index<a.index:
            if result.index+100>a.index:
                result.number=a.number + result.number/(10**(a.index-result.index))
            result.index=a.index
                
        elif result.index==a.index:
            result.number+=a.number
        else:
            if result.index<a.index+100:
                result.number=a.number + result.number/(10**(result.index-a.index))
        if result.number>=10:
            result.number=result.number/10
            result.index+=1
        result.log=result.index+result.number.log10()
        result.array = [result.number,result.index]
        return result
    def __mul__(self,a):
        result=self
        if type(a)!=TanHalfPi:
            a=TanHalfPi([a])
        if a.getnum()==0:
            result=TanHalfPi(0)
        else:
            result.log+=a.log
            result.index=int(result.log)
            result.number=10**(result.log-int(result.log))
        while result.number>=10:
            result.number=result.number/10
            result.index+=1
        result.array = [result.number,result.index]
        
        return result
    def __pow__(self,a):
        result=a
        b=result.getnum()
        
        try:
            result.log = (result*self.log).getnum()
            result.index=int(result.log)
            result.number=10**(result.log-int(result.log))
        except:
            result.log=b.log
            result.index=int(result.log)
            result.number=10**(result.log-int(result.log))*self.log
            result.tetrate+=1
        if result.number>=10:
            
            result.index+=int(result.number.log10())
            result.number=10**(result.index-result.log)
        result.array = [result.number,result.index]
        return result
    def __str__(self):
        return self.getex()
    def __eq__(self,a):
        return (self.number==a.number) and (self.index==a.index)
if __name__ == "__main__":
    a=TanHalfPi([10])
    b=TanHalfPi([1000])
    print(a**b)
