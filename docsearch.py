import re

def high_score_doc_return():
    open_doc = open('HighScore.txt', 'r')
    high_score_search = open_doc.read()

    score_search = re.compile(r'''(
[0-9]+
,
)''', re.VERBOSE)

    score_results = score_search.findall(high_score_search)
    last_score = score_results[-1:]

    num_char = str(last_score)
    num_cut = num_char[2:-3]
    high_score = int(num_cut)
    
    
    
high_score_doc_return()
