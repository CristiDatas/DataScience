import pandas as pd
from functools import wraps
import matplotlib.pyplot as plt


def prepost(key_url):
    def inner(function):
        @wraps(function)
        def wrapper(*a, **k):
            if key_url:
               df=pd.read_csv(key_url)
            retval = function(*a, **k)
            df.hist()
            plt.show()
            return retval
        return wrapper
    return inner

@prepost(key_url="http://winterolympicsmedals.com/medals.csv")   
def _f_protected():
    lamb=lambda x: (x>5)
    l1=[x for x in range(1,16)]
    l1_filtrada = list(filter(lamb, l1))
    print(l1_filtrada)
    return l1_filtrada

filtered=_f_protected()

filtered

