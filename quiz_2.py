#2、如何在一个函数内部修改全局变量

#利用global在函数声明 修改全局变量
x=120
def fn():
    global x
    x=100
fn()
print(x)
