from django.shortcuts import render
import requests
from requests.compat import quote_plus
from.import models
from bs4 import BeautifulSoup
BASE_CRAIGSLIST_URL='https://kerala.craigslist.org/d/housing/search/hhh?query={}'
BASE_IMAGE_URL="https://images.craigslist.org/{}_300x300.jpg"

# Create your views here.
def home(request):
    return render(request,'base.html')
def new_search(request):
    search=request.POST.get('search')
    models.Search.objects.create(search=search)             #object creation takes place here and also the searched things are upddated on the datebase
    final_url=BASE_CRAIGSLIST_URL.format(quote_plus(search))
    #print(final_url)
    response=requests.get(final_url)
    data=response.text
    soup=BeautifulSoup(data,features='html.parser')
    post_listings=soup.find_all('li',{'class':'result-row'})


    final_postings=[]
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if  post.find(class_='result-price'):           # it means that the it exits and it is not none
            post_price =post.find(class_='result-price').text
        else:
            post_price='N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id=post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            print(post_image_id)
            post_image_url=BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
           post_image_url= 'https://craigslist.org/images/peace.jpg'


        final_postings.append((post_titles,post_url,post_price,post_image_url))






   # print(post_url)
    #print(post_price)
  #  print(post_titles[0].get('href'))
    #print(data)

    stuff_for_frontend={
        'search':search,
        'final_postings':final_postings,
    }
    return render(request,'my_app/new_search.html',stuff_for_frontend)