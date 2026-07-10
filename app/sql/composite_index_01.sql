-- BEFORE COMPOSITE INDEXING
EXPLAIN ANALYZE
SELECT *
FROM order_items
WHERE order_id = 500
AND product_id = 25;


-- OUTPUT
Seq Scan on order_items  (cost=0.00..1225.00 rows=1 width=16) (actual time=16.810..16.811 rows=0.00 loops=1)


-- AFTER COMPOSITE INDEXING
CREATE INDEX idx_order_items_order_product
ON order_items(order_id, product_id);

EXPLAIN ANALYZE
SELECT *
FROM order_items
WHERE order_id = 500
AND product_id = 25;


-- OUTPUT
Index Scan using idx_order_items_order_product on order_items  (cost=0.29..8.31 rows=1 width=16) (actual time=69.826..69.827 rows=0.00 loops=1)