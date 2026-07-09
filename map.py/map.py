def capt_name(name):
    return name.capitalize()
names = ('andy','benny','Anto','chika')
proper_name = []


#logic untuk tambah data
#for name in names:
 #   proper_name.append(capt_name(name))


proper_name = list(map(capt_name,names))


print(proper_name)