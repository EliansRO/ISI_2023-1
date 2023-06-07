-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-06-2023 a las 05:11:22
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pensiones-isi-2023`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pensions`
--

CREATE TABLE `pensions` (
  `id` int(11) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `availability` tinyint(1) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pensions`
--

INSERT INTO `pensions` (`id`, `photo`, `name`, `description`, `price`, `availability`, `owner_id`) VALUES
(1, 'https://picsum.photos/200', 'Pensión 0.09190374807631946', 'Descripción aleatoria', 85.73, 0, 8),
(2, 'https://picsum.photos/200', 'Pensión 0.3739274818207393', 'Descripción aleatoria', 42.62, 0, 10),
(3, 'https://picsum.photos/200', 'Pensión 0.8129306918130542', 'Descripción aleatoria', 76.00, 0, 9),
(4, 'https://picsum.photos/200', 'Pensión 0.5471092858790506', 'Descripción aleatoria', 15.71, 0, 7),
(5, 'https://picsum.photos/200', 'Pensión 0.811107041138324', 'Descripción aleatoria', 30.98, 0, 9),
(6, 'https://picsum.photos/200', 'Pensión 0.8938709757233699', 'Descripción aleatoria', 52.52, 1, 6),
(7, 'https://picsum.photos/200', 'Pensión 0.898082362392994', 'Descripción aleatoria', 5.17, 1, 9),
(8, 'https://picsum.photos/200', 'Pensión 0.6387092886853118', 'Descripción aleatoria', 19.46, 0, 10),
(9, 'https://picsum.photos/200', 'Pensión 0.3326226867107886', 'Descripción aleatoria', 56.11, 1, 8),
(10, 'https://picsum.photos/200', 'Pensión 0.354137179771566', 'Descripción aleatoria', 70.42, 0, 7),
(11, 'https://picsum.photos/200', 'Pensión 0.5266230595546058', 'Descripción aleatoria', 9.16, 1, 6),
(12, 'https://picsum.photos/200', 'Pensión 0.9466058872142862', 'Descripción aleatoria', 38.43, 0, 7),
(13, 'https://picsum.photos/200', 'Pensión 0.029359512058421515', 'Descripción aleatoria', 38.25, 1, 11),
(14, 'https://picsum.photos/200', 'Pensión 0.3952437931627443', 'Descripción aleatoria', 5.55, 0, 7),
(15, 'https://picsum.photos/200', 'Pensión 0.1905085995704947', 'Descripción aleatoria', 7.27, 1, 10),
(16, 'https://picsum.photos/200', 'Pensión 0.3297104279787377', 'Descripción aleatoria', 42.55, 0, 8),
(17, 'https://picsum.photos/200', 'Pensión 0.6594882529782953', 'Descripción aleatoria', 5.29, 0, 7),
(18, 'https://picsum.photos/200', 'Pensión 0.4979341267588866', 'Descripción aleatoria', 67.62, 1, 8),
(19, 'https://picsum.photos/200', 'Pensión 0.37286500853753185', 'Descripción aleatoria', 64.39, 0, 9),
(20, 'https://picsum.photos/200', 'Pensión 0.560041682384947', 'Descripción aleatoria', 8.27, 1, 8),
(21, 'https://picsum.photos/200', 'Pensión 0.8922393879780912', 'Descripción aleatoria', 20.59, 0, 6),
(22, 'https://picsum.photos/200', 'Pensión 0.6747418247859384', 'Descripción aleatoria', 93.37, 1, 8),
(23, 'https://picsum.photos/200', 'Pensión 0.16506349683279498', 'Descripción aleatoria', 56.69, 0, 11),
(24, 'https://picsum.photos/200', 'Pensión 0.962699627469014', 'Descripción aleatoria', 82.50, 0, 10),
(25, 'https://picsum.photos/200', 'Pensión 0.835836999896762', 'Descripción aleatoria', 5.14, 1, 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `id_card` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `password` varchar(110) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `id_card`, `name`, `last_name`, `username`, `phone`, `password`) VALUES
(6, '1234567890', 'John', 'Doe', 'johndoe@example.com', '1234567890', 'pbkdf2:sha256:150000$8YobD4h3$42f9254331dc1a6afcb7251e54b39c5c1a20f47837a2ce1edab4749e56b0baf0'),
(7, '9876543210', 'Jane', 'Smith', 'janesmith@example.com', '0987654321', 'pbkdf2:sha256:150000$8YobD4h3$42f9254331dc1a6afcb7251e54b39c5c1a20f47837a2ce1edab4749e56b0baf0'),
(8, '5678901234', 'Michael', 'Johnson', 'michaeljohnson@example.com', '5678901234', 'pbkdf2:sha256:150000$8YobD4h3$42f9254331dc1a6afcb7251e54b39c5c1a20f47837a2ce1edab4749e56b0baf0'),
(9, '4321098765', 'Emily', 'Brown', 'emilybrown@example.com', '5432109876', 'pbkdf2:sha256:150000$8YobD4h3$42f9254331dc1a6afcb7251e54b39c5c1a20f47837a2ce1edab4749e56b0baf0'),
(10, '2468135790', 'David', 'Wilson', 'davidwilson@example.com', '2468135790', 'pbkdf2:sha256:150000$8YobD4h3$42f9254331dc1a6afcb7251e54b39c5c1a20f47837a2ce1edab4749e56b0baf0'),
(11, '1010101010', 'Elians Enrique', 'Rocha Muñoz', 'eliansro@unicartagena.edu.co', '1221212121', 'pbkdf2:sha256:600000$GQjJVkFpAZ9PpTvF$9730e22231a9d1f6503e96a0a768a90b09f33226644429632d62df15e9de7943');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pensions`
--
ALTER TABLE `pensions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `owner_id` (`owner_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pensions`
--
ALTER TABLE `pensions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pensions`
--
ALTER TABLE `pensions`
  ADD CONSTRAINT `pensions_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
