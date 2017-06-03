def bw(sf):
    wds = sf.split(' ')
    return wds
def sw(ws):
    return sorted(ws)
def pfw(ws):
    wd = ws.pop(0)
    print wd
def plw(ws):
    wd = ws.pop(-1)
    print wd
def ss(st):
    ws = bw(st)
    return sw(ws)
def pfal(st):
    ws = bw(st)
    pfw(ws)
    plw(ws)
def pfals(st):
    ws = ss(st)
    pfw(ws)
    plw(ws)
#$ python
# Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05)
# [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
#>>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
#['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
#['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
