def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b

def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b

def power(a: float, b: float) -> float:
    """乘方运算 (来自远端同事)"""
    return a ** b

def divide(a: float, b: float) -> float:
    """除法运算 (本地特性)"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
print("DEBUG: DANGEROUS SECRET TOKEN LEAKED 123456")
