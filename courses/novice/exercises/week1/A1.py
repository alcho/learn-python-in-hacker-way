#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
題目:
	
變數 str1 是句文言文，去掉空白後加上"我愛紅娘"，並且列印出來
"""	
str1 = '  《五音集韻》說：「人死為鬼，人見懼之；鬼死為魙，鬼見怕之。」  '

print str1.replace(' ', '') + "我愛紅娘"
