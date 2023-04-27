import time

# print('A')
# time.sleep(2)
# print('B')

#time.clock()

# t1 = time.perf_counter()
# print(t1)
# time.sleep(1)
# t2 = time.perf_counter()
# print(t2)
# print(f"delta= {t2-t1}")


# t1 = time.time()
# print(t1)
# time.sleep(1)
# t2 = time.time()
# print(t2)
# print(f"delta= {t2-t1}")

#print(time.time())
# print(time.monotonic())
# print(time.process_time())
# time.sleep(1)
# print(time.monotonic())
# print(time.process_time())

# print(time.localtime(0))
# print(time.gmtime(0))
#
# t = time.localtime()
# print(time.strftime('%H:%M', t))

from datetime import timedelta
t1 = timedelta(days=1)
print(t1)
t2 = t1 * 365
print(t2)

from datetime import date
print(date.today() + t2)

from datetime import datetime
print(datetime.now().strftime('%H:%M'))

now = datetime.now()
print(now.hour)