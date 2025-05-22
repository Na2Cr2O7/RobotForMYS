import requests
from bs4 import BeautifulSoup
import hashlib
import pickle
import os
from random import choice
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"}
namelist=[]
urllist=[]



if os.path.exists('urllist.pkl'):
    with open('urllist.pkl','rb') as f:
        urllist=pickle.load(f)

def get(url):

    global namelist
    
    u=requests.get('https://www.vilipix.com'+url,headers=head,verify=False)
    html=BeautifulSoup(u.text,'html.parser')
    _=html.find_all('a')
    pageurls=[]
    src=''
    for i in _:
        try:
            if 'logo' not in i.img['src']:
                src=i.img['src']
                lo=requests.get(src,headers=head,verify=False)
                f=html.title.get_text().replace(' ','').replace('-插画世界','')
                f=hashlib.md5(f.encode('utf-8')).hexdigest()
                p=open(f+'.png','wb')
                p.write(lo.content)
                p.close()
                return f+'.png'

        except:
            pass


def fetch(text=-1):
    global urllist
    if text==-1:
        with open('search.txt','r',encoding='utf-8') as f:
            textlist=f.read().split('\n')
        text=choice(textlist)
    print('🛜',text)
    for pages in range(1,10):
        s=requests.get('https://www.vilipix.com/'+'tags/'+text+'/illusts?p='+str(pages),headers=head,verify=False)
        html=BeautifulSoup(s.content,'html.parser')
        G=html.find_all('a')
        for each in G:
                
                try:
                    l=each['href']
                    if 'illust' in l:
                        if 'tags' in l:
                            pass
                        elif l not in urllist:
                            urllist.append(l)
                            with open('urllist.pkl','wb') as f:
                                pickle.dump(urllist,f)
                            print(l)
                            return [text,get(l)]
                except:
                    pass


if __name__=='__main__':
    #fetch('日系')
    imageLs=fetch()
    print(imageLs)