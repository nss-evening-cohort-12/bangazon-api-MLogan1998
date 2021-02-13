import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection


def completed_orders(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT o.id order_id, p.merchant_name payment_type, SUM(pr.price) total_price, a.first_name || ' ' || a.last_name AS full_name
                FROM bangazonapi_order o
                JOIN bangazonapi_payment p 
                ON o.payment_type_id = p.id
                JOIN bangazonapi_orderproduct op
                ON o.id = op.order_id
                JOIN bangazonapi_product pr 
                ON op.product_id = pr.id
                JOIN bangazonapi_customer c 
                ON o.customer_id = c.id 
                JOIN auth_user a
                ON c.user_id = a.id
                WHERE o.payment_type_id IS NOT NULL
                GROUP BY o.id
            """)

            dataset = db_cursor.fetchall()

            order_list = {}

            for row in dataset:
                order_id = row["order_id"]
                full_name = row["full_name"]
                price = row["total_price"]
                payment_type = row["payment_type"]

                order_list[order_id] = {}
                order_list[order_id]["id"] = order_id
                order_list[order_id]["customer_name"] = full_name
                order_list[order_id]["total_price"] = price
                order_list[order_id]["payment_type"] = payment_type

        completed_list = order_list.values()
        template = 'orders/completed_orders.html'
        context = {
            'completed_orders': completed_list
        }

        return render(request, template, context)
