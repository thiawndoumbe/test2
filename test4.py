import urllib.request
T = urllib.request.urlopen(" https://nskm.xyz/assets/dataset.txt").read().decode()
T=T.splitlines()
print(T)
lst_x=[]
lst_y=[]
for ligne in T:
    l3=ligne.split()
    print(l3)      
    lst_x.append(l3[0])
    print(lst_x)
    lst_y.append(l3[1])
lst_x.pop(0)
lst_y.pop(0)
print(lst_x)
int_list = list(map(int, lst_x))
int_listy = list(map(float, lst_y))
print(int_list)
print(int_listy)

import matplotlib.pyplot as plt
x=int_list
y=int_listy
plt.plot(x,y)
plt.xlabel("listes des X")
plt.ylabel("listes des Y")
plt.title("nuage des points")

plt.show()


