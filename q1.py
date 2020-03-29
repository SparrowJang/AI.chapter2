from treelib import Node, Tree
import json

result = (3,3)



rightMoves = [(1,1), (2,0), (0,2), (1, 0), (0, 1)]
leftMoves = [(-1,0), (0,-1), (-1, -1), (-2,0), (0, -2)]

states = set()

def get_state(x, y, depth):

    return '{0}_{1}_{2}'.format(x, y, depth % 2)

def next(current, depth, parent, i, tree, lastMove = None):

    if parent == None:
        parent = depth
        tree.create_node(json.dumps(current[:]), depth)
        states.add(get_state(current[0], current[1], depth))


    if depth % 2 == 0:
        moves = rightMoves
    else:
        moves = leftMoves

    depth = depth + 1

    for move in moves:
        currentX =  current[0] + move[0]
        currentY =  current[1] + move[1]

        #不做重複動作
        if lastMove and (move[0] + lastMove[0]) == 0 and (move[1] + lastMove[1]) == 0:
            pass

        #跳過原點
        elif currentX == 0 and currentY == 0:
            pass
        
        #不能變負的，也不能超過最大人數
        elif currentX > 3 or currentX < 0 or currentY > 3 or currentY < 0:
            pass

        #防止傳教士被殺
        elif currentY > 0 and currentY < 3 and currentX > currentY:
            pass

        #防止傳教士被殺
        elif currentY > 0 and currentY < 3 and currentX < currentY:
            pass

        elif depth > 20:
            pass

        else:

            #newCurrent = [currentX, currentY, depth, move]
            newCurrent = [currentX, currentY, depth]

            nodeId = '{0}_{1}|{2}'.format(str(depth), str(i), parent)
            #print(nodeId, newCurrent)
            tree.create_node(json.dumps(newCurrent), nodeId, parent = parent)

            states.add(get_state(currentX, currentY, depth))

            if not(currentX == result[0] and currentY == result[1]):
                next(newCurrent, depth, nodeId, i, tree, move)
        
            i = i + 1


currentTree = Tree()

next([0, 0, 0], 0, None, 1, currentTree)

currentTree.show()
#print(currentTree)
print('all states:')
print(len(list(states)))

