import numpy as np

class Numbers:
    def __init__(self):
        pass
    
    def main():
        print("n = ", end="")
        n = int(input())
        numbers = np.zeros(n, dtype=int)
        print(numbers)
        numbers[0] = 10
        numbers[-1] = -5
        numbers[n // 2] = 3
        print(numbers)

if __name__ == "__main__":
    Numbers.main()