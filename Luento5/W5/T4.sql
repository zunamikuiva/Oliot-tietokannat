CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price_per_kilo NUMERIC NOT NULL
);

CREATE TABLE receipt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cashier TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_receipt (
    amount REAL NOT NULL,
    product_id INTEGER NOT NULL,
    receipt_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (receipt_id) REFERENCES receipt(id)
);

INSERT INTO product (name, price_per_kilo) VALUES
('Chunkies', 8),
('Rifrafs', 7),
('Rumbles', 9.5),
('Yumyums', 6),
('Salmarish', 10);

INSERT INTO receipt (cashier, created_at) VALUES
('Alice', 1672531200),
('Alice', 1672617600),
('Alice', 1672704000),
('Alice', 1672790400),
('Alice', 1672876800);

INSERT INTO product_receipt (amount, product_id, receipt_id) VALUES
(0.8, 2, 1),
(1.2, 4, 2),
(1.4, 1, 3),
(0.6, 3, 4),
(1.1, 5, 5);