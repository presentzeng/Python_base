1. python编码
ASCII 一个byte 127字符 大小写英文和符号
Unicode统一编码 2个byte
UTF-8保存时可变长
python支持Unicode保存成文件时为UTF-8

2. yield 生成器
 
```
def odd():
	print('step 1')
	print('step 2')
	print('step 3')
	yield 1
```

这个直接调用odd()，是打印不出step的
需要用next(odd()),或者for 循环的形式

3. sorted
对List嵌套排序


4. lambda表达式