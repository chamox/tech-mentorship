board = [
        ["T","A","L","P"],
        ["S","R","E","E"],
        ["Q","W","O","P"],
        ["K","L","M","N"]
        ]


def check_positions(board,x,y,target):
    dirs = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

    for dir in dirs:
        if board[dir[0]][dir[1]] == target:
            return True
    return False


    



if __name__ == "__main__":
    print ("Executed when invoked directly")


    for i in range(len(board)):
        for j in range(len(board[0])):
            print(str(i)+","+str(j))