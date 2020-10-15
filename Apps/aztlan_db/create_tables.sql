-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Category` (
  `idCategory` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCategory`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Boardgame`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Boardgame` (
  `idBoardgame` INT NOT NULL,
  `Title` VARCHAR(256) NOT NULL,
  `Description` TEXT NULL,
  `OriginalPrice` INT NULL,
  `CurrentPrice` INT NULL,
  PRIMARY KEY (`idBoardgame`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Item` (
  `idItem` INT NOT NULL,
  `Standalone` INT NOT NULL DEFAULT 1,
  `Description` TEXT NULL,
  `Boardgame_idBoardgame` INT NOT NULL,
  PRIMARY KEY (`idItem`),
  INDEX `fk_Item_Boardgame1_idx` (`Boardgame_idBoardgame` ASC) VISIBLE,
  CONSTRAINT `fk_Item_Boardgame1`
    FOREIGN KEY (`Boardgame_idBoardgame`)
    REFERENCES `mydb`.`Boardgame` (`idBoardgame`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Boardgame_has_Language`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Boardgame_has_Language` (
  `Boardgame_idBoardgame` INT NOT NULL,
  `Language_idLanguage` INT NOT NULL,
  PRIMARY KEY (`Boardgame_idBoardgame`, `Language_idLanguage`),
  INDEX `fk_Boardgame_has_Language_Boardgame1_idx` (`Boardgame_idBoardgame` ASC) VISIBLE,
  CONSTRAINT `fk_Boardgame_has_Language_Boardgame1`
    FOREIGN KEY (`Boardgame_idBoardgame`)
    REFERENCES `mydb`.`Boardgame` (`idBoardgame`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Boardgame_has_Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Boardgame_has_Category` (
  `Boardgame_idBoardgame` INT NOT NULL,
  `Category_idCategory` INT NOT NULL,
  PRIMARY KEY (`Boardgame_idBoardgame`, `Category_idCategory`),
  INDEX `fk_Boardgame_has_Category_Category1_idx` (`Category_idCategory` ASC) VISIBLE,
  INDEX `fk_Boardgame_has_Category_Boardgame1_idx` (`Boardgame_idBoardgame` ASC) VISIBLE,
  CONSTRAINT `fk_Boardgame_has_Category_Boardgame1`
    FOREIGN KEY (`Boardgame_idBoardgame`)
    REFERENCES `mydb`.`Boardgame` (`idBoardgame`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Boardgame_has_Category_Category1`
    FOREIGN KEY (`Category_idCategory`)
    REFERENCES `mydb`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Pais` (
  `idPais` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPais`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Provincia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Provincia` (
  `idProvincia` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Pais_idPais` INT NOT NULL,
  PRIMARY KEY (`idProvincia`),
  INDEX `fk_Provincia_Pais1_idx` (`Pais_idPais` ASC) VISIBLE,
  CONSTRAINT `fk_Provincia_Pais1`
    FOREIGN KEY (`Pais_idPais`)
    REFERENCES `mydb`.`Pais` (`idPais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Canton`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Canton` (
  `idCanton` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Provincia_idProvincia` INT NOT NULL,
  PRIMARY KEY (`idCanton`),
  INDEX `fk_Canton_Provincia1_idx` (`Provincia_idProvincia` ASC) VISIBLE,
  CONSTRAINT `fk_Canton_Provincia1`
    FOREIGN KEY (`Provincia_idProvincia`)
    REFERENCES `mydb`.`Provincia` (`idProvincia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Distrito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Distrito` (
  `idDistrito` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Canton_idCanton` INT NOT NULL,
  PRIMARY KEY (`idDistrito`),
  INDEX `fk_Distrito_Canton1_idx` (`Canton_idCanton` ASC) VISIBLE,
  CONSTRAINT `fk_Distrito_Canton1`
    FOREIGN KEY (`Canton_idCanton`)
    REFERENCES `mydb`.`Canton` (`idCanton`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Direccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Direccion` (
  `idDireccion` INT NOT NULL,
  `Descripcion` TEXT NULL,
  `Distrito_idDistrito` INT NOT NULL,
  PRIMARY KEY (`idDireccion`),
  INDEX `fk_Direccion_Distrito1_idx` (`Distrito_idDistrito` ASC) VISIBLE,
  CONSTRAINT `fk_Direccion_Distrito1`
    FOREIGN KEY (`Distrito_idDistrito`)
    REFERENCES `mydb`.`Distrito` (`idDistrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Local`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Local` (
  `idLocal` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Direccion_idDireccion` INT NOT NULL,
  PRIMARY KEY (`idLocal`),
  INDEX `fk_Local_Direccion1_idx` (`Direccion_idDireccion` ASC) VISIBLE,
  CONSTRAINT `fk_Local_Direccion1`
    FOREIGN KEY (`Direccion_idDireccion`)
    REFERENCES `mydb`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customer` (
  `idCustomer` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Lastname` VARCHAR(45) NOT NULL,
  `Direccion_idDireccion` INT NULL,
  `Phone1` INT NULL,
  `Phone2` INT NULL,
  `Create_date` DATE NOT NULL,
  `Active` INT NOT NULL DEFAULT 1,
  `email1` VARCHAR(45) NOT NULL,
  `email2` VARCHAR(45) NULL,
  `Identification` VARCHAR(45) NULL,
  PRIMARY KEY (`idCustomer`),
  INDEX `fk_Customer_Direccion1_idx` (`Direccion_idDireccion` ASC) VISIBLE,
  UNIQUE INDEX `Identification_UNIQUE` (`Identification` ASC) VISIBLE,
  UNIQUE INDEX `email1_UNIQUE` (`email1` ASC) VISIBLE,
  CONSTRAINT `fk_Customer_Direccion1`
    FOREIGN KEY (`Direccion_idDireccion`)
    REFERENCES `mydb`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Rental`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Rental` (
  `idRental` INT NOT NULL,
  `Rental_date` DATETIME NOT NULL,
  `Return_date` DATETIME NULL,
  `Returned` INT NOT NULL DEFAULT 0,
  `Local_idLocal` INT NOT NULL,
  `Customer_idCustomer` INT NOT NULL,
  `Price` INT NOT NULL,
  `Paid` INT NULL,
  `Payment_method` VARCHAR(45) NULL,
  `Description` TEXT NULL,
  PRIMARY KEY (`idRental`),
  INDEX `fk_Rental_Local1_idx` (`Local_idLocal` ASC) VISIBLE,
  INDEX `fk_Rental_Customer1_idx` (`Customer_idCustomer` ASC) VISIBLE,
  CONSTRAINT `fk_Rental_Local1`
    FOREIGN KEY (`Local_idLocal`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rental_Customer1`
    FOREIGN KEY (`Customer_idCustomer`)
    REFERENCES `mydb`.`Customer` (`idCustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Rental_has_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Rental_has_Item` (
  `Rental_idRental` INT NOT NULL,
  `Item_idItem` INT NOT NULL,
  PRIMARY KEY (`Rental_idRental`, `Item_idItem`),
  INDEX `fk_Rental_has_Item_Item1_idx` (`Item_idItem` ASC) VISIBLE,
  INDEX `fk_Rental_has_Item_Rental1_idx` (`Rental_idRental` ASC) VISIBLE,
  CONSTRAINT `fk_Rental_has_Item_Rental1`
    FOREIGN KEY (`Rental_idRental`)
    REFERENCES `mydb`.`Rental` (`idRental`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rental_has_Item_Item1`
    FOREIGN KEY (`Item_idItem`)
    REFERENCES `mydb`.`Item` (`idItem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
