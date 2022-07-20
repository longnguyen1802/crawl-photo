from bs4 import BeautifulSoup
import requests
import webbrowser

def getlistAlbums(offset):
    result = []
    html_text = requests.get('https://www.sportsoho.com/pg/photos/world/?offset='+str(offset*16)).text;
    soup = BeautifulSoup(html_text,'lxml')
    albums = soup.find_all("article")
    for album in albums:
        ALchildren = album.find_all('div',{ "class" : "portfolio-image" })
        for div in ALchildren:
            link = div.find_all('a')[0]
            if link['href']:
                result.append(link['href'])
    return result
def getListPhoto(url,offset):
    result = []
    html_text = requests.get(url+'?offset='+str(18*offset)).text;
    soup = BeautifulSoup(html_text,'lxml')
    albums = soup.find_all("article")
    for album in albums:
        ALchildren = album.find_all('div',{ "class" : "portfolio-image" })
        for div in ALchildren:
            link = div.find_all('a')[0]
            if link['href']:
                result.append(link['href'])
    return result
def getAlbumnPage(url):
    html_text = requests.get(url).text;
    soup = BeautifulSoup(html_text,'lxml')
    pag = soup.find_all("div",{"class":"pagination"})[0]
    result = pag.find_all('a',{"class":"pagination_number"})[-1]
    return int(result.contents[0])
    
def getImageUid(url):
    content = url.split('/')
    return content[6]
def download(url):
    uid = getImageUid(url)
    link = 'https://www.sportsoho.com/mod/sh_photos/downimage.php?file_guid='+str(uid)+'&size=original'
    webbrowser.open(link)

def downloadImageInPage(offset):
    listAlbumn = getlistAlbums(offset-1)
    for albumn in listAlbumn:
        numberPage = getAlbumnPage(albumn)
        for i in range(numberPage):
            listPhotos = getListPhoto(albumn,i)
            for photo in listPhotos:
                download(photo)

downloadImageInPage(1)
#print(getListPhoto('https://www.sportsoho.com/pg/photos/album/8820538/2022-',getAlbumnPage('https://www.sportsoho.com/pg/photos/album/8820538/2022-')-1))


#webbrowser.open('https://www.sportsoho.com/mod/sh_photos/downimage.php?file_guid=8817763&size=large')
#html_text = requests.get('https://www.sportsoho.com/pg/photos/view/8814364').text
#soup = BeautifulSoup(html_text,'lxml');
#divs = soup.find("div", {"id": "image_loading"})

#children = divs.findChildren("a" , recursive=False)
#print(children[0]['href'])
#html_text_out = requests.get('https://www.sportsoho.com/pg/photos/world/?offset=0').text
#soup_out = BeautifulSoup(html_text_out,'lxml')
#albums = soup_out.find_all("article")
#for album in albums:
#    ALchildren = album.find_all('div',{ "class" : "portfolio-image" })
#    for div in ALchildren:
#        link = div.find_all('a')[0]
#        if link['href']:
#            html_text_in = requests.get(link['href']).text
#            soup_in = BeautifulSoup(html_text_in,'lxml')
#            photos = soup_in.find_all("article")
#            for photo in photos:
#                PHchildren = photo.find_all('div',{ "class" : "portfolio-image" })
#                for div in PHchildren:
#                    link = div.find_all('a')[0]
#                    if link['href']:
#                        print(link['href'])
#                        'https://www.sportsoho.com/mod/sh_photos/downimage.php?file_guid="+data.guid+"&size=original'

        
        