import easygui as g

skin = "steve"
frame = 180
bgm_name_list = ["不选择", "Flamingo（米津玄师）", "LOSER（米津玄师）", "Man At Arms（Position music）",
                 "Nyan Cat（daniwellP/桃音モモ）", "千本樱（黒うさP/初音ミク）"
                 ]
now_music = bgm_name_list[0]
set_music = None


def launcher():
    global skin, frame, bgm_name_list, now_music, set_music
    while True:
        open_yn = g.indexbox(
            f"""
                              躲避TNT V1.3.2-alpha-I
                                    皮肤:{skin}
                                    bgm：{now_music}
                                    tps:{frame} 
""", choices=["开始游戏", "退出游戏", "更换皮肤", "设置背景音乐", "设置tps"])
        if open_yn == 0:
            return skin, frame, set_music
        elif open_yn == 1 or open_yn is None:
            exit()
        elif open_yn == 2:
            skin = g.choicebox("请选择皮肤", choices=["steve", "alex", "HIM"])
        elif open_yn == 3:
            music_choose = g.choicebox("请选择背景音乐", choices=bgm_name_list)
            if music_choose == "不选择":
                set_music = None
                now_music = bgm_name_list[0]
            elif music_choose == "Flamingo（米津玄师）":
                set_music = "Flamingo.mp3"
                now_music = bgm_name_list[1]
            elif music_choose == "LOSER（米津玄师）":
                set_music = "LOSER.mp3"
                now_music = bgm_name_list[2]
            elif music_choose == "Man At Arms（Position music）":
                set_music = "ManAtArms.mp3"
                now_music = bgm_name_list[3]
            elif music_choose == "Nyan Cat（daniwellP/桃音モモ）":
                set_music = "NyanCat.mp3"
                now_music = bgm_name_list[4]
            elif music_choose == "千本樱（黒うさP/初音ミク）":
                set_music = "千本樱.mp3"
                now_music = bgm_name_list[5]
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
                g.msgbox("错误的tps数！")
                frame = 180


def die(score, hard, ele_time, sr, nr):
    print("\n\n\n"
          "你死了！\n"
          "You died!")
    print(f"""
==========游戏报告==========
分数: {str(score)} 
等级: {str(hard)}
技能使用次数: {ele_time}
存活时间: {round(nr - sr, 2)}s
==========================

==========Game report==========
score: {str(score)} 
level: {str(hard)}
skill used: {ele_time}
living time: {round(nr - sr, 2)}s
===============================
""")
    input("""
    按下回车退出游戏
    press [Enter] to end game\n
    """)
    exit()


if __name__ == "__main__.py":
    print("This is just a launcher, plz run main.py")
