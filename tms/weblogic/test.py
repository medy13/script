#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

Domains=["10.3.50.241:/root/tms01_domain/servers/server-tms01",
"10.3.50.249:/root/base_domain/servers/server-tms02",
"10.3.50.234:/root/base_domain/servers/server-tms03",
"10.3.50.231:/root/base_domain/servers/server-tms04",
"10.3.50.215:/root/base_domain/servers/server-tms05"
];
def usage():
	print "cp_file.py path/subpath/htmlname.html"
	sys.exit(0);

def rcp(ip,fullFileName):
	idx = fullFileName.rindex("/");
	filePath = fullFileName[:idx]+"/";
	cmdLine="scp webapp/"+fullFileName+" "+ip+"/stage/tms/tms/"+filePath
	print cmdLine;
	os.system(cmdLine);

def rcpClass(ip,fullFileName):
        idx = fullFileName.rindex("/");
        filePath = fullFileName[:idx]+"/";
	javaFile=fullFileName[:len(fullFileName)-5]+".class"
        cmdLine="scp webapp/WEB-INF/classes/"+javaFile+" "+ip+"/stage/tms/tms/WEB-INF/classes/"+filePath
        print cmdLine;
        os.system(cmdLine);
	javaFile2=fullFileName[:len(fullFileName)-5]+"\$*.class"
        cmdLine2="scp webapp/WEB-INF/classes/"+javaFile2+" "+ip+"/stage/tms/tms/WEB-INF/classes/"+filePath
        print cmdLine2;
        os.system(cmdLine2);
print sys.argv
if len(sys.argv)<2 or sys.argv[1] == "":
	usage();
curtFileName = sys.argv[1]
inx1=curtFileName.find(".");
if inx1 <=0:
	usage();
ldIdx=curtFileName.rindex(".");
fgs=curtFileName[ldIdx:]
if fgs == "":
	usage();
print "file_format:"+fgs
print sys.argv
for domain in Domains:
	if ".java" == fgs:
		rcpClass(domain,curtFileName);
	else:
		rcp(domain,curtFileName);
