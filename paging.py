def main():
    ms = int(input("Enter total memory size: "))
    ps = int(input("Enter page size: "))
    nop = ms // ps
    print(f"Total number of pages: {nop}")

    np = int(input("Enter number of processes: "))
    rempages = nop

    s = [0] * 10
    fno = [[0] * 20 for _ in range(10)]

    for i in range(1, np + 1):
        s[i] = int(input(f"\nEnter number of pages required for process [{i}]: "))
        if s[i] > rempages:
            print(f"Memory full! Cannot allocate pages for process {i}.")
            break
        rempages -= s[i]
        print(f"Enter frame numbers for process [{i}]:")
        for j in range(s[i]):
            fno[i][j] = int(input(f" Page {j} -> Frame: "))

    x, y, offset = map(int, input("\nEnter process number, page number, and offset: ").split())

    if x > np or y >= s[x] or offset >= ps:
        print("\nInvalid input!")
    else:
        pa = fno[x][y] * ps + offset
        print(f"\nPhysical Address = {pa}")

if __name__ == "__main__":
    main()
