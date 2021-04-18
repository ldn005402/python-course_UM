CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Saarah', 40);
INSERT INTO Ages (name, age) VALUES ('Nuala', 14);
INSERT INTO Ages (name, age) VALUES ('Liall', 35);
INSERT INTO Ages (name, age) VALUES ('Elvita', 30);
INSERT INTO Ages (name, age) VALUES ('Norman', 27);
INSERT INTO Ages (name, age) VALUES ('Nadine', 31);

SELECT hex(name || age) AS X 
FROM Ages 
ORDER BY X
