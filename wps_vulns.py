import requests

def website(name):
    url = name
    global list
    list = []
   
    target = ("https://"+url)
    
    a = requests.get("https://"+url+"/xmlrpc.php")
    if a.status_code==405:
        list.append("[!] xmlrpc.php file is enabled")
    else:
        list.append("[!] xmlrpc.php file is disabled")


    b = requests.get("https://"+url+"/wp-json/")
    if b.status_code==200:
        list.append("[!] wp-json file is enabled")
    else:
        list.append("[!] wp-json file is disabled")

    c = requests.get("https://"+url+"/admin")
    if c.status_code==200:
            list.append("[!] Admin pannel is enabled")
    else:
        list.append("[!] Admin pannel is disabled")

    d = requests.get("https://"+url+"/robots.txt")
    if d.status_code==200:
        list.append("[!] Robots.txt file is enabled")
    else:
        list.append("[!] Robots.txt is disabled")

    e = requests.get("https://"+url+"/wp-content/uploads")
    if e.status_code==200:
      list.append("[!] Direcotry travelsal  is enabled")
    else:
        list.append("[!] Direcotry travelsal is disabled")

    l = requests.get("https://"+url+"/sitemap.xml")
    if l.status_code==200:
        list.append("[!] Sitemap.xml file is enabled")
    else:
        list.append("[!] Sitemap.xml file is disabled")

    f = requests.get("https://"+url+"/.htaccess")
    if f.status_code==200:
        list.append("[!] .htaccess file is enabled")
    else:
        list.append("[!] .htaccess file is disabled")

    g = requests.get("https://"+url+"/.gitignore")
    if g.status_code==200:
        list.append("[!] .gitignore file is enabled")
    else:
        list.append("[!] .gitignore file is disabled")

    h = requests.get("https://"+url+"/.log")
    if h.status_code==200:
        list.append("[!] .log file is enabled")
    else:
        list.append("[!] .log file is disabled")

    i = requests.get(target+"/license.txt")
    if i.status_code==200:
        list.append("[!] license.txt file is enabled")
    else:
        list.append("[!] license.txt file is disabled")
    j = requests.get(target+"/wp-config.php")
    if j.status_code==200:
       list.append("[!] wp-config.php file is enabled")
    else:
       list.append("[!] wp-config.php file is disabled")

    k = requests.get(target+"/readme.html")
    if k.status_code==200:
       list.append("[!] readme.html file is enabled")
    else:
        list.append("[!] readme.html file is disabled")

    z = requests.get(target)
    header = z.headers
    if "X-Frame-Options" in header:
        list.append("Site is not vulnerable to clickjacking")
    else:
        list.append("Site is vulnerable to clickjacking")

    return list



def run_program(url):
    wpssite=url
    return website(wpssite)

    