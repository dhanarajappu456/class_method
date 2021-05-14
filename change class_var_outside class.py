class s:
 f=1
 def fu(self):
  self.f+=1
  print(self.f)


a=s()
a.fu()    #print  2
b=s()
b.fu()    #print  2
s.f=100   
s().fu()      #print 101 
print(a.f)     # 2 


'''
so what we observe here is 
here fu is object method and change made is 
only reflected for that object

but the class variable changed
by statment s.f=100
and new object after this statement will, have
the value for f as =100




'''
