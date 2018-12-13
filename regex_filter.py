import requests,json,re
from collections import defaultdict
class RegexFilter:
    def __init__(self,inputfile,ftype,regexdict):
        self.inputfile = inputfile
        self.regexdict = regexdict
        self.ftype = ftype
        self.final_result = defaultdict(list)
        
        if self.ftype == 'offline':
            print('woot')
        elif self.ftype == 'online':
            for each_url in self.inputfile:
                req = requests.get(each_url)
                for description,pattern in regexdict.items():
                    pattern =  r"{}".format(pattern)
                    regex = re.compile(pattern).findall(req.text)
                    if len(regex) > 0:
                        for res in regex:
                            self.final_result[str(each_url)].append(res) 
            self.output()
        else:
            print('unknown option.')
        
    def output(self):
        return self.final_result
