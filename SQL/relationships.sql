CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100),
  category TEXT,
  price NUMERIC(10,2),
  stock_quantity INT,
  is_available BOOLEAN,
  added_on DATE
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  product_id INT,
  quantity INT,
  order_date DATE,
  customer_name VARCHAR(50),
  payment_method VARCHAR(50),
  CONSTRAINT fk_product FOREIGN KEY (product_id)
  REFERENCES products(product_id) ON DELETE CASCADE
);

select *From products;
select *From orders;

-- Q1. Show each order along with the product name and price. 
SELECT o.order_id, o.customer_name, p.product_name, p.price 
FROM products p JOIN orders o ON p.product_id = o.product_id; 

-- Q2. Show all products even if they were never ordered.
SELECT p.product_name, o.order_id from products p 
LEFT JOIN orders o ON o.product_id = p.product_id;

-- Q3.Show orders for only ‘Electronics’ category.
SELECT o.order_id, o.customer_name, p.product_name, p.category
FROM products p JOIN orders o ON p.product_id = o.product_id where p.category = 'Electronics';

-- Q4.List all orders sorted by product price (high to low).
SELECT o.order_id, o.customer_name, p.product_name, p.price
FROM orders o JOIN products p 
ON p.product_id = o.product_id ORDER BY p.price DESC;

-- Q5.Show number of orders placed for each product.
SELECT p.product_name, COUNT(o.order_id) as total_orders
FROM products p LEFT JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_name;

-- Q6.Show total revenue earned per product.
SELECT p.product_name, SUM(p.price * o.quantity) as total_revenue
FROM orders o JOIN products p ON p.product_id = o.product_id
GROUP BY p.product_name ORDER BY total_revenue DESC;

-- Q7.Show products where total order revenue > ₹2000.
SELECT p.product_name, SUM(p.price * o.quantity) as total_revenue
FROM orders o JOIN products p ON p.product_id = o.product_id
GROUP BY p.product_name HAVING SUM(p.price * o.quantity) > 2000;

-- Q8.Show unique customers who ordered ‘Fitness’ products.
SELECT DISTINCT o.customer_name, p.product_name, p.category
FROM orders o JOIN products p ON p.product_id = o.product_id
WHERE category = 'Fitness';