# 插入排序

### 输出结果
```
origin array :  [5, 2, 4, 6, 1, 3]
sorted array :  [1, 2, 3, 4, 5, 6]
sorted array desc:  [6, 5, 4, 3, 2, 1]
add binary :  [1, 1, 0, 0]
```

### 简要分析

* 插入排序书上都有,木有啥说的
* 转换成降序主要就是插入的时候如何判断(就改了一个符号)
* 二进制加法

# 归并排序

### 输出结果
```
origin array :  [2, 5, 6, 1, 3, 4, 8, 7]
merge array [2, 5, 6, 1, 3, 4, 8, 7] with p(0) q(0) r(1)   ---- 第一层
merge array result [2, 5, 6, 1, 3, 4, 8, 7]
merge array [2, 5, 6, 1, 3, 4, 8, 7] with p(2) q(2) r(3)   ---- 第一层
merge array result [2, 5, 1, 6, 3, 4, 8, 7]
merge array [2, 5, 1, 6, 3, 4, 8, 7] with p(0) q(1) r(3)   ---- 第二层
merge array result [1, 2, 5, 6, 3, 4, 8, 7]
merge array [1, 2, 5, 6, 3, 4, 8, 7] with p(4) q(4) r(5)   ---- 第一层
merge array result [1, 2, 5, 6, 3, 4, 8, 7]
merge array [1, 2, 5, 6, 3, 4, 8, 7] with p(6) q(6) r(7)   ---- 第一层
merge array result [1, 2, 5, 6, 3, 4, 7, 8]
merge array [1, 2, 5, 6, 3, 4, 7, 8] with p(4) q(5) r(7)   ---- 第二层
merge array result [1, 2, 5, 6, 3, 4, 7, 8]
merge array [1, 2, 5, 6, 3, 4, 7, 8] with p(0) q(3) r(7)   ---- 第三层
merge array result [1, 2, 3, 4, 5, 6, 7, 8]
sorted array :  [1, 2, 3, 4, 5, 6, 7, 8]
```

### 简要分析

* 可以很直观的看到第一层执行了4次,第二层执行了2次,第三层只执行了1次,算法是标准的对数时间复杂度


### 练习题

###### 重写merge过程,不使用哨兵
如果去掉了哨兵,再使用原先的merge就会数组越界了,这时候需要添加边界检测来判断是否某一个数组已经被完全归并完了。
