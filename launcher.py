import easygui as g

piano = False
skin = "steve"
frame = 180


def launcher():
    global skin, piano, frame
    while True:
        open_yn = g.indexbox(
            f"""
                            躲避TNT V1.2-RC-I snapshot
                                指尖钢琴模式:{piano}
                                    皮肤:{skin}
                                    tps:{frame} 
""",
            choices=["开始游戏", "退出游戏", "更换皮肤", "指尖钢琴模式", "设置游戏帧数"])
        if open_yn == 0:
            return piano, skin, frame
        elif open_yn == 1 or open_yn is None:
            exit()
        elif open_yn == 2:
            skin = g.choicebox("请选择皮肤", choices=["steve", "alex", "HIM"])
        elif open_yn == 3:
            piano = not piano
        elif open_yn == 4:
            frame = g.enterbox(f"请输入你要设置的tps（数字）\n当前值为{frame}，不可低于100（越低越难，越高不会越简单）")
            try:
                if frame is not None:
                    frame = int(frame)
                    if frame < 100:
                        g.msgbox("错误的tps数，tps不可低于100")
                        frame = 100
                else:
                    frame = 180
            except ValueError:
                g.msgbox("错误的帧数！")
                frame = 180


def die(score, hard):
    g.msgbox("游戏结束，分数: " + str(score) + "，等级: " + str(hard))
    exit()


if __name__ == "__main__.py":
    print("This is just a launcher, plz run main.py")
