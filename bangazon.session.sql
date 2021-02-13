SELECT o.id order_id, SUM(pr.price) total_price, a.first_name || ' ' || a.last_name AS full_name
FROM bangazonapi_order o
JOIN bangazonapi_orderproduct op
ON o.id = op.order_id
JOIN bangazonapi_product pr 
ON op.product_id = pr.id
JOIN bangazonapi_customer c 
ON o.customer_id = c.id 
JOIN auth_user a
ON c.user_id = a.id
WHERE o.payment_type_id IS NULL
GROUP BY o.id
