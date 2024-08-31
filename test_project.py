import project
import pytest
import warnings
import os


def test_translation():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        warnings.filterwarnings("ignore", category=DeprecationWarning, module="cgi")
        #Test tradcution. Spanish -> English
        assert project.translation(["Zaatos","Rojos"]) == "Red shoes"
        #Test tradcution. Turkish -> English
        assert project.translation(["Kulaklıklar"]) == "Headphones"
        #Test tradcution. Chinese -> English
        assert project.translation(["阿瓜"]) != "Choche"
        #Test the type of data input
        with pytest.raises(TypeError):
            assert project.translation(10)

def test_amazon_search_page():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        warnings.filterwarnings("ignore", category=DeprecationWarning, module="cgi")
        product_list = project.amazon_search_page("headphones",10)
        #Check that the list is not empty
        assert len(product_list) > 0
        #Check the amount of products to look for 
        assert len(product_list) == 10
        
        #Check the type of elements in the list
        for product in product_list:
            assert isinstance(product,dict)
            assert "title" in product
            assert "price" in product
            assert "url"   in product
        
        #Checke the prices have a correct value and format
        for product in product_list:
            assert isinstance(product["price"],(int,float)) and product["price"] > 0

def test_name_analized():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        warnings.filterwarnings("ignore", category=DeprecationWarning, module="cgi")
        #List of item in the basket
        basket = ["Toy","Xbox","Playstation","Laptop"]
        #Check that the named item is not in the basket, and that the tittle of the product contains the item name
        assert project.name_analized("Raspberry","New amazing Raspberry kit",basket) == True
        #Check that the product tittle contains the name introduced by the user
        assert project.name_analized("puzzle","New amazing Console",basket) == False
        #Check that the product already exists in the basket of products
        assert project.name_analized("Xbox one","New amazing Xbox",basket) == False

def test_amazon_list():
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")
			#Create a list of products to test
			product_list =[
				{"title": "New amazing xbox one",
				"price": 250.5,
				"url"  : "http://amazon.uk/xboxone1"},
				{"title": "New amazing playstation",
				"price": 567.3,
				"url"  : "http://amazon.uk/playstation5"},
				{"title": "New amazing wii",
				"price": 300,
				"url"  : "http://amazon.uk/wii"}
			]
			result = project.amazon_list(product_list,False)
			#Check that the function returns nothing, and no problem occureded
			assert result is None
			#Check the new created file exists
			assert os.path.exists("amazon_products.csv")

     
    
    
    