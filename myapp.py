# 辞書型

sales = {"taguchi": 200, "fkoji": 400}
print(sales["taguchi"])
sales["taguchi"] = 300
sales["dotinstall"] = 500
del (sales["fkoji"])
print(sales)

# for sales_name in sales:
#     print(sales[sales_name])

for key, value in sales.items():
    print("{0}: {1}".format(key, value))
