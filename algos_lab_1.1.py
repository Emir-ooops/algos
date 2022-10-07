a=int(input())
if a%3==0 or a%5==0:
    if a%3==0 and a%5!=0:
        print('Fizz')
    elif a%3!=0 and a%5==0:
        print('Buzz')
    elif a%3==0 and a%5==0:
        print('FizzBuzz')
else:
    print(a)