# # 1 Exercitiu
# nr1 = 7
# nr2 = 3
# print(nr1/nr2)


# # 2
# nr1 = 7
# nr2 = 3
# print(nr1 ** 2)
# print(nr2**2)

# # 3
# nr1 = int(input("7"))
# nr2 = int(input("3"))

# if nr2 % nr1 ==0:
#     print("Al doilea numar este divizibil cu primul")
# else:
#     print("Al doilea numar nu este divizibil cu primul")
# # 3 a 2 varianta
# # nr1 = 7
# # nr2 = 3
# # print(type(nr2 % nr1 == 0))

# nr = 7
# nr1 = 3
# if nr1 % nr ==0:
#     print("nr1 e divizibil cu nr")

# 4

numar = 9
if numar % 2 ==0:
    print(f"Numarul{numar} este par.")
else:
    print(f"Numarul{numar} este impar.")

nr1 = 9
if nr1 % 2 ==0:
    print(f"Numarul{nr1} este par.")
else:
    print(f"Numarul{nr1} este impar.")

# 5
nr = 70
if  100 <= nr <= 150:
    print(f"Numarul {nr} se afla in intervalul 100-150.")
else:
    print(f"Numarul {nr} nu este in intervalul 100-150.")

# 6
nr = 100
if  50<= nr <=100:
   print(f"Numarul {nr} este mai mic decat 50")
else:
    print(f"Numarul {nr} este mai mar decat 100")

# 6.2
#include <iostream> 
# using namespace std;

# int main() {
#     int numar;

#     cout <<"100";
#     cin >> numar;

#     if (numar < 50 || numar > 100){
#         cout <<"Numarul este mai mic de cat 50 sau mai mare ecat 100"<< endl;
#     }
# }

# numar = int(input("Introduceti un numar: "))
# if numar < 50:
#     print("Numarul este mai mic decat 50")
# elif numar > 100:
#     print("Numarul este mai mare decat 100")
# else:
#     print("Numarul este intre 50 si 100")

# eu 
# import calendar
# yy = 2014  year
# mm = 12    month
#  display the calendar
# print(calendar.month(yy, mm))


import random
print('Your password: ')

chars ='dfkhfgdznahvfhadnbfbhdj1234@$'

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)