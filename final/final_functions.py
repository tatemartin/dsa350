import re

def cleanexityear(year):
    x = re.findall('\d+', year)
    if not x:
        return "N/A"
    
    if len(x[0]) == 2:
        return '19' + x[0]
    elif len(x[0]) == 1:
        return '190' + x[0]
    else:
        return x[0]

def cleanbirthyear(year):
    x = re.findall('^Died:', year)
    if x:
        return "N/A"

    y = re.findall(r'^DOB: \d+\/\d+\/(\d+)$', year)
    if y:
        if len(y[0]) == 2:
            return '19' + y[0]
        else:
            return y[0]

    z = re.findall(r'^Born: \d+\/\d+\/(\d+)$', year)
    if z:
        if len(z[0]) == 2:
            return '19' + z[0]
        else:
            return z[0]
                 
def contains_2_digits(year:str) -> bool:
    if re.search(r'^\d\d$',year) is None: return False
    return True

def contains_question(year:str) -> bool:
    if re.search(r'^?$',year) is None: return False
    return True

def contains_AD_ASTER(year:str) -> bool:
    if re.search(r'^AD ASTER$',year) is None: return False
    return True

def contains_S(year:str) -> bool:
    if re.search(r'^S$',year) is None: return False
    return True

def contains_data(year:str) -> bool:
    if re.search(r'^.$',year) is None: return False
    return True

def contains_unknown(year:str) -> bool:
    if re.search(r'^UNK$',year) is None: return False
    return True

def contains_slash(year:str) -> bool:
    if re.search(r'^\d\d\\d\d$',year) is None: return False
    return True

def contains_locations(year:str) -> bool:
    if re.search(r'^\D$',year) is None: return False
    return True

def contains_DOB(year:str) -> bool:
    if re.search(r'^DOB$',year) is None: return False
    return True

