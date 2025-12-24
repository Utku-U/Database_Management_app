

create database Product_Stock_management;
use Product_Stock_management;

-- Products Table --
create table Product(
Product_id INT auto_increment PRIMARY KEY,
Product_name varchar (50) NOT NULL ,
Supplier_id INT,
Category_id INT,
Unit_price DECIMAL(5,2) NOT NULL,
Unit varchar(10) NOT NULL,
Discounted TEXT
);
select*from Product;
drop table Product;


ALTER TABLE Product
MODIFY column Discounted ENUM("Yes","No");


ALTER TABLE Product
ADD CONSTRAINT fk_Supplier_id FOREIGN KEY (Supplier_id) references Supplier(Supplier_id);
ALTER TABLE Product
ADD FOREIGN KEY (Category_id) references Categories(Category_id);



-- Categories Table --
create table Categories(
Category_id INT auto_increment PRIMARY KEY ,
Category_name ENUM("food","Health","Electronic","Toys"),
Description TEXT

);
select*from Categories;
drop table Categories;

ALTER table Categories
MODIFY column Category_name varchar(100);


-- Suppliers Table --
create table Supplier(
Supplier_id INT AUTO_INCREMENT PRIMARY KEY,
Company_name varchar(200) UNIQUE NOT NULL,
Contact_name varchar(100) UNIQUE NOT NULL,
Email varchar(60) UNIQUE NOT NULL,
Phone varchar(20) UNIQUE NOT NULL,
Address varchar(100) NOT NULL,
City varchar(60) NOT NULL,
Country varchar(60) NOT NULL

);
select*from Supplier;
drop table Supplier;



-- Inventories Table --
create table Inventory(
Inventory_id INT AUTO_INCREMENT PRIMARY KEY,
Product_id INT,
Wherehouse INT NOT NULL,
Quantity INT NOT NULL
);
select*from Inventory;
drop table Inventory;


ALTER TABLE Inventory
MODIFY COLUMN Wherehouse VARCHAR(100) NOT NULL;

ALTER TABLE Inventory
ADD CONSTRAINT fk_Product FOREIGN KEY(Product_id) references Product(Product_id);


-- Value Assignments --

-- CATEGORİES value assignments --
INSERT INTO Categories(Category_name, Description) values
("food", "Kaliteli yiyecek ürünleri"),
("Health", "Sağlık ve kişisel bakım ürünleri"),
("Toys", "Eğitici ve yaratıcı çocuk oyuncakları"),
("Electronic", "Ev elektroniği ve akıllı ev sistemleri")
select*from Categories;
drop table categories;

-- SUPPLIER value assignments --
INSERT INTO Supplier(Company_name, Contact_name, Email, Phone, Address, City, Country) values
("Utku Ticaret", "Utku Yılmaz", "utkuynk141@gmail.com", "05321234567", "Yenimahalle", "Ankara", "Türkiye"),
("Ekin Gıda", "Ekin Demir", "ekin@gida.com", "05439876543", "Bornova", "İzmir", "Türkiye"),
("Tekno Market", "Zeynep Kaya", "zeynep@tekno.com", "05551231234", "Kadıköy", "İstanbul", "Türkiye");
select*from Supplier;

-- PRODUCT value assignments --
select*from categories;
select*from supplier;

INSERT INTO Product(Product_name, Supplier_id, Category_id, Unit_price, Unit, Discounted) VALUES
("Organik Yulaf Ezmesi", 2, 1, 34.90, "750g", "No"),
("Akıllı Saat", 3, 4, 649.99, "adet", "No"),
("Probiyotik Yoğurt", 1, 1, 18.50, "500g", "No"),
("Çocuk Zeka Kartları", 1, 3, 45.00, "set", "No"),
("Balık Yağı Şurubu", 2, 1, 92.75, "150ml", "No"),
("Kablosuz Mouse", 3, 4, 129.90, "adet", "No"),
("Bebek Oyuncak Seti", 1, 3, 159.50, "kutu", "No"),
("Multivitamin Tablet", 2, 2, 110.00, "90tb", "No"),
("LED Işık Şeridi", 3, 4, 89.90, "5m", "No"),
("Kavrulmuş Badem", 2, 1, 48.00, "250g", "No"),
("Doğal Fındık Ezmesi", 2, 1, 57.00, "300g", "No"),
("Mini Dron", 3, 4, 749.00, "adet", "No"),
("Şekersiz Granola", 2, 1, 44.90, "400g", "No"),
("Çocuk Puzzle 100 Parça", 1, 3, 36.00, "kutu", "No"),
("Yüz Temizleme Köpüğü", 2, 2, 59.90, "150ml", "No"),
("Akıllı Ampul", 3, 4, 119.99, "adet", "No"),
("Organik Mercimek", 1, 1, 32.75, "1kg", "No"),
("Ahşap Blok Seti", 1, 3, 85.00, "set", "No"),
("Kolajen Takviyesi", 2, 2, 145.00, "60tb", "No"),
("Bluetooth Hoparlör", 3, 4, 239.90, "adet", "No"),
("Doğal Zeytinyağı", 2, 1, 78.50, "1L", "No"),
("Mıknatıslı Harf Oyunu", 1, 2, 49.00, "set", "No"),
("Cilt Serumu", 2, 2, 130.00, "30ml", "No"),
("Akıllı Priz", 3, 4, 99.90, "adet", "No"),
("Kuru Kayısı", 2, 1, 38.00, "500g", "No");
select*from Product;

-- INVERTORY value assignments --
-- wherehouse 101(food warehouse)
-- wherehouse 102(Electronic warehouse)
-- wherehouse 103(Health warehouse)
-- wherehouse 104(Toys warehouse)

INSERT INTO Inventory(Product_id, Wherehouse, Quantity) VALUES
(1, 101, 100),
(2, 102, 45),
(3, 101, 70),
(4, 104, 120),
(5, 103, 90),
(6, 102, 110),
(7, 104, 95),
(8, 103, 55),
(9, 102, 130),
(10, 101, 50),
(11, 101, 40),
(12, 102, 25),
(13, 101, 65),
(14, 104, 85),
(15, 103, 70),
(16, 102, 100),
(17, 101, 90),
(18, 104, 80),
(19, 103, 60),
(20, 102, 95),
(21, 101, 110),
(22, 104, 70),
(23, 103, 65),
(24, 102, 88),
(25, 101, 75);

UPDATE Inventory SET Wherehouse = 'Gimat' WHERE Wherehouse = '101';
UPDATE Inventory SET Wherehouse = 'Persemebe' WHERE Wherehouse = '102';
UPDATE Inventory SET Wherehouse = 'Gebze' WHERE Wherehouse = '103';
UPDATE Inventory SET Wherehouse = 'Tarsus' WHERE Wherehouse = '104';

select*from Inventory;
