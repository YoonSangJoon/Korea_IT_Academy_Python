
# 정수 (int형)의 특징

# 1개의 정수 데이터 당 4byte(=32bit) 길이를 가짐
# 맨 앞의 비트 (최상위 비트)를 부호를 표시하는 용도로 사용 (sign bit)

# 1 : -
# 0 : +
# 1 ==> 00000000 00000000 00000000 00000001
# 10 => 00000000 00000000 00000000 00001010
# 17 => 00000000 00000000 00000000 00010001

# -1 ==> 11111111 11111111 11111111 11111111
# -10 => 11111111 11111111 11111111 11110110

# 음수는 절댓값의 2의 보수를 취한 결과임.

#######################################################

# 정수의 음수 표현

# step 1 : 절댓값의 1의 보수를 구한다.
#          ** 1의 보수란 ? : 0 -> 1 로 1 -> 0 으로 바꾼 값

# step 2 : 그 결과에 1을 더한다. ==> 2의 보수

# 1 ==> 00000000 00000000 00000000 00000001
# -1 => 10000000 00000000 00000000 00000001 (X)  /  1 + (-1) 은 -2.

# 1의 1의 보수
# 11111111 11111111 11111111 11111110

# 1의 2의 보수
# 11111111 11111111 11111111 11111111 ==> 실제 컴퓨터의 -1의 모습.
# (정수는 32bit만 인식되므로 가장 앞의 1은 삭제됨.)
# 결과는 0

n1 = 17
n2 = 10

print(n1 & n2) # 0

# & : AND
# A & B : 숫자 A와 숫자 B의 비트 중 하나라도 0이면
#         해당 자릿수의 비트는 0으로 표시한 후 10진수로 변환.


print(n1 | n2) # 27  # | : shift + \

# | : OR
# A | B : 숫자 A와 숫자 B의 비트 중 하나라도 1이면
#         해당 자릿수의 비트는 1로 표시한 후 10진수로 변환.


print(n1 ^ n2) # 27

# ^ : XOR (배타적 OR 연산 (Exclusive OR))
# A ^ B : 숫자 A와 숫자 B의 비트 중 한쪽만 1이면 1로,
#         양쪽 모두 1이면 0으로 표시 후 10진수로 변환.


print(~n1)     # -18

# ~ : NOT (1의 보수)
# ~17 : NOT (1의 보수)
# 00000000 00000000 00010001 ==> 17
# 11111111 11111111 11101110 ==> ~17 ==> -18

# 00000000 00000000 00010010 ==> 18
# 11111111 11111111 11101101 ==> 18의 1의 보수
# 11111111 11111111 11101110 ==> 18의 2의 보수 (-18)

print(n1 >> 2) # 4

# >> n : 우측 쉬프트 연산 (비트를 오른쪽으로 n칸 이동 후 10진수로 변환)


print(n1 << 2) # 68

# << n : 좌측 쉬프트 연산 (비트를 왼쪽으로 n칸 이동 후 10진수로 변환)


print(n1 ^ 16) # 1