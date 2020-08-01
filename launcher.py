import easygui as g

piano = False
skin = "steve"


def launcher():
    global skin, piano
    while True:
        open_yn = g.indexbox(
            f"""
                            躲避TNT V1.2-RC-I snapshot
                                指尖钢琴模式:{piano}
                                    皮肤:{skin}
""",
            choices=["开始游戏", "退出游戏", "更换皮肤", "指尖钢琴模式"])
        if open_yn == 0:
            return piano, skin
        elif open_yn == 1 or open_yn is None:
            exit()
        elif open_yn == 2:
            skin = g.choicebox("请选择皮肤", choices=["steve", "alex", "HIM"])
        elif open_yn == 3:
            piano = not piano


def die(score, hard):
    g.msgbox("游戏结束，分数: " + str(score) + "，等级: " + str(hard))
    exit()


if __name__ == "__main__.py":
    print("This is just a launcher, plz run main.py")
