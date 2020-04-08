
import webbrowser


# http://ouo.io/s/y0d65LCP?s=https%3A%2F%2Fmega.nz%2F%23%21n7Bz2QbB%21gT7nZcJVfOQYb7k00vOzALkV5WV9JOgFhLWMc7geCaE
# https://mega.nz/#!n7Bz2QbB!gT7nZcJVfOQYb7k00vOzALkV5WV9JOgFhLWMc7geCaE

# Zippyshare
# http://ouo.io/s/y0d65LCP?s=https%3A%2F%2Fwww29.zippyshare.com%2Fv%2FsZZG3dcs%2Ffile.html
# http://ouo.io/s/y0d65LCP?s=https%3A%2F%2Fwww94.zippyshare.com%2Fv%2Fsqe4AxWa%2Ffile.html
# http://ouo.io/s/y0d65LCP?s=http%3A%2F%2Fwww3.zippyshare.com%2Fv%2FBkIi3Leu%2Ffile.html
# 

a = "http://ouo.io/s/y0d65LCP?s=https%3A%2F%2Fmega.nz%2F%23%21n7Bz2QbB%21gT7nZcJVfOQYb7k00vOzALkV5WV9JOgFhLWMc7geCaE"
b = "https://mega.nz/#!n7Bz2QbB!gT7nZcJVfOQYb7k00vOzALkV5WV9JOgFhLWMc7geCaE"


#### url = 'http://docs.python.org/'


# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

def zippyparse(link):
    ind = link.index("%3A%2F%2Fwww")
    c = link[ind+9:]    
    if c[0] == "F":
    	c = c[1:]
    if c[0] == "F":
    	c = c[1:]
    if c[0] == "F":
    	c = c[1:]
    b = ""
    l = len(c)
    x = 0
    while(x<l):
        if c[x] == "%":
            x+=3
            b+="/"
        b+=c[x]
        x+=1
    return b

def megaparse(link):
    mega1 = "https://mega.nz/#!"
    i = 0
    while (link[i:i+7] != "mega.nz"):
        i+=1
    i += 16
    print(link[i:])
    m2 = (link[i:])
    m3 = ""
    for i in range(len(m2)):
        if m2[i] == "%":
            m3 = "!"+m2[i+3:]
            m2 = m2[:i]
            break
    return mega1+m2+m3




def openlink(url):	
	print (url)
	webbrowser.get(chrome_path).open(url)


def main():
	input_data = ""
	while (input_data != "-1"):
		input_data = input()		
		url = ""
		if ("zippyshare" in input_data):
			url = zippyparse(input_data)
		if ("mega.nz" in input_data):
			url = megaparse(input_data)
		openlink(url)
		#input_data = "-1"



main()
    
#print("real",b)
#print("test",mega1+m2+m3)
