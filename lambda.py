print((lambda x,y,z : x+y+z)(3,4,9))

add = lambda x,y : x+y
print(add(3,4))

lambdas = [lambda x:x+10, lambda x:x+100]
print(lambdas[0](5))
print(lambdas[1](5))

