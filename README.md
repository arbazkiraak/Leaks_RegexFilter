# Regex-Filter

<b>STATUS : DEVELOPING</b>

Use Case 1: `online`

```python

X = RegexFilter(['https://github.com/hackerarbaz/Tryme/blob/master/creds.py','http://anysite.com/'],'online',{'CSE':'.+\.xml','PASS':'PASSWORD'})
XX = X.output()
XX.items()
```

Use Case 2: `offline`

```python

X = RegexFilter({r'/kiraakboi/cralwed/woot/1.raw':'1'},'offline',{'CSE':'.+\.txt','PASS':'checking '})
XX = X.output()
XX.items()

```

Output Rendering :

```python
from collections import Counter
res = {}
for each_url,each_res in XX.items():
    pattern_match_count = dict(Counter(each_res))
    res[each_url] = pattern_match_count
```
out:
````
{'https://github.com/realchief/Node.js_Ecommerce/blob/c917f1aaeeb42a83677ef18fa036843ea603b85e/environment.json': {'PASS': 213}}
````

<i>`Random helper`</i>


```python
regexdict = {}
import pytoml as toml
with open('file.toml', 'rb') as fin:
    obj = toml.load(fin)
for each_iter in range(len(obj['regexes'])):
     description = (obj['regexes'][each_iter]['description'])
     pattern = (obj['regexes'][each_iter]['regex'])
     print(description,':',pattern)
     regexdict[description] = pattern
    
print(regexdict)
```
