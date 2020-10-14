CREATE TABLE dealer (
    id_dealer INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cpf TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE purchase (
    id_purchase INTEGER PRIMARY KEY,
    code INTEGER NOT NULL,
    value INTEGER NOT NULL,
    date TEXT NOT NULL,
    cpf TEXT NOT NULL,
    status TEXT DEFAULT 'Em validação'
);

 DROP TABLE dealer;
 DROP TABLE purchase;

SELECT * FROM dealer;
SELECT name, cpf, email, password FROM dealer;
SELECT * FROM purchase;
SELECT code, value, date, cpf, status FROM purchase;

INSERT INTO dealer (name, cpf, email, password)
VALUES ('Leonardo', '555.555.555-55', 'teste@teste.com', 'senha123');

INSERT INTO dealer (name, cpf, email, password)
VALUES ('Leonardo', '153.509.460-56', 'teste@teste.com', 'senha123');

INSERT INTO purchase (code, value, date, cpf, status)
VALUES (12345, 850, '2020-07-10 01:32:10', '555.555.555-55', 'Em validação');

INSERT INTO db.dealer (name,cpf,email,password) VALUES ('Leonardo', '555.555.555-55', 'teste@teste.com', 'senha123');

SELECT * FROM db.sqlite_master WHERE type='table';
