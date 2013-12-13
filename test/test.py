import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import pprint
import json

import hasher

with open("tests.json","rb") as tf:
    tests = json.load(tf)

    for t in tests:
        pprint.pprint([t["data"],t["options"]])
        try:
	        assert hasher.hash("md5",t["data"],**t["options"]) == t["md5sum"]
	        assert hasher.hash("sha1",t["data"],**t["options"]) == t["sha1sum"]
	        assert hasher.hash("sha256",t["data"],**t["options"]) == t["sha256sum"]
	        assert hasher.hash("sha512",t["data"],**t["options"]) == t["sha512sum"]
        except:
	        print json.dumps({ 
	        	"md5sum": hasher.hash("md5",t["data"],**t["options"]),
	        	"sha1sum": hasher.hash("sha1",t["data"],**t["options"]),
	        	"sha256sum": hasher.hash("sha256",t["data"],**t["options"]),
	        	"sha512sum": hasher.hash("sha512",t["data"],**t["options"])
	        },indent = 4)