import pandas as pd
def convertoHtml(result,title):
    d={}
    index=0
    for t in title:
        d[t]=result[index]
        index=index+1
    df=pd.DataFrame(d)
    df = df[title]
    pd.set_option('display.max_colwidth', 1500)
    h = df.to_html(index=False)
    #pd.set_option('max_colwidth', 200)
    #pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_colwidth', 1500)
    return h