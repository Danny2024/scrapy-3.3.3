# 导入默认配置
from .default_settings import *

# 导入项目中的配置文件信息，这个信息就会覆盖默认配置
from settings import *

import sys
print(sys.path)
# '/home/python/Desktop/scrapy/framework/project_dir',
# 程序加载的时候，是从运行这个代码那个目录开始加载的
