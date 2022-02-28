
CREATE DATABASE blixentech;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
);

CREATE TABLE `usuario` (
  `user_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `number` int(50) NOT NULL
);

CREATE TABLE `product` (
  `prod_id` int(11) PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `price` float(50) NOT NULL,
  `quantity` int(50) NOT NULL,
  `image` varchar(255)
);

INSERT INTO `product`(`name`, `type`, `price`, `quantity`,`image` ) VALUES
('PS5 Marvel spider-man Miles Morales', 'game',49.9,17,'spiderM.jpg'),
('PS3 Alice: Madness Return', 'game',59.9,23,,'spiderM.jpg'),
('XBOX 360 SLIM 320GB', 'console',109.9,17,'xBox.png')
('League of legends', 'game',69.9,17,'lol.jpg')


INSERT INTO `employee`(`username`, `email`, `password` ) VALUES
('admin', 'admin@gmail.com','admin'),
('Isabel Dos Santos', 'isabelS@gmail.com',123)

INSERT INTO `usuario`(`name`, `email`, `password`, `number`) VALUES
('Fernanda Chaves', 'fernandafortesch@gmail.com',123,936822470),
('Lilo Stitch', 'lilos@gmail.com','abc',987567812)