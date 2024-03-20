'''
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Name : lab9_exe_C
Assignment : Lab 9 Exercise C
Author ( s ) : César García , Wassim Belghache
Submission : March 20 , 2024
Description : Interacting with JSON Data in Python
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
'''

import requests
import json

def fetch_product_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()['products']
    except requests.exceptions.Timeout:
        print("Error: The request timed out")
    except requests.exceptions.TooManyRedirects:
        print("Error: Too many redirects")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    return None

def list_all_products(products):
    for product in products:
        print(product['title'])                         #iterate through products to get all of them
        print('\n')

def search_product(products, name):
    found = False
    for product in products:
        if product['title'].lower() == name.lower():   #Capitalization does not affect search
            found = True 
            print(f"Product Details for '{name}':")
            print(json.dumps(product, indent=4))
            print('\n')
    if not found:
        print("Product not found.")                     #if name of products is not found print message


def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n> ")

            if choice == '1':
                list_all_products(products)
            elif choice == '2':
                product_name = input("Enter the product name: ")
                search_product(products, product_name)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")


if __name__ == "__main__":
    main()
