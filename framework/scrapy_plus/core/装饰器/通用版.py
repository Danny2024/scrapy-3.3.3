class decorate(object):
    def decor_01(self,num):
        print('开始装饰－1')
        def decor_02(func):
            print('开始装饰－2')
            def fn_in(a,b):
                print('这是装饰器－－{}'.format(num))
                return func(a,b)
            return fn_in
        return decor_02
# add = decor(add)
# add(1,3)
d1=decorate()
@d1.decor_01(1)
def add(a,b):
    # print('aaaa-')
    print(a+b)
    return 'ok'


add(1,5)
print(add(1,2))
print(type(decorate))
print(type(d1))

# 元类

D2 = type('d2',(object,),{'bbbb':22222})
print(type(D2))
print(D2.bbbb)
E2 = D2()
print(E2.bbbb)
#　外部函数被调用一次，内部函数就执行一次


class Meta(type):
    def __new__(cls,name,parents,attrs):
        kvs=[[k,v] for k,v in attrs.items() if not k.startswith('__') ]
        for kv in kvs:
             attrs[kv[0]]+=10
        return super(Meta,cls).__new__(cls,name,parents,attrs)

class Student(metaclass=Meta):
   age1 = 10
   age2 = 11

stu = Student()
print(stu.age1)
print(stu.age2)



