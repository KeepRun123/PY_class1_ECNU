# #
# # ##第一题：口算公式
# #
# # for m in range(1,10):
# #     a = ""
# #     n = 1
# #     while n <= m:
# #         a = a+f"{n}*{m}={m*n}\t"
# #         n = n+1
# #     print(a)
# # print("\n")
# #
# #
# # ##第二题：判断单词的元音字符
# #
# # flag_vowel = 0
# # decide_word = "aeiouAEIOU"
# # word = input("请输入你的单词：")
# # list_word = list(word)
# # for index in range(0,len(list_word)):
# #     if word[index] in decide_word:
# #         flag_vowel = 1
# # if flag_vowel:
# #     print(word+" have vowel")
# # else:
# #     print(word + " does not have vowel")
# #
# # print("\n")
# #
# #
# # ##第三题：判断第几天
# # month = int(input("your month:"))
# # day = int(input("your day:"))
# # month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
# # print(f'this is the {sum(month_list[0:month - 1])+day}th day of the year')
#
#
# ##第一题 ： 括号匹配
# expression = input("input your experssion:")
#
# my_stack = []
# left_quote = ['(','{','[']
# right_quote = [')','}',']']
#
# no_match = False
# for ch in expression:
#     if ch in left_quote:
#         my_stack.append(ch)
#     elif ch in right_quote:
#         if not my_stack:
#             no_match = True
#             break
#         else:
#             left_ch = my_stack.pop()
#             if left_quote.index(left_ch) != right_quote.index(ch):
#                 no_match = True
#                 break
# if no_match or my_stack != []:
#     print("not match.")
# else:
#     print("match.")
#
#
# ##第二题 ： 筛子
# import random
#
# len = 10000
# count = [0] * 6
# for i in range(0,len):
#     count[random.randint(1,6)-1] += 1
# print(count)
#
# import matplotlib.pyplot as plt
# plt.bar(range(1,7),count)
# plt.show()
#
# ##第三题 ： 概率图
# count = [0] * 6
# history = []
# for j in range(0,1000):
#     for i in range(0,50):
#         count[random.randint(1,6)-1] += 1
#     percentage = []
#     for i in range(0,6):
#         percentage.append(count[i]/sum(count))
#     history.append(percentage)
#
# import matplotlib.pyplot as plt
# fig,ax = plt.subplots()
#
# x = list(range(1000))
# plt.plot(x,history)
# plt.show
#
# ##第四题 ： 三维坐标图
# X,Y =np.meshgrid(np.linspace(-2,2,25),np.linspace(-2,2,25))
# Z = X*X+Y*Y
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize = (10,8))
# ax = fig.subplots(subplot_kw = {"projection":"3d"})
# surf = ax.plot_surface(X,Y,Z,cmap = 'plasma')
#
# ##第五题 ： 二位点
# x = [x for x in range(10) for y in range(10)]
# y = [y for x in range(10) for y in range(10)]
# import matplotlib.pyplot as plt
# plt.scatter(x,y)
# plt.show()
#
# ##第六题
# print('*' * 40)
# print('hello'.center(38).center(40,'*'))
# print('hfc'.center(38).center(40,'*'))
# print('*' * 40)