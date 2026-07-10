-- INNER JOIN
SELECT
c.name,
o.id,
o.total_amount
FROM customers c
INNER JOIN orders o
ON c.id=o.customer_id;


-- LEFT JOIN
SELECT
cat.name,
p.name
FROM categories cat
LEFT JOIN products p
ON cat.id=p.category_id;


-- RIGHT JOIN
SELECT
p.name,
oi.quantity
FROM order_items oi
RIGHT JOIN products p
ON oi.product_id=p.id;


-- FULL OUTER JOIN
SELECT
e.name,
o.id
FROM employees e
FULL OUTER JOIN orders o
ON e.id=o.employee_id;


-- SELF JOIN
SELECT
c1.name,
c2.name
FROM customers c1
JOIN customers c2
ON LEFT(c1.phone,4)=LEFT(c2.phone,4)
AND c1.id<c2.id;

