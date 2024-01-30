phone_number = int(input())

area_code = phone_number // 10000000
number = phone_number % 10000000

print('({}) {}-{}'.format(area_code, number //10000, number % 10000))
