def console(entities):
    def traceback():
        return "\033[31m[sys] [command traceback] >>>"

    def sysmsg():
        return "\033[33m[sys] >>>"

    def UIDPe(entity=entities, value: dict = None):
        uids = []
        if value is None:
            uids.append(entity["tnt"])
            uids.append(entity["player"])
        else:
            if "type" in value:
                for uuid in entity[value["type"]]:
                    uids.append(entity[uuid])
        return uids

    commanding = False
    while True:
        command = input()
        commandl = command.split("|")
        if commanding:
            if commandl[0] == "/command":
                if len(commandl) == 1:
                    print(sysmsg(), "help of /command:\n"
                                    "/command enable  enable command control game\n"
                                    "/command disable  disable command control game")
                    continue
                if commandl[1] == "enable" or commandl[1] == "e":
                    print(sysmsg(), "command enabled")
                elif commandl[1] == "disable" or commandl[1] == "d":
                    print(sysmsg(), "command disabled")
                else:
                    print(traceback(), "unknown suffix <", commandl[1], ">")
            else:
                if len(commandl) < 3:
                    print(traceback(), "command error, error suffix or missing value")
                    continue
                commanddic = {"command": commandl[0], "UID": commandl[1]}
                for x in range(2, len(commandl)):
                    commanddic["value" + str((x - 1))] = commandl[x]
                commandx = commanddic["command"]

        else:
            # /command
            if commandl[0] == "/command":
                if len(commandl) == 1:
                    print(sysmsg(), "help of /command:\n"
                          "/command enable  enable command control game\n"
                          "/command disable  disable command control game")
                    continue
                if commandl[1] == "enable" or commandl[1] == "e":
                    print(sysmsg(), "command enabled")
                elif commandl[1] == "disable" or commandl[1] == "d":
                    print(sysmsg(), "command disabled")
                else:
                    print(traceback(), "unknown suffix <", commandl[1], ">")

            # /system
            elif commandl[0] == "/system":
                pass
            else:
                print(traceback(), "unknown command <", commandl[0], ">")

