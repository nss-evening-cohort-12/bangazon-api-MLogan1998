import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection


def inexpensive_products(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT p.id product_id, p.name product_name, p.price product_price
                FROM bangazonapi_product p
                WHERE p.price <= 999
            """)

            dataset = db_cursor.fetchall()

            inexpensive_list = {}

            for row in dataset:
                product_id = row["product_id"]
                name = row["product_name"]
                price = row["product_price"]

                inexpensive_list[product_id] = {}
                inexpensive_list[product_id]["id"] = product_id
                inexpensive_list[product_id]["name"] = name
                inexpensive_list[product_id]["price"] = price

        product_list = inexpensive_list.values()
        template = 'products/inexpensive_products.html'
        context = {
            'inexpensive_products': product_list
        }

        return render(request, template, context)
