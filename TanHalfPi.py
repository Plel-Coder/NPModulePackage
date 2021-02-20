from decimal import Decimal,getcontext,Overflow
import math as m
import time
getcontext().prec=100
class exponential(object):
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
            return exponential([self.number,self.index])
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
        if type(a)!=exponential:
            a=exponential([a])
        if a.getnum()==0:
            result=exponential(0)
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
if __name__ == "__main__":
    a=exponential([10])
    b=exponential([1000])
    print((a**b).getex())