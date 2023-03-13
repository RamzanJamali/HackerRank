import webbrowser
new = 5
url = "http://docs.python.org/library/webbrowser.html"
webbrowser.get(using='/usr/bin/google-chrome %s').open_new_tab(url) 
print('done')
