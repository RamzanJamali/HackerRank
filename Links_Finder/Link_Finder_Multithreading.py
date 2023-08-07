from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from threading import Thread, Lock
import time
from urllib.parse import urlsplit



#service = Service(executable_path=r"C:/Program Files/Google/Chrome/Application/chromedriver")
service = Service(executable_path=r'./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

# To make pages load faster by excluding some resources.
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.xhr': 2,
                                                 'profile.managed_default_content_settings.preflight': 2,
                                                 'profile.managed_default_content_settings.images': 2,
                                                'profile.managed_default_content_settings.font': 2,
                                                'profile.managed_default_content_settings.css': 2})




def enter_url():
    url = input('Enter URL: ')

    # URL validation
    if not url.startswith("https"):
        url = 'https://' + url
    elif not url.startswith("http"):
        url = 'http://' + url
    else:
        pass
    
    return url



url = enter_url()

def base_url(url):
    parts = urlsplit(url)
    base = '{0.netloc}'.format(parts)
    temp = base.split('.')
    remove_this = temp[0] + '.'
    base = base.replace(remove_this, '')
    
    return base

domain_url = base_url(url)
print(domain_url)
links_to_scrape = {}
links_to_scrape[url] = url
scraped_links = []
all_links = {}
lock = Lock()




def link_finder(url):
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url)

        # Give the required tag and/or class, etc.
        elems = driver.find_elements(By.TAG_NAME, "a")
        global links_found
        links_found = []
        # Save the scraped links in list
        for elem in elems:
            link = elem.get_attribute("href")
            links_found.append(link)

    except:
        pass
        
    driver.quit()




def links_manager(links_found, scraped_links, links_to_scrape, url):
    
    for link in links_found:
        all_links[link] = 1
        link_base = base_url(link)
        if domain_url == link_base:
            if link in scraped_links:
                pass
            else:
                links_to_scrape[link] = link


    


#link_finder(links_to_scrape[0])
#N = 1   # Number of browsers to spawn
thread_list = list()
link_finder(links_to_scrape[url])
# Start test
remaining_links = len(links_to_scrape)
i = 0
while remaining_links > 0:
    try:
        with lock:
            url = next(iter(links_to_scrape))
            scraped_links.append(url)
            del links_to_scrape[url]
    
        if url == None: 
            break

        t = Thread(name='Test {}'.format(i), target=link_finder, args=(url,))
        with lock:    
            links_manager(links_found, scraped_links, links_to_scrape, url)
        t.start()
        print(t.name + ' started!')
        thread_list.append(t)
        i += 1

    except:
        pass

    remaining_links = len(links_to_scrape)
    
# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')




print(len(all_links))
print(len(links_to_scrape))
print(len(scraped_links))