# Regex-Filter

> Are you fan of https://github.com/zricethezav/gitleaks ? <br>
Want to use it anywhere besides github? <br>
<i> TOML format : `https://github.com/zricethezav/gitleaks/blob/master/gitleaks.toml` </i>

```python
            all_paths = {'url':'file','url2','file2'}
            toml_file = '/dir/reg.toml'
            PAGE_OUTPUT_DIR = '/dir/output/'
            X = RegexFilter(all_paths,'offline',toml_file,PAGE_OUTPUT_DIR)
            print(X.output())
```

<hr><hr><hr>

`all_paths` : LIST OF URLS/LOCAL FILES <br>
`offline` or `online` : OFFLINE FOR LOCAL FILES | ONLINE FOR LIST OF URLS <br>
`toml_file` : PATH FOR TOML FILE <br>

Use Case 1: `online`

```python

X = RegexFilter(['https://github.com/hackerarbaz/Tryme/blob/master/creds.py','http://anysite.com/'],'online','/woot/gitleaks.toml')
XX = X.output()
XX.items()
```

Use Case 2: `offline`

```python

X = RegexFilter({r'/kiraakboi/cralwed/woot/1.raw':'1'},'offline',{'CSE':'.+\.txt','/woot/gitleaks.toml','/path/to/output/dir/to/store/results')
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

<i>`Verifying`</i>

`
$ printf 'http://username:password@example.com/sagsagasggsaasggggg' | grep -P "[a-zA-Z]{3,10}://[^/\s:@]{3,20}:[^/\s:@]{3,20}@.{1,100}"
`
