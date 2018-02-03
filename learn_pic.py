# pickle & cpickle
import pickle
# d = dict(url='index.html',title='首页',content='首页')
# print(pickle.dumps(d))
# f=open(r'dump.txt','wb')
# pickle.dump(d,f)
# f.close()
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)