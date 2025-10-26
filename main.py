def is_prime(num):
    """判断单个数字是否为质数"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_primes_less_than(n):
    """返回小于n的所有质数列表"""
    primes = []
    for num in range(2, n):  # 质数从2开始，遍历到n-1
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    # 交互输入n，输出小于n的所有质数
    try:
        n = int(input("请输入一个正整数n："))
        if n <= 2:
            print(f"小于{n}的质数不存在")
        else:
            primes = get_primes_less_than(n)
            print(f"小于{n}的所有质数为：{primes}")
    except ValueError:
        print("请输入有效的正整数！")
