#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mycart = ('мяч','палка','луна','садик','дерево','небо')
s=input("Введите элемент картежа ")
if s not in mycart:
    print("Такого элемента в списке нет")
else:
    print(mycart.index(s))
