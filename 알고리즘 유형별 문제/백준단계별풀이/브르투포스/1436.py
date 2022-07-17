num = int(input()) #입력 받는 번호 입력
word = 666
cnt = 0 #몇개의 666을 찾았는지
# while cnt <= num:
#     if result in str(word):
#         cnt += 1
#         result = result + word
#     print(cnt)
#

ret = 0
while cnt < num:
    if '666' in str(word):
        ret = word
        cnt += 1

    word += 1

print(ret)