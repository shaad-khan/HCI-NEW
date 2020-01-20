import re
def PercentageConversion(x):
    if re.search('%$',x):
        try:
            item=x.replace("%","")
            item=(float(item)/100)
            return item
        except Exception as ex:
            
             return item
    else:
        return x
