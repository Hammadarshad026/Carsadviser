import requests
from bs4 import BeautifulSoup
brand='toyota'
car='corolla GLi 1.3 VVTi'
model=2016


def add_plus_separator(text):
    # Remove extra spaces and split into words
    words = text.strip().split()
    # Join with +
    return '+'.join(words)

def get_first_two_words(text):
    words = text.strip().split()
    return ' '.join(words[:2])
    

def imgLink_scrapper(brand,car,model):
    Car=get_first_two_words(car)
    Car_=add_plus_separator(Car)
    print("Car"      ,Car_)
    header={
                'User-Agent':'Mozilla/5.0'
            }
    url=f"https://www.pakwheels.com/used-cars/search/-/?q={brand}+{Car_}+{model}"
    re=requests.get(url,headers=header)
    Soup=BeautifulSoup(re.text,'html.parser')
    cars_profile_links=Soup.find('a',class_="car-name")
    car_profile_href=cars_profile_links.get('href')
    car_profile_link='https://www.pakwheels.com'+car_profile_href   #carprofile link
    car_profile_link_re=requests.get(car_profile_link,headers=header)
    re_soup=BeautifulSoup(car_profile_link_re.content,"html.parser")
    ul_tag=re_soup.find('ul',class_='gallery')
    img_tag=ul_tag.find('img')
    src=img_tag['src']
    
    return src




