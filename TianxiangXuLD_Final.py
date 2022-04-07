import math

class LinearDiophantine:
      #Initialize
      def __init__(self,C11,C12,C13,C1,n):
            self.c11=C11
            self.c12=C12
            self.c13=C13
            self.c1=C1
            self.n=n

      #Implementationi of CMax
      def CMax(self):
            self.domain2=[self.c12,self.c12,self.c13,1]
            self.res=[0,abs(1+self.c11+self.c12+self.c13),abs(self.c11),abs(self.c12),abs(self.c13)]
            self.a = 1+self.c11+self.c12+self.c13
            for i in range(0,len(self.domain2)):
                self.res.append(abs(self.a-self.domain2[i]))
            for i in range(0,len(self.domain2)):
                for j in range(i+1,len(self.domain2)):
                      self.res.append(abs(self.domain2[i]+self.domain2[j]))

            for i in range(0,len(self.res)):
                for j in range(i+1,len(self.res)):
                      if self.res[i]<self.res[j]:
                            self.temp=self.res[i]
                            self.res[i]=self.res[j]
                            self.res[j]=self.temp

            return self.res[0]

      #Implementation of Kc
      def KNumber(self):
            self.res=[0]
            if (self.c1 == 0):
                  return 'Kc=',0
            else:
                  while(self.c1 != 0):
                        self.res.insert(1,self.c1%2)
                        self.c1 = self.c1 >> 1

            self.a = len(self.res)-1
            return self.a

      #Implementation of bi
      def bNumber(self):
            self.res=[0]
            if self.c1 == 0:
                  return 'Kc=',0
            else:
                  while(self.c1 != 0):
                        self.res.insert(self.c1%2)
                        self.c1 = self.c1>>1

            if ((self.n>=0) & (self.n<=len(self.res))):   #calculate the bi
                  return self.res[len(self.res)-self.n-1]
            else:
                  return 'Error'

      #Implementation of condition function of FA
      def condition(self,carry,i,a1,a2,a3,carryprime,iprime):
            self.carry=carry
            self.i=i
            self.a1=a1
            self.a2=a2
            self.a3=a3
            self.carryprime=carryprime
            self.iprime=iprime
            #Judge the value of the carry
            if ((self.carry<-self.CMax(self)) or (self.carry>self.CMax(self))):
                  return False
            if ((self.i>=1) and (self.i<=self.KNumber())):
                  self.iprime = self.i + 1
            else:
                  self.iprime = self.i

            #Calculate the i
            if (self.i == self.KNumber(self) + 1):
                  self.carry = 0
                  self.i=self.KNumber()+1
                  self.R=self.CMax().c1*self.a1 + self.CMax().c2*self.a2 + self.CMax().c3*self.a3 + self.bNumber() + self.carry
                  if (((self.a1 != 0) or (self.a1 != 1)) and ((self.a2 != 0) or (self.a2 != 1)) and ((self.a3 != 0) or (self.a3 != 1))):
                        return False

                  #Calculate R
                  self.R = self.c11*self.a1 + self.c12*self.a2 + self.c13*self.a3 + bi + self.carry
                  if (self.R%2 != 0):
                        return False
                  elif (self.R%2 == 0):
                        self.carry = self.R//2
                        return True

      #Implementation of a finite automata
      def FiniteAutomata(self):
            self.M=[]   #array of FA M
            for carry in range((-self.CMax()),self.CMax()+1):
                  for i in range(1,self.KNumber()+2): #The interval is left closed and right open
                        for a1 in range(0,2):
                              for a2 in range(0,2):
                                    for a3 in range(0,2):
                                          for carryprime in range(-self.CMax(),self.CMax()+1):
                                                for iprime in range(1,self.KNumber()+2):
                                                      if self.condition(carry,i,a1,a2,a3,carryprime,iprime):
                                                            self.M.append(carry)
                                                            self.M.append(i)
                                                            self.M.append(a1)
                                                            self.M.append(a2)
                                                            self.M.append(a3)
                                                            self.M.append(carryprime)
                                                            self.M.append(iprime)
                                                            self.M.append(1)
                                                      else:
                                                            self.M.append(carry)
                                                            self.M.append(i)
                                                            self.M.append(a1)
                                                            self.M.append(a2)
                                                            self.M.append(a3)
                                                            self.M.append(carryprime)
                                                            self.M.append(iprime)
                                                            self.M.append(0)
            return self.M

      #Condition of Cartesian product of two FAs
      def Tcondition(self,carry1,i1,a11,a12,a13,carry1prime,i1prime,carry2,i2,a21,a22,a23,carry2prime,i2prime):
            #Judge the value of the carry1 and carry2
            if ((carry1<-self.CMax()) or (carry1>self.CMax())):
                  return False
            if ((carry1>=-self.CMax()) and (carry1<=self.CMax()))
		return True
            if ((carry2<-self.CMax()) or (carry2>self.CMax())):
                  return False
            if ((carry2>=-self.CMax()) and (carry2<=self.CMax())):
                  return True
	
            #Calculate the i1 and i2
            if ((i1>=1) and (i1<=Kc)):
                  i1prime = i1 + 1
            if (i1 == Kc + 1):
                  i1 = Kc+1
            if ((i2>=1) and (i2<=Kc)):
                  i2prime = i2 + 1
            if (i2 == Kc + 1):
                  i2 = Kc+1
				  
            #Calculate R1 and R2
            self.R1=c11*a11 + c12*a12 + c13*a13 + self.bNumber().bi + carry1
    if (((a11 != 0) and (a11 != 1)) and ((a12 != 0) and (a12 != 1)) and ((a13 != 0) and (a13 != 1))):
        return False
    if (self.R1%2 != 0):
          print('no edge')
          return False
    elif (self.R1%2 == 0):
          if(carry1prime != self.R1//2):
                print('no edge')
                return False
          else:
                carry1 = self.R1//2
                return True
	
    self.R2=c21*a21 + c22*a22 + c23*a23 + bNumber().bi + carry2
    if (((a21 != 0) and (a21 != 1)) and ((a22 != 0) and (a22 != 1)) and ((a23 != 0) and (a23 != 1))):
          return False
    if (R2%2 != 0):
          print('no edge')
          return False
    elif (R2%2 == 0):
          if(carry2prime != R2//2):
             print('no edge')
             return False
          else:
                carry2 = self.R2//2
                return True
	
      if((a11==a21) and (a12==a22) and (a13==a23)):
            return True

      
      #Cartesian of FA
      def CartesianFA(self):
            self.M=[]   #Cartesian product of two FAs
            for carry1 in range(((-self.CMax()),self.CMax()+1):   #The interval is left closed and right open
                                for i1 in range(1,self.KNumber()+2):
                                      for a11 in range(0,2):
                                            a12 in range(0,2):
                                                  for a13 in range(0,2):
                                                        for carry1prime in range(-self.CMax(),self.CMax()+1):
                                                              for i1prime in range(1,self.KNumber()+2):
                                                                    for carry2 in range(((-self.CMax()),self.CMax()+1):   #The interval is left closed and right open
                                                                          for i2 in range(1,self.KNumber()+2):
                                                                                for a21 in range(0,2):
                                                                                      a22 in range(0,2):
                                                                                            for a23 in range(0,2):
                                                                                                  for carry2prime in range(-self.CMax(),self.CMax()+1):
                                                                                                        for i2prime in range(1,self.KNumber()+2):
                                                                                                                if Tcondition():
                                                                    

   


L=LinearDiophantine(-3,0,4,34,2)
print(L.CMax())
print(L.KNumber())
print(L.bNumber())
print(L.FiniteAutomata())
