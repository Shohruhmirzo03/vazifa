DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;


CREATE TABLE IF NOT EXISTS categories(
	category_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	massa INTEGER,
	narxi INTEGER
);


CREATE TABLE IF NOT EXISTS products(
	product_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	sabzavotlar VARCHAR,
	mevalar VARCHAR
    category_id INTEGER REFERENCES categories(category_id)
);




INSERT INTO products(sabzavotlar) VALUES ('kartoshka');
INSERT INTO products(sabzavotlar) VALUES ('piyoz');
INSERT INTO products(sabzavotlar) VALUES ('sabzi');
INSERT INTO products(sabzavotlar) VALUES ('sholgom');
INSERT INTO products(sabzavotlar) VALUES ('karam');
INSERT INTO products(sabzavotlar) VALUES ('pomidor');

	
SELECT * FROM categories;	

SELECT * FROM products;	
