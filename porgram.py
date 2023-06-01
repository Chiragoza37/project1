import click
import requests
import json

@click.command()
@click.argument('book_name')
def search_book(book_name):
    try:
        params={"title":book_name}
        response = requests.get('https://openlibrary.org/search.json',params=params)
    except (TypeError, requests.exceptions.ConnectionError):
        pass
    if response.status_code == 200:
        results = response.json()
        for result in results['docs']:
             title =f"Title: {result['title']}"
             author = f"Author: {result['author_name']}" 
             print(title, "\n" , author)
    else:
        print("Error in code")

search_book()
