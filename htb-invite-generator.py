from subprocess import PIPE, run;import json;import base64;c="curl -XPOST https://www.hackthebox.eu/api/invite/generate -s";g=run(c,stdout=PIPE,stderr=PIPE,universal_newlines=True,shell=True);l=json.loads(g.stdout);cd=base64.b64decode(l['data']['code']);print(f"Your HackTheBox invite is {str(cd, 'utf-8')}")
