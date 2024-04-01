

def fatorial(son):

    if son == 1:
        return  1

    else:
        return son * fatorial(son-1)


print(fatorial(995))

# a = 1
#
# for i in range(1, 1000):
#     a*=i
#
# print(a)