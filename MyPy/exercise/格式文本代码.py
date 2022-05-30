# coding:utf8
# with open('origin.txt', encoding='utf-8') as f:
#     c = f.read()
#     a = c.split()
#
# with open('sortedfile.txt', 'w') as f:
#     try:
#         # 两段处理代码
#         c = 1
#         for i in range((len(a) // 2) + 1):
#             f.write(f'{c}、')
#             c += 1
#             f.write('{:<16}'.format(a[2*i]))
#             f.write('{:<}'.format(a[2*i+1]))
#             f.write('\n')
#
#         # 四段处理代码
#         # i = 1
#         # count = 0
#         # while count < (len(a) // 4) + 1:
#         #     # f.write('{:<4}'.format(i))    # 三段处理，第一段添加序号
#         #     f.write('{:<8}'.format(a[0+4*count]))
#         #     f.write('{:^20}'.format(a[1+4*count]))
#         #     f.write('{:^20}'.format(a[2+4*count]))
#         #     f.write('{:^8}'.format(a[3+4*count]))
#         #     f.write('\n')
#         #     count += 1
#         #     i += 1
#     except Exception as e:
#         print("wrong:", e)

#  json格式化
text = ''
print(text.replace("'", "\"").replace('None', 'null').replace('True', 'false').replace('False', 'false'))