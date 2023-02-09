import requests
import sqlite3


def insert_db(offer):
    with sqlite3.connect('../db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO main_productmodel
            VALUES (NULL, :sku, :title, :category, :category_productAmount, :discount_price, :full_price, :availability, 
            :orders, :product_rating, :seller_id, :seller_title, :seller_link, 
            :seller_description, :seller_registrationDate, :seller_rating, :seller_reviews, 
            :seller_orders)
        """, offer)
        # REMOVED ( :product_tags, photos_collection, :seller_contacts  )
        connection.commit()  # чтоб данный записались в ДБ


# def insert_db():
#     with sqlite3.connect('../uzum.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute("""
#             CREATE TABLE offers (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 sku TEXT,
#                 name TEXT,
#                 category TEXT,
#                 discount_price INTEGER,
#                 full_price INTEGER,
#                 availability INTEGER,
#                 orders INTEGER
#             )
#         """)
#         connection.commit()  # чтоб данный записались в ДБ


# def update_available():
#     quantity = 0
#     with sqlite3.connect('uzum.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute("""
#         UPDATE offers
#         SET availability = NULL
#         """)
#         cursor.execute("""
#             SELECT id, sku
#             FROM offers
#             WHERE name not null
#         """)
#         result = cursor.fetchall()
#
#
#         for row in result:
#             row_id, sku = row
#
#             quantity = get_available(sku)
#
#             cursor.execute("""
#                 UPDATE offers
#                 SET availability = (?)
#                 WHERE id = (?)
#             """, (quantity, row_id))
#             connection.commit()
#             print(row_id, quantity)
#


# def get_available(quantity):
#     quantity = 0
#     start = 1
#     response = requests.get(f'https://api.umarket.uz/api/v2/product/{start}')
#     result = response.json()
#     try:
#         quantity = result['payload']['data']['skuList']['availableAmount']
#     except TypeError:
#         quantity = None


def get_product(result):
    if result['payload'] == None:
        print('if  working')
        offer = {
            'sku': None,
            'title': None,
            'category': None,
            'category_productAmount': None,
            'discount_price': None,
            'full_price': None,
            'availability': None,
            'orders': None,
            'product_rating': None,
            # 'product_tags': None,
            'seller_id': None,
            'seller_title': None,
            'seller_link': None,
            'seller_description': None,
            'seller_registrationDate': None,
            'seller_rating': None,
            'seller_reviews': None,
            'seller_orders': None,
            # 'seller_contacts': None,

        }
        insert_db(offer)

    else:
        items = result['payload']['data']
        # print(items['category']['title'])

        #  GET ALL IMAGES ON LIST

        photos = items['photos']
        photos_collection_list = []
        for photo in photos:
            x = photo['photo']['800']['high']
            photos_collection_list.append(x)

        #  GET ALL IMAGES ON LIST ENDS

        offer = {
            'sku': items['id'],
            'title': items['title'],
            'category': items['category']['title'],
            'category_productAmount': items['category']['productAmount'],
            'discount_price': items['skuList'][0]['purchasePrice'],
            'full_price': items['skuList'][0]['fullPrice'],
            'availability': items['skuList'][0]['availableAmount'],
            'orders': items['ordersAmount'],

            # 'photos_collection': photos_collection_list,
            'product_rating': items['rating'],
            # 'product_tags': items['tags'],

            # SELLER

            'seller_id': items['seller']['id'],
            'seller_title': items['seller']['title'],
            'seller_link': items['seller']['link'],
            'seller_description': items['seller']['description'],
            'seller_registrationDate': items['seller']['registrationDate'],
            'seller_rating': items['seller']['rating'],
            'seller_reviews': items['seller']['reviews'],
            'seller_orders': items['seller']['orders'],
            # 'seller_contacts': items['seller']['contacts'],

        }
        #

        print(offer)

        insert_db(offer)


def get_products():
    start = 1

    while True:
        url = f'https://api.umarket.uz/api/v2/product/{start}'  # from 35 till 60076

        response = requests.get(url=url)
        result = response.json()

        # if len(result['payload']['data']) == 0:
        #     pass
        get_product(result)
        start += 1
        print(url)


def main():
    get_products()
    # update_available()
    # insert_db()


if __name__ == '__main__':
    main()

######## CREATE TABLE ############


# def insert_db():
#     with sqlite3.connect('uzum.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute("""
#             CREATE TABLE offers (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 sku TEXT,
#                 name TEXT,
#                 category TEXT,
#                 discount_price INTEGER,
#                 full_price INTEGER,
#                 availability INTEGER,
#                 orders INTEGER
#             )
#         """)


#######################


# offer = {
#     'sku': None,
#     'title': None,
#     'category': None,
#     'discount_price': None,
#     'full_price': None,
#     'availability': None,
# }
# insert_db(offer)


############################
