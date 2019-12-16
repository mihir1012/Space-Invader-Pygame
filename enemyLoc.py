import random
def enemyRoute(NumEnemy,enemyX_Change,enemyY_Change):
    EnemyX = []
    EnemyY = []
    EnemyXChg = 100
    EnemyX.append(random.randint(0,736))
    EnemyY.append(random.randint(0,150))
    for i in range(1,NumEnemy):
        EnemyX.append(EnemyX[i-1]+EnemyXChg)
        EnemyY.append(EnemyY[i-1])
        if EnemyX[i] >=736:
            EnemyXChg = -100
            EnemyX[i]=min(EnemyX)+ EnemyXChg
        if EnemyX[i] < 0:
            EnemyX[i] = 0
            EnemyXChg =  100
            EnemyY[i] += enemyY_Change
    return (EnemyX,EnemyY)
#x = []
#y = []
#(x, y) = enemyRoute(5,50,40)
#print("Hello")
#print(x)
#print(y)
