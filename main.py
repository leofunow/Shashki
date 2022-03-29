from tkinter import *

import numpy

SHAHSKI = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
           [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
           [2, 0, 2, 0, 2, 0, 2, 0, 2, 0]]

root = Tk()
root.title("шашки")
root.minsize(width=500, height=600)
root.maxsize(width=500, height=600)

XX = 0
YY = 0

XXX = 0
YYY = 0

whitekills = 0
blackkills = 0

canv = Canvas(root, width=500, height=600)
tmp = False
turn = False  # ход белых
flag_repeat = False


def redraw():
    global SHAHSKI
    canv.delete("text")
    if whitekills == 15:
        canv.create_text(250, 570, text="Победа белых", tags="text")
        canv.tag_unbind("<Button-1>")
    if blackkills == 15:
        canv.create_text(250, 570, text="Победа черных", tags="text")
        canv.tag_unbind("<Button-1>")
    if turn:
        canv.create_text(250, 510, text="ход черных", tags="text")
    else:
        canv.create_text(250, 510, text="ход белых", tags="text")
    canv.create_text(200, 550, text=("Счет белых:" + str(whitekills)), tags="text")
    canv.create_text(300, 550, text=("Счет черных:" + str(blackkills)), tags="text")
    canv.delete("shahka")
    canv.dtag("shahka")
    canv.clipboard_clear()
    for i in range(0, 10):
        for j in range(0, 10):
            if j == 9 and SHAHSKI[j][i] == 1:
                SHAHSKI[j][i] = 3
            if j == 0 and SHAHSKI[j][i] == 2:
                SHAHSKI[j][i] = 4
            if SHAHSKI[j][i] == 1:
                canv.create_oval(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill='black', tags="shahka")
            elif SHAHSKI[j][i] == 2:
                canv.create_oval(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill='white', tags="shahka")
            elif SHAHSKI[j][i] == 3:
                canv.create_oval(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill='black', tags="shahka")
                canv.create_oval(i * 50 + 10, j * 50 + 10, i * 50 + 40, j * 50 + 40, fill='gray', tags="shahka")
            elif SHAHSKI[j][i] == 4:
                canv.create_oval(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill='white', tags="shahka")
                canv.create_oval(i * 50 + 10, j * 50 + 10, i * 50 + 40, j * 50 + 40, fill='gray', tags="shahka",
                                 width=0)


