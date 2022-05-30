空格：None，追加只会在没有数据的最后一行
```python
# 新建工作表
from openpyxl import Workbook, load_workbook

workbook = Workbook()
sheet = workbook.active
print(sheet)
sheet.title = 'first'
workbook.create_sheet('second')  # 创建另一个表格
workbook.save('created.xlsx')
print("创建新表成功！")

# 工作表信息
workbook = load_workbook(filename='test.xlsx')
sheet = workbook['Sheet1']
print("所有工作表：", workbook.sheetnames)
print("工作表的尺寸：", sheet.dimensions)

# 移除工作表
n_s = workbook['new_sheet']
workbook.remove(n_s)
workbook.save(filename='test.xlsx')
print(workbook.sheetnames)

# 获取工作表中单元格的的值
w_a = workbook.active
print("B2的数据：", w_a['B2'].value)
cell1 = sheet.cell(row=1, column=1)
cell2 = sheet.cell(row=11, column=3)
print("通过行列确定单元cell1：", cell1, cell1.value, cell1.coordinate)
print("通过行列确定单元cell2：", cell2, cell2.value, cell2.coordinate)

cells1 = sheet["B2:C3"]   # 获取 B2:C3 区域的值
print("范围单元格地址列表：", cells1)
print("------矩形区域的值--------")
for i in cells1:
    for j in i:
        print(j.value)     # 先行后列

print("-------获取列---------")
cells2 = sheet['B:C']
print(cells2)   # 返回元组
for i in cells2:
    for j in i:
        print(j.value, end='\t')

print("----------通过行列索引获取范围--------")
for i in sheet.iter_rows(min_row=1, max_row=2, min_col=1, max_col=2):  # 闭区间
    for j in i:
        print(j.value, end='\t')

print("-------------修改单元格值并保存-----------")
sheet['A2'] = "晾A2"
workbook.save(filename='test.xlsx')
print(sheet['A2'].value)

print("-------------向表格中插入行数据-----------")
date = [["唐僧", "男", "180cm"],
        ["孙悟空", "男", "188cm"],
        ["猪八戒", "男", "175cm"],
        ["沙僧", "男", "176cm"]]
for row in date:
    sheet.append(row)
workbook.save(filename='test.xlsx')
print("保存成功！")

print("---------向excel中插入公式---------")
sheet["E2"] = "标准身高"
for i in range(2, 19):
    sheet["E{}".format(i)] = '=IF(RIGHT(C{},2)="cm",C{},SUBSTITUTE(C{},"m","")*100&"cm")'.format(i, i, i)
workbook.save(filename="test.xlsx")
print("插入公式成功！")

print("-------插入空行列---------")
sheet.insert_cols(idx=3, amount=1)      # 在左侧插入
sheet.insert_rows(idx=2, amount=1)      # 在上面插入
workbook.save(filename="test.xlsx")
print("插入空行列成功！")

print("-------删除空行列---------")
sheet.delete_cols(idx=3, amount=1)
sheet.delete_rows(idx=2, amount=1)
workbook.save(filename="test.xlsx")
print("删除空行列成功！")

print("----------移动表格-----------")
sheet.move_range("C1:D4", rows=2, cols=-1)  # 下移两行，左移1列
workbook.save(filename="test.xlsx")
print("移动表格成功！")

print("---------复制工作表------")
workbook.copy_worksheet(sheet)  # 产生另一个工作表sheet+' Copy'
workbook.save(filename="test.xlsx")
print(workbook.sheetnames)

print("---------重命名工作表------")
s1 = workbook["城市"]
s1.title = 'city'
workbook.save(filename="test.xlsx")
print(workbook.sheetnames)

```
