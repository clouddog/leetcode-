# 所有python相关的技巧与注意事项

## 栈
1. 将list当作栈时，要注意list[-1]（栈顶元素）前判断栈是否为空


2. 判断字符串是否为数字、字母、组合

        str.isdigit()  # 不能判断负数
        str.isalpha()
        str.isalnum()

3. 注意边界条件与意外情况
比如负数,stack是否为空等情况

4. 一般字符串的比较等用stack较多

5. 字母大小写
   
        s.islower()   #所有字符都是小写
        s.isupper()   #所有字符都是大写
        s.upper()     #把所有字符中的小写字母转换成大写字母
        s.lower()     #把所有字符中的大写字母转换成小写字母
        
        利用ascii码：
        abs(ord(i)-ord(stack[-1]))==32  # ord()返回ascii码

## 堆
