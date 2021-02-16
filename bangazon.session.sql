                SELECT buyer.first_name as Customer_Name, seller.first_name as Favorite_Seller_Name
                FROM bangazonapi_favorite favorite
                JOIN bangazonapi_customer buyer_customer
                ON favorite.customer_id = buyer_customer.id
                JOIN auth_user buyer
                ON buyer.id =  buyer_customer.user_id
                JOIN bangazonapi_customer seller_customer
                ON favorite.seller_id = seller_customer.id
                JOIN auth_user seller
                ON seller.id = seller_customer.user_id
