import random, sys, os

print("欢迎来玩左轮手枪游戏，游戏规则很简单.\n")
print("左轮手枪里有6个弹孔，只有一个弹孔装有子弹\n")
print("每人轮流用枪指着脑袋并开枪，开枪前可以下注，坚持到最后的人将拿走所有的赌注~\n")

while True:
    play_flag = input("确定要玩吗？(Y/N)")
    if play_flag == 'Y' or play_flag == 'N':
        break;
    else:
        print("请输入Y或N\n")

if play_flag == 'N':
    print("好吧！朋友们，欢迎下次再来！\n")
    sys.exit()
else:
    print("勇敢的朋友，你的对手是AI，咱们开始吧！Good Luck!\n")

total_bet = 0
bet = 0
gun = "AI"    #AI or Human

while True:
    first = input("你要开第一枪吗？(Y/N)\n")
    if first == 'Y' or first == 'N':
        break
    else:
        print("请输入Y或N\n")
        continue

if first == 'Y':
    gun = "Human"
    order = 0
else:
    gun = "AI"
    order = 1
    
bullet = random.randint(0,6)
for times in range(0,6):
    print("***************第"+ str(times + 1) + "回合**************\n")
    print("现在台面上的赌注是$" + str(total_bet) + "\n")

    if (times % 2 == order):
        print("枪正指在你的头上\n")
    else:
        print("枪正指在AI的头上\n")

    while True:
        bet = int(input("请问你要加注多少？"))
        if bet >= 0:
            total_bet = total_bet + bet * 2
            print("加注$" + str(bet) + "，AI跟注$" + str(bet) + "，台面总赌注是$" + str(total_bet))
            break
        else:
            print("输入有误，请输入数字\n")

    print("开枪,嘭。。。。。。。。。。。。。。。。\n")
    if bullet == times:
        if (times % 2 == order):
            print("人类：呃。。。噗。。。(人类中枪、脑浆迸裂)\n")
            print("AI: 愚蠢的人类，你以为输掉的只是赌注吗？哈哈哈哈……(猖狂大笑)\n")
        else:
            print("AI：呃。。。呲。。。(AI中枪、火花四射)\n")
            print("AI: 啊！！！我还会回来的。。。。。\n")
        break
    else:
        if (times % 2 == order):
            print("AI: 幸运的人类，希望下一轮你还是这么幸运，嘿嘿……\n")
        else:
            print("AI: 机智如我，怎么可能倒下，哈哈~~~\n")

print("游戏结束^_^\n")
os.system("pause")
