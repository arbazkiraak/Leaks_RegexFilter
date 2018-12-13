import requests,json,re
from collections import defaultdict
class RegexFilter:
    def __init__(self,inputfile,ftype,regexdict):
        self.inputfile = inputfile
        self.regexdict = regexdict
        self.ftype = ftype
        self.final_result = defaultdict(list)
        
        if self.ftype == 'offline' and isinstance(self.inputfile,dict):
            for each_file,each_url in self.inputfile.items():
                each_file = each_file.strip('\r\n')
                fopen = open(each_file,encoding="utf8")
                fread = fopen.read().strip('\r\n')
                for description,pattern in regexdict.items():
                    pattern =  r"{}".format(pattern)
                    regex = re.compile(pattern).findall(fread)
                    if len(regex) > 0:
                        for res in regex:
                            self.final_result[str(each_url)].append(description)
                fopen.close()
                            
        elif self.ftype == 'online':
            for each_url in self.inputfile:
                req = requests.get(each_url)
                for description,pattern in regexdict.items():
                    pattern =  r"{}".format(pattern)
                    regex = re.compile(pattern).findall(req.text)
                    if len(regex) > 0:
                        for res in regex:
                            self.final_result[str(each_url)].append(description) 
            self.output()
        else:
            exit("wrong option buddy!")
        
    def output(self):
        return self.final_result
