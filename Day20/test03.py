import time

s = time.strftime('%T-%m-%d', time.localtime(time.time()))
print(s)
print(type(s))

print(time.time())  # 1970.1.1 자정 ~ 현재 시간의 밀리초
print(time.localtime(time.time()))