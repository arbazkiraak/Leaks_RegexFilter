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

<i>`Random helper`</i>
