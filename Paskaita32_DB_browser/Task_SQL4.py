"""
---------------------------------------------------1-------------------------------------------------------------------
1. SUKURIAMAS CUSTOMER TABLE
CREATE TABLE customer(
	id INTEGER PRIMARY KEY,
	f_name VARCHAR(50) NOT NULL,
	l_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE
	)


2. SUKURIAMAS STATUS TABLE

CREATE TABLE status(
	id INTEGER PRIMARY KEY,
	name VARCHAR(50) NOT NULL
	)


3. SUKURIAMAS PRODUCT TABLE

CREATE TABLE product(
	id INTEGER PRIMARY KEY,
	name VARCHAR(50),
	price FLOAT
	)


4. SUKURIAMAS order_ TABLE kuris turi sarysi su customer_id ir status_id

CREATE TABLE order_(
	id INTEGER PRIMARY KEY,
	customer_id INTEGER,
	date_ VARCHAR(50),
	status_id INTEGER,
	FOREIGN KEY (customer_id) REFERENCES customer (id),
	FOREIGN KEY (status_id) REFERENCES status (id)
	)


5.

CREATE TABLE product_order(
	order_id INTEGER,
	product_id INTEGER,
	quantity INTEGER,
	FOREIGN KEY (order_id) REFERENCES order_ (id)
	FOREIGN KEY (product_id) REFERENCES product (id)
	)


---------------------------------------------------2-------------------------------------------------------------------
Užpildykite duomenimis - bent 3 klientai, bent 5 užsakymai, kiekviename jų po 1-3 pozicijas(product_order),
keletas produktų, keletas užsakymo statusų (pvz, patvirtintas, vykdomas, įvykdytas, atmestas)





---------------------------------------------------3-------------------------------------------------------------------
uzklausa su kuria gaunu order_id, date_, l_name, bendra suma

SELECT product_order.order_id, order_.date_, customer.l_name,
(product_order.quantity * product.price) as total_sum
FROM product_order
JOIN order_ ON product_order.order_id = order_.id
JOIN customer ON order_.customer_id = customer.id
JOIN product on product_order.product_id = product.id


Uzklausa su kuria gaunu uzsakymo_id, uzsakymo_name, quantity, price, bendra suma:

SELECT order_.id, product.name, product_order.quantity, product.price,
(product_order.quantity * product.price) as total
FROM product_order
JOIN order_ ON product_order.order_id = order_.id
JOIN product ON product_order.product_id = product.id


Uzklausa su kuria gaunu uzsakymo_name, quantity, price, bendra suma:

SELECT product.name, product_order.quantity, product.price,
(product_order.quantity * product.price) as total
FROM product_order
JOIN order_ ON product_order.order_id = order_.id
JOIN product ON product_order.product_id = product.id
"""