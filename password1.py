import random
upp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low="abcdeghijklmnopqrstuvwxyz"
digit="1234567890"
sym="{}()@*;,-_[]"
all=upp+low+digit+sym

length=16
password="".join(random.sample(all,length))
print(password)