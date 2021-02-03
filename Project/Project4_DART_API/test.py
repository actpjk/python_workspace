tables = [1,2,3,4,5,6,7,8]

df_list= list()

for i, v in enumerate(tables):
    if i in [0,2,4]:
        pass
    else:
        df = tables[i]
        df_list.append(df)
print(df_list)   