
def pypart(num):

    for i in range(num, 0):

        for j in range(0, i+1):

            print("* ", end=" ")
        print("\r")

num=10
pypart(num)


def pypart01(num):
    for i in range(0, num):

        for j in range(0, i+1):

            print("* ", end=" ")
        print("\t")

num=10
pypart01(num)

def pypart2(num):
    k = 2*num - 2

    for i in range(0, num):

        for j in range(0, k):
            print(end=" ")

        k = k - 2

        for j in range(0, i + 1):

            print(" *", end=" ")
    print("\t")

#pypart2(num)