def move(x1, y1, x2, y2, *args):
    redraw()
    global flag_repeat
    global turn
    global YY
    global XX
    global whitekills
    global blackkills
    global canv
    global XXX
    global YYY
    line = []
    niceflag = 0

    if flag_repeat:
        if turn:
            if SHAHSKI[YYY][XXX] == 1:
                if abs(XXX - x2) == 2 and abs(YYY - y2) == 2:
                    if (SHAHSKI[int((YYY + y2) / 2)][int((XXX + x2) / 2)] == 2 or SHAHSKI[int((YYY + y2) / 2)][
                        int((XXX + x2) / 2)] == 4) and SHAHSKI[y2][x2] == 0:
                        SHAHSKI[YYY][XXX] = 0
                        SHAHSKI[y2][x2] = 1
                        SHAHSKI[int((YYY + y2) / 2)][int((XXX + x2) / 2)] = 0
                        blackkills += 1
                        flag_repeat = False
                        turn = not turn
                        try:
                            if ((SHAHSKI[y2 + 1][x2 + 1] == 2 or SHAHSKI[y2 + 1][x2 + 1] == 4) and SHAHSKI[y2 + 2][
                                x2 + 2] == 0):
                                YY = y2
                                XX = x2
                                YYY = y2
                                XXX = x2
                                turn = not turn
                                click(*args)
                                flag_repeat = True
                        except:
                            EXCEPTION
                        try:
                            if ((SHAHSKI[y2 - 1][x2 + 1] == 2 or SHAHSKI[y2 - 1][x2 + 1] == 4) and SHAHSKI[y2 - 2][
                                x2 + 2] == 0):
                                YY = y2
                                XX = x2
                                YYY = y2
                                XXX = x2
                                turn = not turn
                                click(*args)
                                flag_repeat = True
                        except:
                            EXCEPTION
                        try:
                            if ((SHAHSKI[y2 + 1][x2 - 1] == 2 or SHAHSKI[y2 + 1][x2 - 1] == 4) and SHAHSKI[y2 + 2][
                                x2 - 2] == 0):
                                YY = y2
                                XX = x2
                                YYY = y2
                                XXX = x2
                                turn = not turn
                                click(*args)
                                flag_repeat = True
                        except:
                            EXCEPTION
                        try:
                            if ((SHAHSKI[y2 - 1][x2 - 1] == 2 or SHAHSKI[y2 - 1][x2 - 1] == 4) and SHAHSKI[y2 - 2][
                                x2 - 2] == 0):
                                YY = y2
                                XX = x2
                                YYY = y2
                                XXX = x2
                                turn = not turn
                                click(*args)
                                flag_repeat = True
                        except:
                            EXCEPTION
            elif SHAHSKI[YYY][XXX] == 3:
                direction_y = numpy.sign(y2 - YYY)
                direction_x = numpy.sign(x2 - XXX)

                if abs(x2 - XXX) == abs(y2 - YYY):
                    for i in range(0, abs(y2 - YYY) + 1):
                        line.append(SHAHSKI[YYY + i * direction_y][XXX + i * direction_x])

                err = 0
                for i in range(1, len(line) - 1):
                    if line[i] == 3 or line[i] == 1:
                        err = 1
                    if (line[i] == 2 or line[i] == 4) and (line[i + 1] == 2 or line[i + 1] == 4):
                        err = 1
                if line[len(line) - 1] != 0:
                    err = 1
                if err == 0:
                    for i in range(1, len(line)):
                        if line[i] == 2 or line[i] == 4:
                            SHAHSKI[YYY + i * direction_y][XXX + i * direction_x] = 0
                            blackkills += 1
                            niceflag = 1
                    SHAHSKI[y2][x2] = 3
                    SHAHSKI[YYY][XXX] = 0
                    YYY = y2
                    XXX = x2
                    turn = not turn
                    flag_repeat = False
                    if niceflag == 1:
                        lines = [[], [], [], []]
                        for i in range(0, 4):
                            if i < 2:
                                direction_y = -1
                            else:
                                direction_y = 1
                            if i % 2 == 0:
                                direction_x = -1
                            else:
                                direction_x = 1
                            sch = 0
                            while 0 <= YYY + sch * direction_y < 10 and 0 <= XXX + sch * direction_x < 10:
                                sch += 1
                            for j in range(0, sch):
                                lines[i].append(SHAHSKI[YYY + j * direction_y][XXX + j * direction_x])
                            err = 1
                            for j in range(1, sch - 1):
                                if (lines[i][j] == 2 or lines[i][j] == 4) and (
                                        lines[i][j + 1] == 2 or lines[i][j + 1] == 4) or (
                                        lines[i][j] == 1 or lines[i][j] == 3):
                                    err = 1
                                    break
                                if (lines[i][j] == 2 or lines[i][j] == 4) and lines[i][j + 1] == 0:
                                    err = 0
                                    break
                                if lines[i][j + 1] != 0 and j == sch - 2:
                                    err = 1
                            if err == 0:
                                flag_repeat = True
                                YY = y2
                                XX = x2
                                YYY = y2
                                XXX = x2
                                turn = not turn
                                click(*args)
                                flag_repeat = True
                                return

                # while 0 <= YYY + sch*direction_y < 10 and 0 <= XXX + sch*direction_x < 10:
                #     sch += 1

        elif SHAHSKI[YYY][XXX] == 2:
            if abs(XXX - x2) == 2 and abs(YYY - y2) == 2:
                if (SHAHSKI[int((YYY + y2) / 2)][int((XXX + x2) / 2)] == 1 or SHAHSKI[int((YYY + y2) / 2)][
                    int((XXX + x2) / 2)] == 3) and SHAHSKI[y2][x2] == 0:
                    SHAHSKI[YYY][XXX] = 0
                    SHAHSKI[y2][x2] = 2
                    SHAHSKI[int((YYY + y2) / 2)][int((XXX + x2) / 2)] = 0
                    whitekills += 1
                    flag_repeat = False
                    turn = not turn
                    try:
                        if ((SHAHSKI[y2 + 1][x2 + 1] == 1 or SHAHSKI[y2 + 1][x2 + 1] == 3) and SHAHSKI[y2 + 2][
                            x2 + 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
                    try:
                        if ((SHAHSKI[y2 - 1][x2 + 1] == 1 or SHAHSKI[y2 - 1][x2 + 1] == 3) and SHAHSKI[y2 - 2][
                            x2 + 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
                    try:
                        if ((SHAHSKI[y2 + 1][x2 - 1] == 1 or SHAHSKI[y2 + 1][x2 - 1] == 3) and SHAHSKI[y2 + 2][
                            x2 - 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
                    try:
                        if ((SHAHSKI[y2 - 1][x2 - 1] == 1 or SHAHSKI[y2 - 1][x2 - 1] == 3) and SHAHSKI[y2 - 2][
                            x2 - 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
        elif SHAHSKI[YYY][XXX] == 4:
            direction_y = numpy.sign(y2 - YYY)
            direction_x = numpy.sign(x2 - XXX)

            if abs(x2 - XXX) == abs(y2 - YYY):
                for i in range(0, abs(y2 - YYY) + 1):
                    line.append(SHAHSKI[YYY + i * direction_y][XXX + i * direction_x])

            err = 0
            for i in range(1, len(line) - 1):
                if line[i] == 4 or line[i] == 2:
                    err = 1
                if (line[i] == 1 or line[i] == 3) and (line[i + 1] == 1 or line[i + 1] == 3):
                    err = 1
            if line[len(line) - 1] != 0:
                err = 1
            if err == 0:
                for i in range(1, len(line)):
                    if line[i] == 1 or line[i] == 3:
                        SHAHSKI[YYY + i * direction_y][XXX + i * direction_x] = 0
                        whitekills += 1
                        niceflag = 1
                SHAHSKI[y2][x2] = 4
                SHAHSKI[YYY][XXX] = 0
                turn = not turn
                YYY = y2
                XXX = x2
                flag_repeat = False
                if niceflag == 1:
                    lines = [[], [], [], []]
                    for i in range(0, 4):
                        if i < 2:
                            direction_y = -1
                        else:
                            direction_y = 1
                        if i % 2 == 0:
                            direction_x = -1
                        else:
                            direction_x = 1
                        sch = 0
                        while 0 <= YYY + sch * direction_y < 10 and 0 <= XXX + sch * direction_x < 10:
                            sch += 1
                        for j in range(0, sch):
                            lines[i].append(SHAHSKI[YYY + j * direction_y][XXX + j * direction_x])
                        err = 1
                        for j in range(1, sch - 1):
                            if (lines[i][j] == 1 or lines[i][j] == 3) and (
                                    lines[i][j + 1] == 1 or lines[i][j + 1] == 3) or (
                                    lines[i][j] == 2 or lines[i][j] == 4):
                                err = 1
                                break
                            if (lines[i][j] == 1 or lines[i][j] == 3) and lines[i][j + 1] == 0:
                                err = 0
                                break
                            if lines[i][j + 1] != 0 and j == sch - 2:
                                err = 1
                        if err == 0:
                            flag_repeat = True
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True

                            return

    elif turn:
        if SHAHSKI[y1][x1] == 1:
            if abs(x1 - x2) == 1 and y2 - y1 == 1:
                if SHAHSKI[y2][x2] == 0:
                    SHAHSKI[y1][x1] = 0
                    SHAHSKI[y2][x2] = 1
                    turn = not turn
            elif abs(x1 - x2) == 2 and abs(y1 - y2) == 2:
                if (SHAHSKI[int((y1 + y2) / 2)][int((x1 + x2) / 2)] == 2 or SHAHSKI[int((y1 + y2) / 2)][
                    int((x1 + x2) / 2)] == 4) and SHAHSKI[y2][x2] == 0:
                    SHAHSKI[y1][x1] = 0
                    SHAHSKI[y2][x2] = 1
                    SHAHSKI[int((y1 + y2) / 2)][int((x1 + x2) / 2)] = 0
                    blackkills += 1
                    turn = not turn
                    try:
                        if ((SHAHSKI[y2 + 1][x2 + 1] == 2 or SHAHSKI[y2 + 1][x2 + 1] == 4) and SHAHSKI[y2 + 2][
                            x2 + 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
                    try:
                        if ((SHAHSKI[y2 - 1][x2 + 1] == 2 or SHAHSKI[y2 - 1][x2 + 1] == 4) and SHAHSKI[y2 - 2][
                            x2 + 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
                    try:
                        if ((SHAHSKI[y2 + 1][x2 - 1] == 2 or SHAHSKI[y2 + 1][x2 - 1] == 4) and SHAHSKI[y2 + 2][
                            x2 - 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
                    try:
                        if ((SHAHSKI[y2 - 1][x2 - 1] == 2 or SHAHSKI[y2 - 1][x2 - 1] == 4) and SHAHSKI[y2 - 2][
                            x2 - 2] == 0):
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                    except:
                        EXCEPTION
        elif SHAHSKI[y1][x1] == 3:
            direction_y = numpy.sign(y2 - y1)
            direction_x = numpy.sign(x2 - x1)

            if abs(x2 - x1) == abs(y2 - y1):
                for i in range(0, abs(y2 - y1) + 1):
                    line.append(SHAHSKI[y1 + i * direction_y][x1 + i * direction_x])

            err = 0
            for i in range(1, len(line) - 1):
                if line[i] == 3 or line[i] == 1:
                    err = 1
                if (line[i] == 2 or line[i] == 4) and (line[i + 1] == 2 or line[i + 1] == 4):
                    err = 1
            if line[len(line) - 1] != 0:
                err = 1
            if err == 0:
                for i in range(1, len(line)):
                    if line[i] == 2 or line[i] == 4:
                        SHAHSKI[y1 + i * direction_y][x1 + i * direction_x] = 0
                        blackkills += 1
                        niceflag = 1
                SHAHSKI[y2][x2] = 3
                SHAHSKI[y1][x1] = 0
                turn = not turn
                YYY = y2
                XXX = x2
                flag_repeat = False
                if niceflag == 1:
                    lines = [[], [], [], []]
                    for i in range(0, 4):
                        if i < 2:
                            direction_y = -1
                        else:
                            direction_y = 1
                        if i % 2 == 0:
                            direction_x = -1
                        else:
                            direction_x = 1
                        sch = 0
                        while 0 <= YYY + sch * direction_y < 10 and 0 <= XXX + sch * direction_x < 10:
                            sch += 1
                        for j in range(0, sch):
                            lines[i].append(SHAHSKI[YYY + j * direction_y][XXX + j * direction_x])
                        err = 1
                        for j in range(1, sch - 1):
                            if (lines[i][j] == 2 or lines[i][j] == 4) and (
                                    lines[i][j + 1] == 2 or lines[i][j + 1] == 4) or (
                                    lines[i][j] == 1 or lines[i][j] == 3):
                                err = 1
                                break
                            if (lines[i][j] == 2 or lines[i][j] == 4) and lines[i][j + 1] == 0:
                                err = 0
                                break
                            if lines[i][j + 1] != 0 and j == sch - 2:
                                err = 1
                        if err == 0:
                            flag_repeat = True
                            YY = y2
                            XX = x2
                            YYY = y2
                            XXX = x2
                            turn = not turn
                            click(*args)
                            flag_repeat = True
                            return

            # while 0 <= y1 + sch*direction_y < 10 and 0 <= x1 + sch*direction_x < 10:
            #     sch += 1
    elif SHAHSKI[y1][x1] == 2:
        if abs(x1 - x2) == 1 and y1 - y2 == 1:
            if SHAHSKI[y2][x2] == 0:
                SHAHSKI[y1][x1] = 0
                SHAHSKI[y2][x2] = 2
                turn = not turn
        elif abs(x1 - x2) == 2 and abs(y1 - y2) == 2:
            if (SHAHSKI[int((y1 + y2) / 2)][int((x1 + x2) / 2)] == 1 or SHAHSKI[int((y1 + y2) / 2)][
                int((x1 + x2) / 2)] == 3) and SHAHSKI[y2][x2] == 0:
                SHAHSKI[y1][x1] = 0
                SHAHSKI[y2][x2] = 2
                SHAHSKI[int((y1 + y2) / 2)][int((x1 + x2) / 2)] = 0
                whitekills += 1
                turn = not turn
                try:
                    if ((SHAHSKI[y2 + 1][x2 + 1] == 1 or SHAHSKI[y2 + 1][x2 + 1] == 3) and SHAHSKI[y2 + 2][
                        x2 + 2] == 0):
                        YY = y2
                        XX = x2
                        YYY = y2
                        XXX = x2
                        turn = not turn
                        click(*args)
                        flag_repeat = True
                except:
                    EXCEPTION
                try:
                    if ((SHAHSKI[y2 - 1][x2 + 1] == 1 or SHAHSKI[y2 - 1][x2 + 1] == 3) and SHAHSKI[y2 - 2][
                        x2 + 2] == 0):
                        YY = y2
                        XX = x2
                        YYY = y2
                        XXX = x2
                        turn = not turn
                        click(*args)
                        flag_repeat = True
                except:
                    EXCEPTION
                try:
                    if ((SHAHSKI[y2 + 1][x2 - 1] == 1 or SHAHSKI[y2 + 1][x2 - 1] == 3) and SHAHSKI[y2 + 2][
                        x2 - 2] == 0):
                        YY = y2
                        XX = x2
                        YYY = y2
                        XXX = x2
                        turn = not turn
                        click(*args)
                        flag_repeat = True
                except:
                    EXCEPTION
                try:
                    if ((SHAHSKI[y2 - 1][x2 - 1] == 1 or SHAHSKI[y2 - 1][x2 - 1] == 3) and SHAHSKI[y2 - 2][
                        x2 - 2] == 0):
                        YY = y2
                        XX = x2
                        YYY = y2
                        XXX = x2
                        turn = not turn
                        click(*args)
                        flag_repeat = True
                except:
                    EXCEPTION
    elif SHAHSKI[y1][x1] == 4:
        direction_y = numpy.sign(y2 - y1)
        direction_x = numpy.sign(x2 - x1)

        if abs(x2 - x1) == abs(y2 - y1):
            for i in range(0, abs(y2 - y1) + 1):
                line.append(SHAHSKI[y1 + i * direction_y][x1 + i * direction_x])

        err = 0
        for i in range(1, len(line) - 1):
            if line[i] == 4 or line[i] == 2:
                err = 1
            if (line[i] == 1 or line[i] == 3) and (line[i + 1] == 1 or line[i + 1] == 3):
                err = 1
        if line[len(line) - 1] != 0:
            err = 1
        if err == 0:
            for i in range(1, len(line)):
                if line[i] == 1 or line[i] == 3:
                    SHAHSKI[y1 + i * direction_y][x1 + i * direction_x] = 0
                    whitekills += 1
                    niceflag = 1
            SHAHSKI[y2][x2] = 4
            SHAHSKI[y1][x1] = 0
            turn = not turn
            YYY = y2
            XXX = x2
            flag_repeat = False
            if niceflag == 1:
                lines = [[], [], [], []]
                for i in range(0, 4):
                    if i < 2:
                        direction_y = -1
                    else:
                        direction_y = 1
                    if i % 2 == 0:
                        direction_x = -1
                    else:
                        direction_x = 1
                    sch = 0
                    while 0 <= YYY + sch * direction_y < 10 and 0 <= XXX + sch * direction_x < 10:
                        sch += 1
                    for j in range(0, sch):
                        lines[i].append(SHAHSKI[YYY + j * direction_y][XXX + j * direction_x])
                    err = 1
                    for j in range(1, sch - 1):
                        if (lines[i][j] == 1 or lines[i][j] == 3) and (
                                lines[i][j + 1] == 1 or lines[i][j + 1] == 3) or (
                                lines[i][j] == 2 or lines[i][j] == 4):
                            err = 1
                            break
                        if (lines[i][j] == 1 or lines[i][j] == 3) and lines[i][j + 1] == 0:
                            err = 0
                            break
                        if lines[i][j + 1] != 0 and j == sch - 2:
                            err = 1
                    if err == 0:
                        flag_repeat = True
                        YY = y2
                        XX = x2
                        YYY = y2
                        XXX = x2
                        turn = not turn
                        click(*args)
                        flag_repeat = True

                        return


def click(*args):
    global XX
    global YY
    global canv

    YY = int(args[0].y / 50)
    XX = int(args[0].x / 50)
    if YY >= 10:
        YY = 9
    if XX >= 10:
        XX = 9

    if turn and (SHAHSKI[YY][XX] == 1 or SHAHSKI[YY][XX] == 3) or (not turn) and (
            SHAHSKI[YY][XX] == 2 or SHAHSKI[YY][XX] == 4):
        canv.bind("<Button-1>", click2)


def click2(*args):
    global XX
    global YY
    global canv
    if args[0].y >= 500:
        args[0].y = 475
    if args[0].x >= 500:
        args[0].x = 475
    if turn and (SHAHSKI[int(args[0].y / 50)][int(args[0].x / 50)] == 1 or SHAHSKI[int(args[0].y / 50)][
        int(args[0].x / 50)] == 3) or (not turn) and (SHAHSKI[int(args[0].y / 50)][
                                                          int(args[0].x / 50)] == 2 or SHAHSKI[int(args[0].y / 50)][
                                                          int(args[0].x / 50)] == 4):
        click(*args)
        return

    canv.bind("<Button-1>", click)
    move(XX, YY, int(args[0].x / 50), int(args[0].y / 50), *args)
    redraw()


for i in range(0, 10):
    tmp = not tmp
    for j in range(0, 10):
        tmp = not tmp
        if (tmp):
            canv.create_rectangle(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill="gray")
        else:
            canv.create_rectangle(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill="lightgray")

redraw()
canv.bind("<Button-1>", click)

canv.pack()
root.mainloop()
