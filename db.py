from math import log
import time

from sqlalchemy import create_engine
from sqlalchemy import text

def get_pid(count):
    return count // 1000

engine = create_engine('mysql+pymysql://root:rlaguswjd@127.0.0.1:9001/large_db')

chunk = 100000
#max_value = 100000000
max_value = 15000000
count = 1000
total = 200000
alpha = 1.001


with engine.connect() as conn:
    conn.execute(text("truncate product_rec"))

    while total < max_value:
        query = "insert into product_rec (pid, rec_pid, cossim) values "
        if chunk > 5000:
            chunk = int(chunk *(2 + log(total)) / (alpha * (2 + log(total + chunk))))

        values_list = []
        for i in range(chunk):
            pid = get_pid(count)
            values_list.append('(%d, 2, 0.7)' % pid)
            count += 1

        query = query + ', '.join(values_list)
        start = time.time()
        conn.execute(text(query))
        end = time.time()
        print('total: %d, chunk size: %d, time spent: %.2fs' % (total, chunk, end-start))

        total += chunk
