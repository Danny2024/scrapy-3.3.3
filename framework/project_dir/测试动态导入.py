import importlib


# 根据全类名，从模块中获取类对象，通过类对象创建实例对象


# 1.全类名
full_name = 'spiders.baidu.BaiduSpider'
split_names = full_name.rsplit('.', maxsplit=1)
module_name = split_names[0]
class_name = split_names[1]
print(module_name)
print(class_name)

# 根据模块名，导入对应模块，获取该模块对象
module = importlib.import_module(module_name)
# print(module)
# 根据模块对象，根据类名，获取类对象
cls = getattr(module,class_name)
# print(cls)
# 使用类对象创建实例对象
instance = cls()
# 后面就可以使用这个对象了
print(instance)
