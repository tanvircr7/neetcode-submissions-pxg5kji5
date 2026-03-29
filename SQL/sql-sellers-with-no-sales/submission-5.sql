-- Write your query below
select seller_name
FROM seller
WHERE seller_id NOT IN (select seller_id from orders WHERE sale_date >= '2020-01-01' and sale_date <= '2020-12-31')
ORDER BY seller_name ASC