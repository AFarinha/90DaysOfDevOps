#!/usr/bin/env python3
"""Create a random disposable lab Secret through stdin, without printing values."""
import argparse,json,secrets,subprocess
parser=argparse.ArgumentParser()
parser.add_argument("namespace")
args=parser.parse_args()
name='mysql-credentials'
found=subprocess.run(["kubectl","get","secret",name,"-n",args.namespace],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
if found.returncode==0:
    print("Existing Secret preserved:",name)
else:
    password=secrets.token_urlsafe(24)
    data={'mysql-root-password': password, 'mysql-password': password, 'mysql-replication-password': password}
    obj={"apiVersion":"v1","kind":"Secret","metadata":{"name":name,"namespace":args.namespace},"stringData":data}
    subprocess.run(["kubectl","create","-f","-"],input=json.dumps(obj),text=True,check=True)
