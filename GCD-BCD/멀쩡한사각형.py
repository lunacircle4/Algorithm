# https://programmers.co.kr/learn/courses/30/lessons/62048
##

from math import gcd

def solution(w,h):
    _gcd = gcd(w, h)
    return w * h - _gcd * (w // _gcd + h // _gcd - 1)
