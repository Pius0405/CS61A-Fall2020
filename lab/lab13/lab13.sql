.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price)
  FROM inventory
  GROUP BY ITEM;

CREATE TABLE best_item AS
  SELECT products.name, lowest_prices.store, min(MSRP/rating)
  FROM products, lowest_prices
  WHERE products.name = lowest_prices.item
  GROUP BY products.category;

CREATE TABLE shopping_list AS
  SELECT name, store
  FROM best_item;

CREATE TABLE total_bandwidth AS
  SELECT sum(stores.Mbs)
  FROM shopping_list, stores
  WHERE stores.store = shopping_list.store;

