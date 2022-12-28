import re

test = 'TRINITY_GG_100000_c20_g1_i1'



matchobj = re.match(r'(\S)+_i',test)

if matchobj:
    print('matchobj.group()',matchobj.group())
    print('matchobj.group()',matchobj.group().split('_i')[0])
    print('matchobj.group()',matchobj.group(1))