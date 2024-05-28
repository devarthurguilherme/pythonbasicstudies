import requests
import beaupy


def fillListProducts():
    # Devolver 20 produtos ordenados por preço descendente
    endpoint = "https://dummyjson.com/products"
    parameters = {
        'sortBy': 'price',
        'order': 'desc',
        'limit': 0,
        'select': 'id,title,price,rating,category'
    }
    response = requests.get(url=endpoint, params=parameters)
    return response.json()['products']


def printAllComments(listReviews):
    print("\nListagem de Reviews\n")
    for review in listReviews:
        print(f"""
            {review['date'][:10]} - {review['comment']} ({review['rating']}/5)
            by {review['reviewerName']}
            """)


def showProductComments(product):
    endpoint = f"https://dummyjson.com/products/{product['id']}"
    response = requests.get(url=endpoint)
    listComments = response.json()["reviews"]
    printAllComments(listComments)


def showProducts(listProducts):
    # Selecionar um produto dessa listagem (beaupy) e ver comentários desse produto
    print("\nIndique o produto desejado: \n")
    listProductsBeaupy = [product['title'] for product in listProducts]
    op = beaupy.select(listProductsBeaupy, cursor='->',
                       cursor_style='white', return_index=True)
    showProductComments(listProducts[op])


def getAllCategories():
    endpoint = 'https://dummyjson.com/products/categories'
    response = requests.get(url=endpoint)
    return response.json()


def getProductsFromCategory(slug, listProducts):
    return [product for product in listProducts if product["category"].lower() == slug]


def printAllProductsCategory(listProductsCategory):
    if listProductsCategory:
        for product in listProductsCategory:
            print(
                f"{product['title']} ({product['rating']}/5)\nPVP: {product['price']}€ Categoria: {product['category']}\n")
    else:
        print("\nNão foram encontrados produtos da categoria definida.\n")


def getProductsFromCategories(listCategories, listProducts):
    print("\nCategorias\n")
    for category in listCategories[:3]:
        print(f"{category['name']}\n")
        listProductsCategory = getProductsFromCategory(
            category['slug'], listProducts)
        printAllProductsCategory(listProductsCategory)
        print("*" * 100)


# globals
listProducts = fillListProducts()
# showProducts(listProducts)
# Ver 10 produtos de cada categoria
listCategories = getAllCategories()
getProductsFromCategories(listCategories, listProducts)
