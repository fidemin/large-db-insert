from math import log

init_chunk = 100000
threshold = 10000000
chunk = init_chunk

total = 0

while total < 1000000000:
    if total < 10000:
        print('chunk: %d' % chunk)
        total += chunk
    else:
        chunk = int(chunk *(1 + log(total)) / (1 + log(total + chunk)))
        print('chunk: %d' % chunk)
        total += chunk

