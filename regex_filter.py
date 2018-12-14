import requests,json,re
from collections import defaultdict
from collections import Counter
import queue,threading
import pytoml as toml

class RegexFilter:
    THREAD_NUM = 5
    def __init__(self,inputfile,ftype,tom_file,outputdir):
        self.inputfile = inputfile
        self.outputdir = outputdir
        self.ftype = ftype
        self.final_result = defaultdict(list)
        self.final_output = {}
        self.q = queue.Queue()
        self.threads = []
        self.regexdict = {}
        
        with open(tom_file, 'rb') as fin:
            obj = toml.load(fin)
        for each_iter in range(len(obj['regexes'])):
             description = (obj['regexes'][each_iter]['description'])
             pattern = (obj['regexes'][each_iter]['regex'])
             self.regexdict[description] = pattern
        
        if self.ftype == 'offline' and isinstance(self.inputfile,dict):
            for each_url,each_file in self.inputfile.items():
                # each_file = each_file.strip('\r\n')
                # print(each_)
                fopen = open(str(self.outputdir)+str(each_file),encoding="utf8")
                fread = fopen.read().strip('\r\n')
                for description,pattern in self.regexdict.items():
                    pattern =  r"{}".format(pattern)
                    regex = re.compile(pattern).findall(fread)
                    if len(regex) > 0:
                        for res in regex:
                            self.final_result[str(each_url)].append(description)
                fopen.close()
                            
        elif self.ftype == 'online':
            for each_url in self.inputfile:
                self.q.put(each_url)
            for j in range(RegexFilter.THREAD_NUM): 
                t = threading.Thread(target=self.ProcessQueue)
                self.threads.append(t)
                t.start()
                
    def ProcessQueue(self):
        while not self.q.empty():
            each_url = self.q.get()
            self.Online_Regexer(each_url)
            self.q.task_done()
                
               
    def Online_Regexer(self,each_url):
        req = requests.get(each_url)
        for description,pattern in self.regexdict.items():
            pattern =  r"{}".format(pattern)
            regex = re.compile(pattern).findall(req.text)
            if len(regex) > 0:
                for res in regex:
                    self.final_result[str(each_url)].append(description) 
        
    def output(self):
        for t in self.threads:
            t.join()
        for each_url,each_res in self.final_result.items():
            pattern_match_count = dict(Counter(each_res))
            self.final_output[each_url] = pattern_match_count
        return self.final_output
