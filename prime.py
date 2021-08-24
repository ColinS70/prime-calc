cur = 3.0
div = 0.0
out = 0.0
found = 0
calcAmt = 0
import time
current = time.time()
recentPrime = 0

while 1 == 1:
    div = cur - 1
    while div > 1:
        out = cur/div
        if out.is_integer() == False:
            #print(cur,'/',div,'= ',out)
            div -= 1
            calcAmt += 1
        else:
            div = -10
            calcAmt += 1
            break
        if div == 2:
            if cur == 4:
                break
            #if(cur > 15000):
                #print('Prime: ', cur)
            found += 1
            calcAmt += 1
            recentPrime = cur
            div = 1
    cur += 1
    if time.time() - current >= 60:
        print('About ', found, ' primes this minute!')
        print('Thats about ', found/60, ' a second!')
        print('The computer preformed ', calcAmt, ' calculations!')
        print('The current prime is ', recentPrime,'.')
        print()
        found = 0
        current = time.time()
    
