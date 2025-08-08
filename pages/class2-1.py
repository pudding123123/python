# # 比較運算值
# print(1 == 1)
# print(1 != 1)
# print(1 >= 2)
# print(1 <= 2)
# print(1 > 2)
# print(1 < 2)

# # 邏輯運算值
# print(not True)
# print(not False)

# print(False and False)
# print(False and True)
# print(True and False)
# print(True and True)

# print(False or False)
# print(False or True)
# print(True or False)
# print(True or True)
# # 練習:密碼驗證
# password = input("請輸入密碼:")
# if password == "1234":
#     print("密碼正確，Josh歡迎回家!")
# elif password == "5678":
#     print("密碼正確，Dino歡迎回家!")
# else:
#     print("密碼錯誤")
# a = input("請輸入年份:")
# b = int(a)
# if b % 400 == 0:
#     print(f"{a}年是閏年")
# elif b % 100 == 0 and b % 400 != 0:
#     print(f"{a}年不是閏年")
# elif b % 4 == 0:
#     print(f"{a}年可能是閏年")

# a = input("請輸入年分:")
# b = int(a)
# if b % 4 == 0:
#     if b % 100 == 0:
#         if b % 400 == 0:
#             print(f"{a}年是閏年")
#         else:
#             print(f"{a}年不是閏年")
#     else:
#         print(f"{a}年是閏年")
# else:
#     print(f"{a}年不是閏年")
