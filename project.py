##----------------- Amazon Product Scraper ----------------------
import argparse 
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys
import csv
import cowsay
import pyttsx3
from googletrans import Translator
import time

def main():
    try:
        parser = argparse.ArgumentParser(description="Amazon product finder")
        parser.add_argument("-i",default=False, nargs='+', help="Item to look for", type= str)
        parser.add_argument("-n",default=1, help="Number of item to sear", type= int)
        parser.add_argument("-p",default=False,help="Print the item information",type = bool)
        args = parser.parse_args()
        if args.i == False:
            raise ValueError
        
    except ValueError:
        sys.exit("No item name has been instroduced.\nPlease introduce a valid name")
        
    else:
        item = translation(args.i)
        product = amazon_search_page (item,args.n)
        amazon_list(product,args.p)
        
def translation(word:list, target_lenguage: str = 'en') -> str:
    try:
        #Convert the list of args into a string
        word_str = ' '.join(word).strip()
        #Create an object for translation into english
        translator = Translator()
        #Translate the string. This returns a class
        translated_text = translator.translate(word_str,dest=target_lenguage) 
        #Return only the translated text of the class
    except TypeError:
        raise TypeError("Invalid argument type. Expected list of words.")
    else:
        return translated_text.text
    
def amazon_search_page(name:list,quantity:int)-> list:
    #Confiture Selenium
    options = Options()
    options.add_experimental_option("detach", True)
    
    #Stablish User-Agent. Headers for the HTTP requests.
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    #Don't show the browser window
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    #Amazon URL
    page = 1  
    url = "https://www.amazon.co.uk/s?k="+name+"&page="+str(page)
    #Open the browser with the url formed
    driver.get(url)
    #Give time to load the page
    time.sleep(2)
    
    #Wait until the webpage is fully loaded
    driver.implicitly_wait(2)
    
    #Get HTML of the webpage after it loads
    html = driver.page_source
    
    #Create an object BeautifulSoup to analize HTML
    soup = BeautifulSoup(html,"html.parser")
    
    #Find all the elements of products on the page
    product_elements = soup.find_all('div',class_='s-result-item')
    
    #Find the maximun page in the web browser
    total_pages_element = soup.find('span',{'class': 's-pagination-item s-pagination-disabled'})

    #Save the value of Max pages in a variable
    total_pages = int(total_pages_element.text.strip())
   
    #List of names of products to avoid repetitions
    names_in_the_basket = []
    
    #List to return with the info
    basket = []
    
    #Page to start the scraping
    page = 1
    
    while len(basket) < quantity and page <= total_pages:
        
        #Variable to determine to save or not information
        exists_name = False
        exists_price = False
        exists_url = False
        
        #Iterate on the elements to extract the data
        for product in product_elements:
            #Check for an element
            title_element = product.find('h2',class_ = 'a-size-mini')
            if title_element:
                #Save the product's name in a variable.
                title = title_element.text.strip()
                #Use a function to verify the product is not repeated in the basket, and that it contains the words of the "name"
                exists_name = name_analized(name, title,names_in_the_basket)
                
            #Check for the price
            price_element = product.find('span',class_='a-price')
            if price_element:
                exists_price = True
                price = float("{:.2f}".format(float(price_element.find('span',class_='a-offscreen').text.strip().replace("£","").replace(",",""))))
            # Check for the url    
            url_element = product.find('a', class_='a-link-normal', href=True)
            if url_element:
                exists_url = True
                url = 'https://www.amazon.co.uk' + url_element['href']
                
                
            #To save the info, the item must have all thre information
            if exists_name and exists_price and exists_url:
                basket.append({"title":title,"price":price,"url":url})
                names_in_the_basket.append(title)

            
            exists_name,exists_price,exists_url = False,False,False
        
        #print(f"Searched in page {page} and have {len(basket)} results")
        
        #If the list is bigger than the quantity requiered, stop the search    
        if len(basket) >= quantity:
            break
        #If the list is smaller thant the requiered, click enxt page
        page +=1
        
        
        url = "https://www.amazon.co.uk/s?k="+name+"&page="+str(page)
        driver.get(url)
        
        #Wait until the webpage is fully loaded
        driver.implicitly_wait(1)
        
        #Get HTML of the webpage after it loads
        html = driver.page_source
        
        #Create an object BeautifulSoup to analize HTML
        soup = BeautifulSoup(html,"html.parser")
        
        #Find all the elements of products on the page
        product_elements = soup.find_all('div',class_='s-result-item')

    #Close the chorme window            
    driver.quit()
    #Return the list with all the products
    if len(basket) >= quantity:
        return basket[:quantity]
    else: 
        return basket
        
def name_analized(name:str, title:str,names_in_the_basket:list)->bool:
    
    name_words = name.lower().split()
    title_words = title.lower().split()
    if not title in names_in_the_basket:
        if all(word in title_words for word in name_words):
            return True
    return False

def amazon_list(basket:list,printable:bool) -> None:
    try:
        if printable:
            phrase = "Thanks for using this scrip. Here are the results"
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            #For my laptop, these are the voices available!
            spanish_mexico_Sabina = voices[0].id
            english_EUA_David = voices[1].id
            english_EUA_Zira = voices[2].id
            english_GB_Hazel = voices[3].id
            
            engine.setProperty('voice',english_GB_Hazel)

        
        with open("amazon_products.csv","w",newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames=["Name","Price","Link"])
            writer.writeheader()
            for item in sorted(basket , key = lambda s: s["price"]):
                writer.writerow({"Name":item["title"],"Price":item["price"],"Link":item["url"]})
                
    except PermissionError:
        cowsay.cow("problem detected")
        engine.say("problem detected")
        engine.runAndWait()
        sys.exit("System Error. Document already exists and is currently opended")
    except IndexError:
        sys.exit("Wrong set of voice reader")
    else:
        if printable:
            cowsay.cow(phrase)
            engine.setProperty('voice',english_GB_Hazel)
            engine.say(phrase)
            engine.runAndWait()
            for item in basket:
                print(f"Product name: {item['title']}")
                print(f"Product price: {item['price']}")
                print(f"Produce link: {item['url']}")
                print("-"*50)
                
if __name__ == "__main__":
    main()