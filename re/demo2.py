#!/usr/bin/env python
#coding:utf-8
import re
'''
Match 对象属性讲解

'''
pattern = re.compile(r'(\w+) (\w+) (?P<word>.*)')
match = pattern.match('I love you!')

print('match.string',match.string)
print('match.re',match.re)
print('match.pos',match.pos)
print('match.endpos',match.endpos)
print('match.lastindex',match.lastindex)
print('match.lastgroup',match.lastgroup)

print('match.group(1,2)',match.group(1,2))
print('match.groups()',match.groups())
print('match.groupdict()',match.groupdict())
print('match.start(2)',match.start(2))
print('match.end(2)',match.end(2))
print('match.span(2)',match.span(2))
print(r"match.expand(r'\2 \1 \3')",match.expand(r'\2 \1 \3'))
