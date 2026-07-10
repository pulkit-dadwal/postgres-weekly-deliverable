-- BEFORE COMPOSITE INDEXING
EXPLAIN ANALYZE
SELECT *
FROM products
WHERE category_id = 3
ORDER BY price;


-- OUTPUT
Seq Scan on products  (cost=0.00..2.25 rows=15 width=29) (actual time=0.024..0.037 rows=15.00 loops=1)


-- AFTER COMPOSITE INDEXING
CREATE INDEX idx_products_category_price
ON products(category_id, price);

EXPLAIN ANALYZE
SELECT *
FROM products
WHERE category_id = 3
ORDER BY price;

-- OUTPUT
Index Scan using idx_orders_customer_status on orders  (cost=0.29..8.31 rows=1 width=37) (actual time=2.890..2.896 rows=2.00 loops=1)