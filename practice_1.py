class Calculator():
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result +=num
        return self.result

    def sub(self,num):
        self.result -=num
        return self.result

    def mul(self,num):
        self.result *=num
        return self.result

    def div(self,num):
        self.result /=num
        return self.result


cal=Calculator()
r=cal.add(5,0)
print(f'더하기 5 ----> {r}')
r=cal.sub(2)
print(f'빼기 2 ------> {r} ')
