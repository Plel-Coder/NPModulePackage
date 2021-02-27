from decimal import Decimal,getcontext,Overflow
import math as m
import time
import copy
#TanHalfPi([x])
#x값을 형식으로 바꾸기
#TanHalfPi([x,y])
#x가 곱값
#y가 지수값
#a.getnum()
#a의 숫자값을 decimal로 출력을시도
#실패시 TanHalfPi형태로 출력
#a.getex()
#a를 지수형으로 출력-10
getcontext().prec=100
class TanHalfPi(object):
    def __init__(self,array):
        if type(array[0])!=Decimal:                             #인수를 데시멀형태로 바꾸기
            array[0]=Decimal(array[0])
        if len(array)==1:                                       #그냥 수 입력
            if array[0]<0:
                self.negative=True
                array[0]=abs(array[0])
            else:
                self.negative=False
            self.index = Decimal(m.floor(abs(array[0]).log10()))     #index:지수부분
            self.number = array[0]/10**self.index               #number:수부분
            self.log = abs(array[0]).log10()                         #log:로그
            
            self.array = [self.number,self.index,self.negative]               #array:그냥 데이터
            
        else:                                                   #길이가 두개인 리스트를 받으면 첫번째를 수 부분으로 두번째를 지수부분으로 나누기
            if type(array[1])!=Decimal:
                array[1]=Decimal(array[1])
            if array[0]<0:
                self.negative=True
                array[0]=abs(array[0])
            else:
                self.negative=False
            self.index = array[1]
            self.number = array[0]
            self.log = array[1]+array[0].log10()
            
            self.array = [self.number,self.index,self.negative]
            
    def getnum(self):                                           #Decimal형태로 출력(실패시 경고 출력하고 TanHalfPi상태로 출력)
        try:
            return self.number * 10**Decimal(self.index)
        except Overflow:
            print("경고:getnum()를 하기엔 수가 너무 큽니다. ")
            print("값을 출력하려면 getex()를 쓰거나 연산자로 계산하세요.")
            return TanHalfPi([self.number,self.index])
    def getex(self):                                            #a를 지수형으로 출력
        if self.negative:
            result="-"
        else:
            result=""
        result+=str(self.number)+"E+"+str(Decimal(self.index)+1-1)
        return result

    def __add__(self,a):                                        #더하는 함수(__add__를 쓰면 함수없이도 덧셈 가능)
        result=copy.deepcopy(self)
        if result.negative ^ a.negative:
            if result.index<a.index:
                if result.index+100>a.index:
                    result.number=a.number - result.number/(10**(a.index-result.index))
                else:
                    result.number=a.number
                result.index=a.index
                result.negative=a.negative
                
            elif result.index==a.index:
                result.number-=a.number
                if a.number==result.number:
                    result=TanHalfPi([0])
                if result.number<0:
                    result.number=abs(result.number)
                    result.negative=True
                else:
                    result.negative=False
            else:
                if result.index<a.index+100:
                    result.number = result.number-a.number/(10**(result.index-a.index))
            while result.number<1 and not result.number==0:
                result.number=result.number*10
                result.index-=1
            result.log=result.index+abs(result.number).log10()
        else:
            if result.index<a.index:
                if result.index+100>a.index:
                    result.number=a.number + result.number/(10**(a.index-result.index))
                else:
                    result.number=a.number
                result.index=a.index
                
                
            elif result.index==a.index:
                result.number+=a.number
            else:
                if result.index<a.index+100:
                    result.number=a.number/(10**(result.index-a.index)) + result.number
            if result.number>=10:
                result.number=result.number/10
                result.index+=1
            result.log=result.index+result.number.log10()
            result.array = [result.number,result.index,result.negative]
        return result
    def __sub__(self,a):
        a.negative=not a.negative
        return self+a
    def __mul__(self,a):                                        #곱하는 함수(__mul__를 쓰면 함수없이도 곱셈 가능)
        result=copy.deepcopy(self)
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
        if result.negative ^ a.negative:
            result.negative=True
        else:
            result.negative=False
        result.array = [result.number,result.index,result.negative]
        
        return result
    def __pow__(self,a):                                        #거듭제곱 함수(__pow__를 쓰면 함수없이도 거듭제곱 가능)
        result=a
        
        try:
            result.log = (result*self.log).getnum()
            result.index=int(result.log)
            result.number=10**(result.log-int(result.log))
        except:
            raise OverflowError
        result.array = [result.number,result.index]
        return result
    def __str__(self):                                          #출력 함수(__str__를 쓰면 함수없이도 print로 원하는값 출력 가능)
        result=self
        result.number=round(result.number,3)
        return self.getex()
    def __eq__(self,a):                                         #출력 함수(__eq__를 쓰면 함수없이도 같은지 확인 가능)
        return (self.number==a.number) and (self.index==a.index)
if __name__ == "__main__":
    a=TanHalfPi([9])
    b=TanHalfPi([-10])
    print(a+b)
