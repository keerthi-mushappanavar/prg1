def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag and num > 1:
        print("prime")
    else:
        print("not prime")