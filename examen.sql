-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 24 Juin 2022 à 04:46
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `examen`
--

-- --------------------------------------------------------

--
-- Structure de la table `classe1`
--

CREATE TABLE IF NOT EXISTS `classe1` (
  `num_serie` int(15) NOT NULL,
  `prix` int(11) NOT NULL,
  `produit` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_today` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `validite_ticket` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_fin` varchar(16) COLLATE latin1_general_ci NOT NULL,
  UNIQUE KEY `produit` (`num_serie`),
  UNIQUE KEY `produit_2` (`num_serie`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Contenu de la table `classe1`
--

INSERT INTO `classe1` (`num_serie`, `prix`, `produit`, `date_today`, `validite_ticket`, `date_fin`) VALUES
(209600, 2500, 'Billet 1 er clas', '23/06/2022 20:09', '120', '2022-06-30 20:09'),
(462147, 2500, 'Billet 1 er clas', '23/06/2022 18:42', '120', '2022-06-30 18:42'),
(1169513, 2500, 'Billet 1 er clas', '23/06/2022 15:28', '120', '2022-06-30 15:28'),
(1276096, 2500, 'Billet 1 er clas', '23/06/2022 20:07', '120', '2022-06-30 20:07'),
(1350456, 2500, 'Billet 1 er clas', '23/06/2022 20:06', '120', '2022-06-30 20:06'),
(1476576, 2500, 'Billet 1 er clas', '23/06/2022 20:11', '120', '2022-06-30 20:11'),
(1512481, 2500, 'Billet 1 er clas', '23/06/2022 19:58', '120', '2022-06-30 19:58'),
(1975905, 2500, 'Billet 1 er clas', '23/06/2022 20:06', '120', '2022-06-30 20:06');

-- --------------------------------------------------------

--
-- Structure de la table `zone1`
--

CREATE TABLE IF NOT EXISTS `zone1` (
  `num_serie` int(15) NOT NULL,
  `prix` int(11) NOT NULL,
  `produit` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_today` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `validite_ticket` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_fin` varchar(16) COLLATE latin1_general_ci NOT NULL,
  UNIQUE KEY `produit` (`num_serie`),
  UNIQUE KEY `produit_2` (`num_serie`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Contenu de la table `zone1`
--

INSERT INTO `zone1` (`num_serie`, `prix`, `produit`, `date_today`, `validite_ticket`, `date_fin`) VALUES
(54028, 500, 'Billet 2 eme cla', '23/06/2022 15:24', '120', '2022-06-30 15:24'),
(179239, 500, 'Billet 2 eme cla', '23/06/2022 15:24', '120', '2022-06-30 15:24');

-- --------------------------------------------------------

--
-- Structure de la table `zone2`
--

CREATE TABLE IF NOT EXISTS `zone2` (
  `num_serie` int(15) NOT NULL,
  `prix` int(11) NOT NULL,
  `produit` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_today` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `validite_ticket` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_fin` varchar(16) COLLATE latin1_general_ci NOT NULL,
  UNIQUE KEY `produit` (`num_serie`),
  UNIQUE KEY `produit_2` (`num_serie`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Contenu de la table `zone2`
--

INSERT INTO `zone2` (`num_serie`, `prix`, `produit`, `date_today`, `validite_ticket`, `date_fin`) VALUES
(209600, 1000, 'Billet 2 eme cla', '23/06/2022 20:09', '120', '2022-06-30 20:09'),
(227421, 1000, 'Billet 2 eme cla', '23/06/2022 18:43', '120', '2022-06-30 18:43'),
(575836, 1000, 'Billet 2 eme cla', '23/06/2022 15:08', '120', '2022-06-30 15:08'),
(587625, 1000, 'Billet 2 eme cla', '23/06/2022 15:27', '120', '2022-06-30 15:27'),
(831703, 1000, 'Billet 2 eme cla', '23/06/2022 20:07', '120', '2022-06-30 20:07'),
(1276096, 1000, 'Billet 2 eme cla', '23/06/2022 20:07', '120', '2022-06-30 20:07'),
(1678842, 1000, 'Billet 2 eme cla', '23/06/2022 20:11', '120', '2022-06-30 20:11'),
(1879611, 1000, 'Billet 2 eme cla', '23/06/2022 20:10', '120', '2022-06-30 20:10');

-- --------------------------------------------------------

--
-- Structure de la table `zone3`
--

CREATE TABLE IF NOT EXISTS `zone3` (
  `num_serie` int(15) NOT NULL,
  `prix` int(11) NOT NULL,
  `produit` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_today` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `validite_ticket` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `date_fin` varchar(16) COLLATE latin1_general_ci NOT NULL,
  UNIQUE KEY `produit` (`num_serie`),
  UNIQUE KEY `produit_2` (`num_serie`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Contenu de la table `zone3`
--

INSERT INTO `zone3` (`num_serie`, `prix`, `produit`, `date_today`, `validite_ticket`, `date_fin`) VALUES
(34515, 1500, 'Billet 2 eme cla', '23/06/2022 15:20', '120', '2022-06-30 15:20'),
(476282, 1500, 'Billet 2 eme cla', '23/06/2022 20:12', '120', '2022-06-30 20:12'),
(588639, 1500, 'Billet 2 eme cla', '23/06/2022 18:43', '120', '2022-06-30 18:43'),
(1007447, 1500, 'Billet 2 eme cla', '23/06/2022 20:07', '120', '2022-06-30 20:07'),
(1163267, 1500, 'Billet 2 eme cla', '23/06/2022 20:11', '120', '2022-06-30 20:11'),
(1164762, 1500, 'Billet 2 eme cla', '23/06/2022 20:12', '120', '2022-06-30 20:12'),
(1669553, 1500, 'Billet 2 eme cla', '23/06/2022 15:08', '120', '2022-06-30 15:08'),
(1857216, 1500, 'Billet 2 eme cla', '23/06/2022 15:21', '120', '2022-06-30 15:21');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
