'''Să se calculeze sumele: 	s1=1+2+3+…+n
							s2=1*2+2*3+3*4+…+(n-1)*n
							s3=1+1*2+1*2*3+…+1*2*3*…*n
							s4=12+22+32+…+n2
							s5=1/2+2/3+3/4+…+n/(n+1)
							s6=1+2+22+23+24+…+2n
							Notă: Pentru fiecare sumă n – se va citi de la tastatură.'''
s1 = 0
n = eval(input("n = "))
for i in range(1,n+1):

	s1+=i
print('suma este ', s1)

s2 = 0
n = eval(input("n = "))
for i in range(2,n+1):
	s2+=(i-1)*i
print('suma este ', s2)

s3 = 0
n = eval(input("n = "))
p = 1
for i in range(1,n+1):
	p*=i
	s3+=p	
print('suma este ', s3)

s4 = 0
n = eval(input("n = "))
for i in range(12,n*10+3,10):
	s4+=i
print('suma este ', s4)

s5 = 0
n = eval(input("n = "))
for i in range(1,n+1):
    s5+=i/(i+1)
print('suma este ', s5)
