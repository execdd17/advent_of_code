from SprialMemory import SpiralMemory

def main():
    target = 8432
    spiral_memory = SpiralMemory(total_elements=target)
    print spiral_memory

    for i in range(len(spiral_memory.board)):
        for j in range(len(spiral_memory.board)):
            if spiral_memory.board[i][j] == target:
                print str(i) + "," + str(j)


if __name__ == "__main__":
    main()
