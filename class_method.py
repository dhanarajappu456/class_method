class s:
 f=1
 @classmethod
 def fu(cls):
  cls.f+=1
  print(cls.f)

c=s()
d=s()
c_met=c.fu()     #print 3
d_met=d.fu()     #print 3

e=s()
print(s.f,c.f)   # print 3 3


