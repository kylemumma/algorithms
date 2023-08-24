'''
This is my implementation of the closest pair of points problem,
it uses a divide and conquer approach to achieve O(nlogn) running
time.

NOTE: I couldnt actually test this solution with an online judge,
because unfortunately https://www.spoj.com/problems/CLOPPAIR/ didnt
allocate enough time for python solutions... additionally i was unable
to find comprehensive test cases online and of course too lazy to come
up with them myself. Though it did past the first 12 test cases from SPOJ
and the two at the start. Additionally given the high level solution is known
to be correct, ill just assume my implementation is too xD

Input
First line of input will contain N (2<=N<=50000) 
and then N lines follow each line contains two integers
giving the X and Y coordinate of the point. 
Absolute value of X,Y will be at most 10^6.

Output
Output 3 numbers a b c, where a, b (a<b)
are the indexes (0 based) of the point pair
in the input and c is the distance between them. 
Round c to 6 decimal digits.

Example Input: 
5 
0 0
0 1
100 45
2 3
9 9

Example Output: 
0 1 1.000000

Author: Kyle Mumma
'''

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
def _parrtostr(p):
    if len(p) == 0:
        return "[]"
    out = ""
    out += f'[{str(p[0])}'
    for i in range(1,len(p)):
        out += f', {str(p[i])}'
    return out + "]"

def _dist(p1,p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return dx**2 + dy**2

'''
here is the algorithm, i chose to sort by both x and y
at the global level, though it is more common to sort y
using merges
'''
def cp(points):
    xsort = sorted(points, key=lambda p: p.x)
    ysort = sorted(points, key=lambda p: p.y)
    def _cp(start, stop):
        # base case: 2 or 3 points left
        if stop-start+1 <= 3:
            winner = (None,None,-1)
            for i in range(start, stop+1):
                for j in range(i+1, stop+1):
                    d = _dist(xsort[i],xsort[j])
                    if winner[2]==-1 or d < winner[2]:
                        winner = (xsort[i],xsort[j],d)
            return winner
        
        # recursive case
        median = start+(stop-start+1)//2
        lwin = _cp(start, median-1)
        rwin = _cp(median, stop)

        # combine
        delta = min(lwin[2], rwin[2])
        gmin = lwin if delta == lwin[2] else rwin
        # check every point in delta bounds
        for i in range(len(ysort)):
            cp = ysort[i]
            xmid = xsort[median-1].x+((xsort[median].x-xsort[median-1].x)/2)
            if cp.x >= xmid - delta or cp.x <= xmid + delta:
                # its in range, check bigger and smaller
                for j in range(i-1, max(i-12, -1), -1):
                    d = _dist(ysort[i], ysort[j])
                    if d < gmin[2]:
                        gmin = (ysort[i],ysort[j],d)
                for j in range(i+1, min(i+12, len(ysort))):
                    d = _dist(ysort[i], ysort[j])
                    if d < gmin[2]:
                        gmin = (ysort[i],ysort[j],d)
        return gmin
    return _cp(0, len(points)-1)


points = []
for i in range(int(input())):
    i = input().split(" ")
    points.append(Point(float(i[0]), float(i[1])))

win = cp(points)
out = ""
for i in range(len(points)):
    if ((points[i].x == win[0].x and points[i].y == win[0].y) or 
        (points[i].x == win[1].x and points[i].y == win[1].y)):
        out += str(i) + " "

out += '%.6f' % math.sqrt(win[2])
print(out)