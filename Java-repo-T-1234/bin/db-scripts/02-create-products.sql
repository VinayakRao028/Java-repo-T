-- -----------------------------------------------------
-- Schema full-stack-ecommerce
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `full-stack-ecommerce`;

CREATE SCHEMA `full-stack-ecommerce`;
USE `heroku_c0edb524a9c3c7d`;

-- -----------------------------------------------------
-- Table `full-stack-ecommerce`.`product_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mpvmweiv00pv3pt2`.`product_category` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(255) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;

-- -----------------------------------------------------
-- Table `full-stack-ecommerce`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mpvmweiv00pv3pt2`.`product` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `sku` VARCHAR(255) NULL,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `unit_price` DECIMAL(13,2) NULL,
  `image_url` VARCHAR(255) NULL,
  `active` BOOLEAN DEFAULT TRUE,
  `units_in_stock` INT NULL,
  `date_created` DATETIME NULL,
  `last_updated` DATETIME NULL,
  `category_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category` (`category_id`),
  CONSTRAINT `fk_category` FOREIGN KEY (`category_id`) REFERENCES `product_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;

-- -----------------------------------------------------
-- Add sample data
-- -----------------------------------------------------

INSERT INTO product_category(category_name) VALUES ('BOOKS');

INSERT INTO product (sku, name, description, image_url, active, units_in_stock, unit_price, category_id, date_created)
VALUES 
('BOOK-TECH-1000', 'JavaScript - The Fun Parts', 'Learn JavaScript', 'assets/images/products/placeholder.png', TRUE, 100, 19.99, 1, NOW()),
('BOOK-TECH-1001', 'Spring Framework Tutorial', 'Learn Spring', 'assets/images/products/placeholder.png', TRUE, 100, 29.99, 1, NOW()),
('BOOK-TECH-1002', 'Kubernetes - Deploying Containers', 'Learn Kubernetes', 'assets/images/products/placeholder.png', TRUE, 100, 24.99, 1, NOW()),
('BOOK-TECH-1003', 'Internet of Things (IoT) - Getting Started', 'Learn IoT', 'assets/images/products/placeholder.png', TRUE, 100, 29.99, 1, NOW()),
('BOOK-TECH-1004', 'The Go Programming Language: A to Z', 'Learn Go', 'assets/images/products/placeholder.png', TRUE, 100, 24.99, 1, NOW());