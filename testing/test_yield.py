# yield + 函数 == 生成器

def provider():
    for i in range(5):
        # return i
        yield i # 生成器：相当于return i



p = provider()
print(next(p))
print(next(p))
