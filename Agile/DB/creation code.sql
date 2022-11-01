-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema agile_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema agile_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `agile_project` DEFAULT CHARACTER SET utf8 ;
USE `agile_project` ;

-- -----------------------------------------------------
-- Table `agile_project`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`admin` (
  `admin_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(125) NULL,
  `date_of_birth` DATE NULL,
  `salary` FLOAT NULL,
  `contact_info` INT NULL,
  `date_of_employement` DATE NULL,
  PRIMARY KEY (`admin_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`building`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`building` (
  `building_id` INT NOT NULL,
  `location` VARCHAR(45) NULL,
  `admin_id` INT NOT NULL,
  `total_floor` INT NULL,
  PRIMARY KEY (`building_id`, `admin_id`),
  INDEX `fk_building_admin1_idx` (`admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_building_admin1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `agile_project`.`admin` (`admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`building_admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`building_admin` (
  `building_admin_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(125) NULL,
  `date_of_birth` DATE NULL,
  `salary` FLOAT NULL,
  `contact_info` INT NULL,
  `date_of_employement` DATE NULL,
  `admin_id` INT NOT NULL,
  `building_id` INT NOT NULL,
  PRIMARY KEY (`building_admin_id`, `admin_id`, `building_id`),
  INDEX `fk_building_admin_admin1_idx` (`admin_id` ASC) VISIBLE,
  INDEX `fk_building_admin_building1_idx` (`building_id` ASC) VISIBLE,
  CONSTRAINT `fk_building_admin_admin1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `agile_project`.`admin` (`admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_building_admin_building1`
    FOREIGN KEY (`building_id`)
    REFERENCES `agile_project`.`building` (`building_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`floor_admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`floor_admin` (
  `floor_admin_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(125) NULL,
  `date_of_birth` DATE NULL,
  `salary` FLOAT NULL,
  `contact_info` INT NULL,
  `date_of_employement` DATE NULL,
  `building_admin_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  `building_id` INT NOT NULL,
  PRIMARY KEY (`floor_admin_id`, `building_admin_id`, `admin_id`, `building_id`),
  INDEX `fk_floor_admin_building_admin_idx` (`building_admin_id` ASC) VISIBLE,
  INDEX `fk_floor_admin_admin1_idx` (`admin_id` ASC) VISIBLE,
  INDEX `fk_floor_admin_building1_idx` (`building_id` ASC) VISIBLE,
  CONSTRAINT `fk_floor_admin_building_admin`
    FOREIGN KEY (`building_admin_id`)
    REFERENCES `agile_project`.`building_admin` (`building_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_floor_admin_admin1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `agile_project`.`admin` (`admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_floor_admin_building1`
    FOREIGN KEY (`building_id`)
    REFERENCES `agile_project`.`building` (`building_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`receptionist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`receptionist` (
  `receptionist_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(125) NULL,
  `date_of_birth` DATE NULL,
  `salary` FLOAT NULL,
  `contact_info` INT NULL,
  `date_of_employement` DATE NULL,
  `building_admin_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  `building_id` INT NOT NULL,
  PRIMARY KEY (`receptionist_id`, `building_admin_id`, `admin_id`, `building_id`),
  INDEX `fk_receptionist_building_admin1_idx` (`building_admin_id` ASC) VISIBLE,
  INDEX `fk_receptionist_admin1_idx` (`admin_id` ASC) VISIBLE,
  INDEX `fk_receptionist_building1_idx` (`building_id` ASC) VISIBLE,
  CONSTRAINT `fk_receptionist_building_admin1`
    FOREIGN KEY (`building_admin_id`)
    REFERENCES `agile_project`.`building_admin` (`building_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_receptionist_admin1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `agile_project`.`admin` (`admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_receptionist_building1`
    FOREIGN KEY (`building_id`)
    REFERENCES `agile_project`.`building` (`building_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`floor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`floor` (
  `floor_id` INT NOT NULL,
  `status` VARCHAR(45) NULL,
  `building_id` INT NOT NULL,
  `building_admin_id` INT NOT NULL,
  `floor_admin_id` INT NOT NULL,
  `total_room` INT NULL,
  `gender` TINYINT NULL,
  PRIMARY KEY (`floor_id`, `building_id`, `building_admin_id`, `floor_admin_id`),
  INDEX `fk_floor_building1_idx` (`building_id` ASC, `building_admin_id` ASC) VISIBLE,
  INDEX `fk_floor_floor_admin1_idx` (`floor_admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_floor_building1`
    FOREIGN KEY (`building_id` , `building_admin_id`)
    REFERENCES `agile_project`.`building` (`building_id` , `admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_floor_floor_admin1`
    FOREIGN KEY (`floor_admin_id`)
    REFERENCES `agile_project`.`floor_admin` (`floor_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`room` (
  `room_id` INT NOT NULL,
  `status` VARCHAR(45) NULL,
  `floor_id` INT NOT NULL,
  `building_id` INT NOT NULL,
  `building_admin_id` INT NOT NULL,
  `total_bed` INT NULL,
  PRIMARY KEY (`room_id`, `floor_id`, `building_id`, `building_admin_id`),
  INDEX `fk_room_floor1_idx` (`floor_id` ASC, `building_id` ASC, `building_admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_room_floor1`
    FOREIGN KEY (`floor_id` , `building_id` , `building_admin_id`)
    REFERENCES `agile_project`.`floor` (`floor_id` , `building_id` , `building_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`bed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`bed` (
  `bed_id` INT NOT NULL,
  `status` VARCHAR(45) NULL,
  `room_id` INT NOT NULL,
  `floor_id` INT NOT NULL,
  `building_id` INT NOT NULL,
  `building_admin_id` INT NOT NULL,
  PRIMARY KEY (`bed_id`, `room_id`, `floor_id`, `building_id`, `building_admin_id`),
  INDEX `fk_bed_room1_idx` (`room_id` ASC, `floor_id` ASC, `building_id` ASC, `building_admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_bed_room1`
    FOREIGN KEY (`room_id` , `floor_id` , `building_id` , `building_admin_id`)
    REFERENCES `agile_project`.`room` (`room_id` , `floor_id` , `building_id` , `building_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`user` (
  `national_id` INT NOT NULL,
  `date_of_birth` DATE NULL,
  `rate` CHAR(1) NULL,
  `first_name` VARCHAR(45) NULL,
  `middle_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `gender` VARCHAR(45) NULL,
  `eligible` TINYINT NULL,
  `last_stay` DATETIME NULL,
  PRIMARY KEY (`national_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`reservation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`reservation` (
  `reservation_id` INT NOT NULL,
  `bed_id` INT NOT NULL,
  `room_id` INT NOT NULL,
  `floor_id` INT NOT NULL,
  `building_id` INT NOT NULL,
  `building_admin_id` INT NOT NULL,
  `receptionist_id` INT NOT NULL,
  `floor_admin_id` INT NOT NULL,
  `date_of_entry` TIMESTAMP NULL,
  `user_national_id` INT NOT NULL,
  `date_of_leave` DATETIME NULL,
  `stay_rate` CHAR(1) NULL,
  PRIMARY KEY (`reservation_id`, `bed_id`, `room_id`, `floor_id`, `building_id`, `building_admin_id`, `receptionist_id`, `floor_admin_id`, `user_national_id`),
  INDEX `fk_reservation_bed1_idx` (`bed_id` ASC, `room_id` ASC, `floor_id` ASC, `building_id` ASC, `building_admin_id` ASC) VISIBLE,
  INDEX `fk_reservation_receptionist1_idx` (`receptionist_id` ASC) VISIBLE,
  INDEX `fk_reservation_floor_admin1_idx` (`floor_admin_id` ASC) VISIBLE,
  INDEX `fk_reservation_user1_idx` (`user_national_id` ASC) VISIBLE,
  CONSTRAINT `fk_reservation_bed1`
    FOREIGN KEY (`bed_id` , `room_id` , `floor_id` , `building_id` , `building_admin_id`)
    REFERENCES `agile_project`.`bed` (`bed_id` , `room_id` , `floor_id` , `building_id` , `building_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reservation_receptionist1`
    FOREIGN KEY (`receptionist_id`)
    REFERENCES `agile_project`.`receptionist` (`receptionist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reservation_floor_admin1`
    FOREIGN KEY (`floor_admin_id`)
    REFERENCES `agile_project`.`floor_admin` (`floor_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reservation_user1`
    FOREIGN KEY (`user_national_id`)
    REFERENCES `agile_project`.`user` (`national_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`communication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`communication` (
  `communication_id` INT NOT NULL,
  `type` VARCHAR(45) NULL,
  `from_id` INT NULL,
  `to_id` INT NULL,
  `message` VARCHAR(1500) NULL,
  PRIMARY KEY (`communication_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`citizen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`citizen` (
  `national_id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `middle_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `gender` TINYINT NULL,
  `date_of_birth` DATE NULL,
  PRIMARY KEY (`national_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agile_project`.`login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agile_project`.`login` (
  `login_id` INT NOT NULL,
  `id` INT NULL,
  `password` INT NULL,
  `type` INT NULL,
  PRIMARY KEY (`login_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
