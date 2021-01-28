from subprocess import PIPE, run;import json;import base64
def request(command):
    codegen = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True);return codegen.stdout
loadit=json.loads(request("curl -XPOST https://www.hackthebox.eu/api/invite/generate -s"));code=base64.b64decode(loadit['data']['code']);print(f"Your HackTheBox invite is {str(code, 'utf-8')}")
