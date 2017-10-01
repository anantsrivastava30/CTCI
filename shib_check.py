#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
nn = [float('inf'),float('inf')]
ne = [float('inf'),float('inf')]
ee = [float('inf'),float('inf')]
se = [float('inf'),float('inf')]
ss = [float('inf'),float('inf')]
sw = [float('inf'),float('inf')]
ww = [float('inf'),float('inf')]
nw = [float('inf'),float('inf')]
obst = []
for a0 in range(k):
    robst,cobst = input().strip().split(' ')
    obst.append([robst,cobst])
    robst,cobst = [int(robst),int(cobst)]


count=8
print(count)
dir_obst = {k: [-1,-1] for k in range(1,9)}

print(count)
while count!=0:
    print(count)
    # Direction North
    if count == 8:
        obs = False
        r = rQueen
        while obs == False or r!=n+1:
            if [r+1, cQueen] not in obst:
                r = r+1
            else:
                obs = True
                dir_obst[count] = [r+1,cQueen]

    # Direction North-East
    if count == 7:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or r!=n+1 or c!=n+1:
            if [r+1, c+1] not in obst:
                r = r+1
                c = c+1
            else:
                obs = True
                dir_obst[count] = [r+1,c+1]

    # Direction East
    if count == 6:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or c!=n+1:
            if [r, c+1] not in obst:
                c = c+1
            else:
                obs = True
                dir_obst[count] = [r,c+1]

    # Direction South-East
    if count == 5:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or c!=n+1 or r!=0:
            if [r-1, c+1] not in obst:
                r = r-1
                c = c+1
            else:
                obs = True
                dir_obst[count] = [r-1,c+1]

    # Direction South
    if count == 4:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or r!=0:
            if [r-1, c] not in obst:
                r = r-1
            else:
                obs = True
                dir_obst[count] = [r-1,c]


    # Direction South-West
    if count == 3:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or c!=0 or r!=0:
            if [r-1, c-1] not in obst:
                r = r-1
                c = c-1
            else:
                obs = True
                dir_obst[count] = [r-1,c-1]

    # Direction West
    if count == 2:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or c!=0 :
            if [r, c-1] not in obst:
                c = c-1
            else:
                obs = True
                dir_obst[count] = [r,c-1]

    # Direction North-West
    if count == 1:
        obs = False
        r = rQueen
        c = cQueen
        while obs == False or c!=0 or r!=n+1 :
            if [r+1, c-1] not in obst:
                c = c-1
                r = r+1
            else:
                obs = True
                dir_obst[count] = [r+1,c-1]
    print(count)
    count -= 1

num_pos = 0
print(dir_obst)
for k,v in dir_obst:
    if k == 8:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + (n+1 - rQueen) - 1
        else:
            num_pos = num_pos + ((dir_obst[k])[0] - rQueen - 1)

    if k == 7:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + min((n+1 - rQueen), (n+1 - cQueen) ) -1
        else:
            num_pos = num_pos + min(((dir_obst[k])[0] - rQueen), ((dir_obst[k])[1] - cQueen) ) -1

    if k == 6:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + (n+1 - cQueen)  -1
        else:
            num_pos = num_pos + (dir_obst[k])[0] - rQueen -1


    if k == 5:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + min(n - (n+1 - rQueen), (n+1 - cQueen) ) -1
        else:
            num_pos = num_pos + min(abs((dir_obst[k])[0] - rQueen), abs((dir_obst[k])[1] - cQueen) ) -1

    if k == 4:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + n - (n+1 - rQueen)
        else:
            num_pos = num_pos + abs((dir_obst[k])[0] - rQueen) -1

    if k == 3:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + min(n - (n+1 - rQueen), n - (n+1 - cQueen) ) -1
        else:
            num_pos = num_pos + min(abs((dir_obst[k])[0] - rQueen), abs((dir_obst[k])[1] - cQueen) ) -1

    if k == 2:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + n - (n+1 - cQueen)  -1
        else:
            num_pos = num_pos + abs((dir_obst[k])[1] - cQueen) -1

    if k == 1:
        if dir_obst[k] == [-1,-1]:
            num_pos = num_pos + min((n+1 - rQueen), n - (n+1 - cQueen) ) -1
        else:
            num_pos = num_pos + min(abs((dir_obst[k])[0] - rQueen), abs((dir_obst[k])[1] - cQueen) ) -1

print(num_pos)

"""
    r = rQueen - robst
    c = cQueen - cobst
    # ne, se, sw, nw
    if abs(r) == (c):
        # ne
        if r < 0 and c < 0:
            ne = min(ne,[robst,cobst])
        # se
        if r > 0 and c < 0:
            se = min(se,[robst,cobst])
        # sw
        if r > 0 and c > 0:
            sw = min(sw,[robst,cobst])
        # nw
        if r < 0 and c > 0:
            nw = min(nw,[robst,cobst])
    if r == 0:
        # ww
        if c > 0:
            ww = min(ww,[robst,cobst])
        # ee
        if c < 0:
            ee = min(ee,[robst,cobst])
    if c == 0:
        # ss
        if r > 0:
            ss = min(ss,[robst,cobst])
        # nn
        if r < 0:
            nn = min(nn,[robst,cobst])

print(nn,ss,ww,ee,sw,se,nw,ne)
nn = abs(n - rQueen) if nn == [float('inf'),float('inf')] else  abs(nn[0] - rQueen)
ss = abs(rQueen - 1) if ss == [float('inf'),float('inf')] else  abs(rQueen - ss[0] - 1)
ee = abs(n - cQueen) if ee == [float('inf'),float('inf')] else  abs(ee[1] - cQueen)
ww = abs(cQueen - 1) if ww == [float('inf'),float('inf')] else  abs(cQueen - ww[1] - 1)

ne = min(abs(n - rQueen),abs(n - cQueen)) if ne == [float('inf'),float('inf')] \
                else min(abs(ne[0] - rQueen),abs(ne[1] - cQueen))

se = min(abs(rQueen - 1),abs(n - cQueen)) if se == [float('inf'),float('inf')] \
                else min(abs(rQueen - se[0] - 1),abs(se[1] - cQueen))

sw = min(abs(rQueen - 1),abs(cQueen - 1)) if sw == [float('inf'),float('inf')] \
                else min(abs(rQueen - sw[0] - 1),abs(rQueen - sw[1] - 1))

nw = min(abs(n - rQueen),abs(cQueen - 1)) if nw == [float('inf'),float('inf')] \
                else min(abs(nw[0] - rQueen),abs(cQueen - nw[1] - 1))

print(nn,ss,ww,ee,sw,se,nw,ne)
"""

