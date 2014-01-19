Plurk Robot
=
It's an easy program to create your own plurk robot.
Using RegExp to match the keywords in new plurks and then response proper messages.

Sample: [@waterme1on](http://plurk.com/waterme1on)

Requirement
-
Python 2.7.x


Usage
-
### Plurk OAuth keys
Add your OAuth keys(CONSUMER_KEY, CONSUMER_SECRET, TOKEN_KEY, TOKEN_SECRET) into **PlurkAPI.py**.
### Responses
Add your own responses mapping into **resp.json** in following format.
```
[
      r"keyword1", ["resp1-1", "resp1-2", ... , "resp1-n"],
      r"keyword2", ["resp2-1", "resp2-2", ... , "respn-n"],
      ...
      r"keywordN", ["respN-1", "respN-2", ... , "respN-n"]
]
```
The first string is the keyword you want to match, which used regular expression. 
The following is a list holding the responses correspond to the keyword. 
If matched, the program will randomly pick up one response in the list.
### Execution
```python PlurkBot.py```


References
-
* [Plurk API 2.0](http://www.plurk.com/API/)
* [Plurk's Blog (Chinese)](http://zh.blog.plurk.com/archives/1121)
