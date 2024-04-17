def is_prime(num):
    if num < 2:
        return false
    for i in range(2,int (num ** 0.5)+1):
        if num%i==0:
            return False
        return True

    def main():
        n=int(input("Enter the limit n:"))
        print()

        for i in range(2,n+1):
            if is_prime(i):
                print(i,end=" ")

    if __name__ == "__main__":
        main()
