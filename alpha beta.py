MAX, MIN = float('inf'), -float('inf')

def minimax(depth, nodeindex, maximizingplayer, values, alpha, beta):
    if depth == maxdepth:
        return values[nodeindex]

    if maximizingplayer:
        best = MIN
        for i in range(2):  # Assuming binary tree (2 children)
            val = minimax(depth + 1, nodeindex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            print("Level: ", depth)
            print("Alpha: ", alpha)
            print("Beta: ", beta)

            if beta <= alpha:  # Corrected condition
                print("PRUNING IS DONE")
                break  # Exit the loop if pruning occurs

        return best
    else:
        best = MAX
        for i in range(2):  # Assuming binary tree (2 children)
            val = minimax(depth + 1, nodeindex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:  # Corrected condition
                print("PRUNING IS DONE")
                break  # Exit the loop if pruning occurs

        return best

maxdepth = int(input('Enter the depth of tree: '))
values = []

for i in range(2 ** maxdepth):
    value = int(input(f"Enter value {i + 1}: "))
    values.append(value)

print("The optimal value is", minimax(0, 0, True, values, MIN, MAX))