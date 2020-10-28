import sqlite3

conn = sqlite3.connect('aztlan.db')

conn.execute('''CREATE TABLE Category
  (idCategory INTEGER PRIMARY KEY,
  Name        VARCHAR(45) NOT NULL,
  UNIQUE (Name COLLATE NOCASE)
  );''')


conn.execute('''CREATE TABLE Boardgame
  (idBoardgame INTEGER PRIMARY KEY,
  Title VARCHAR(256) NOT NULL UNIQUE,
  Description TEXT,
  OriginalPrice INT,
  CurrentPrice INT,
  BaseGame INT DEFAULT 0,
  Standalone INT DEFAULT 1,
  FOREIGN KEY (Basegame) REFERENCES Boardgame (idBoardgame)
  );''')

conn.execute('''CREATE TABLE Category_Boardgame
  (fkCategory INT NOT NULL,
  fkBoardgame INT NOT NULL,
  FOREIGN KEY (fkCategory) REFERENCES Category (idCategory),
  FOREIGN KEY (fkBoardgame) REFERENCES Boardgame (idBoardgame),
  UNIQUE (fkCategory, fkBoardgame)
  );''')




conn.execute('''CREATE TABLE Item
  (idItem INTEGER PRIMARY KEY,  
  fkBoardgame INT NOT NULL,
  Description TEXT,
  FOREIGN KEY (fkBoardgame) REFERENCES Boardgame (idBoardgame)
  );''')


conn.execute('''CREATE TABLE Pais
  (idPais INTEGER PRIMARY KEY,
  Name        VARCHAR(45) NOT NULL UNIQUE
  );''')

conn.execute('''CREATE TABLE Provincia
  (idProvincia INTEGER PRIMARY KEY,
  Name        VARCHAR(45) NOT NULL, 
  fkPais INT NOT NULL,
  FOREIGN KEY (fkPais) REFERENCES Pais (idPais),
  UNIQUE (Name, fkPais)
  );''')

conn.execute('''CREATE TABLE Canton
  (idCanton INTEGER PRIMARY KEY,
  Name        VARCHAR(45) NOT NULL, 
  fkProvincia INT NOT NULL,
  FOREIGN KEY (fkProvincia) REFERENCES Provincia (idProvincia),
  UNIQUE (Name, fkProvincia)
  );''')


conn.execute('''CREATE TABLE Distrito
  (idDistrito INTEGER PRIMARY KEY,
  Name        VARCHAR(45) NOT NULL, 
  Postal_code INT, 
  fkCanton INT NOT NULL,
  FOREIGN KEY (fkCanton) REFERENCES Canton (idCanton),
  UNIQUE (Name, fkCanton)
  );''')


conn.execute('''CREATE TABLE LocalStore
  (idLocalStore INTEGER PRIMARY KEY,
  Name VARCHAR(45) NOT NULL,  
  Direccion TEXT
  );''')


conn.execute('''CREATE TABLE Customer
  (idCustomer INTEGER PRIMARY KEY,
  Name VARCHAR(45) NOT NULL,  
  Lastname VARCHAR(45) NOT NULL,  
  fkDistrito INT,
  Direccion TEXT,
  Phone1 INT, 
  Phone2 INT, 
  Create_date DATE NOT NULL, 
  Active INT NOT NULL DEFAULT 1, 
  Email1 VARCHAR(45) NOT NULL UNIQUE ,
  Email2 VARCHAR(45),  
  Identification VARCHAR(45) UNIQUE,
  FOREIGN KEY (fkDistrito) REFERENCES Distrito (idDistrito),
  );''')



conn.execute('''CREATE TABLE Rental
  (idRental INTEGER PRIMARY KEY,
  Rental_date DATETIME NOT NULL,
  Expected_date DATETIME NOT NULL, 
  Returned_date DATETIME,  
  fkLocalStore INT NOT NULL,
  fkCustomer INT NOT NULL,
  Price INT NOT NULL,
  Paid INT,
  Payment_mathod VARCHAR(45),
  Description TEXT NULL,
  FOREIGN KEY (fkLocalStore) REFERENCES LocalStore (idLocalStore),
  FOREIGN KEY (fkCustomer) REFERENCES Customer (idCustomer)
  );''')

conn.execute('''CREATE TABLE Rental_Item
  (fkItem INT NOT NULL,
  fkRental INT NOT NULL,
  FOREIGN KEY (fkItem) REFERENCES Item (idItem),
  FOREIGN KEY (fkRental) REFERENCES Rental (idRental),
  UNIQUE (fkItem, fkRental)
  );''')



conn.close()
