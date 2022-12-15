-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : jeu. 15 déc. 2022 à 19:15
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `CHU_Caen`
--
CREATE DATABASE IF NOT EXISTS `CHU_Caen` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `CHU_Caen`;

-- --------------------------------------------------------

--
-- Structure de la table `Archive`
--

CREATE TABLE `Archive` (
  `id_resident` varchar(200) NOT NULL,
  `date_entree` date DEFAULT NULL,
  `date_sortie` date DEFAULT NULL,
  `CDD_CDI` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `Archive`
--

INSERT INTO `Archive` (`id_resident`, `date_entree`, `date_sortie`, `CDD_CDI`) VALUES
('Patient-ASTIER-Alexandre-O+', '2022-12-15', NULL, NULL),
('Patient-DENIER-Charlie-A+', '2021-09-01', NULL, NULL),
('Patient-DESBOIS-Julie-A+', '2022-12-13', '2022-12-15', NULL),
('Patient-EDOUARD-Jean-A+', '2022-12-01', '2022-12-02', NULL),
('Patient-FREEMAN-Morgan-Z-', '2022-12-24', '2023-01-01', NULL),
('Patient-KJZEAIE-zapoeapoe-B-', '2022-09-09', '2022-10-10', NULL),
('Patient-ZOUITEN-Guinel-O+', '2022-11-06', NULL, NULL),
('RH-DFITUQDL-eqmlziemlq', '2018-12-15', '2030-12-15', 'CDD'),
('RH-DUJARDIN-Jean', '2000-12-01', '2023-09-12', 'CDD'),
('RH-LECAROSIER-michel', '2022-12-15', '2023-12-15', 'CDI'),
('RH-LEPISTOUILLEUR-Phillipe', '2000-12-15', NULL, 'CDI'),
('RH-Leroy-François', '2018-07-18', '2022-02-05', 'CDI'),
('RH-Theroulde-Jean-Baptiste', '2020-08-27', '2020-09-27', 'CDD'),
('RH-Vauthier-Antoine', '2022-01-01', NULL, 'CDI');

-- --------------------------------------------------------

--
-- Structure de la table `Patient`
--

CREATE TABLE `Patient` (
  `id_patient` varchar(200) NOT NULL,
  `nom` varchar(200) NOT NULL,
  `prenom` varchar(200) NOT NULL,
  `is_in_hospital` tinyint(1) DEFAULT NULL,
  `groupe_sanguin` varchar(3) NOT NULL,
  `age` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `Patient`
--

INSERT INTO `Patient` (`id_patient`, `nom`, `prenom`, `is_in_hospital`, `groupe_sanguin`, `age`) VALUES
('Patient-ASTIER-Alexandre-O+', 'astier', 'Alexandre', 1, 'O+', 40),
('Patient-DENIER-Charlie-A+', 'DENIER', 'Charlie', 0, 'A+', 25),
('Patient-DESBOIS-Julie-A+', 'DESBOIS', 'Julie', 0, 'A+', 24),
('Patient-EDOUARD-Jean-A+', 'EDOUARD', 'Jean', 0, 'A+', 77),
('Patient-FREEMAN-Morgan-Z-', 'FREEMAN', 'Morgan', 0, 'Z-', 77),
('Patient-KJZEAIE-zapoeapoe-B-', 'kjzeaie', 'zapoeapoe', 0, 'B-', 50),
('Patient-ZOUITEN-Guinel-O+', 'ZOUITEN', 'Guinel', 1, 'O+', 25),
('PatientLEPISTOUYEUR-PhillipeAB+', 'lepistouyeur', 'Phillipe', 1, 'AB+', 31);

-- --------------------------------------------------------

--
-- Structure de la table `Rh`
--

CREATE TABLE `Rh` (
  `id_rh` varchar(200) NOT NULL,
  `nom` varchar(200) NOT NULL,
  `prenom` varchar(200) NOT NULL,
  `salaire` int NOT NULL,
  `working_at_hospital` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `Rh`
--

INSERT INTO `Rh` (`id_rh`, `nom`, `prenom`, `salaire`, `working_at_hospital`) VALUES
('RH-DFITUQDL-eqmlziemlq', 'DFITUQDL', 'eqmlziemlq', 1000, 1),
('RH-DUJARDIN-Jean', 'DUJARDIN', 'Jean', 8000, 1),
('RH-LECAROSIER-michel', 'LECAROSIER', 'michel', 6163, 0),
('RH-LEPISTOUILLEUR-Phillipe', 'lepistouilleur', 'Phillipe', 10000, 1),
('RH-Leroy-François', 'Leroy', 'François', 3000, 0),
('RH-Theroulde-Jean-Baptiste', 'Theroulde', 'Jean-Baptiste', 3500, 1),
('RH-Vauthier-Antoine', 'Vauthier', 'Antoine', 4500, 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Archive`
--
ALTER TABLE `Archive`
  ADD PRIMARY KEY (`id_resident`);

--
-- Index pour la table `Patient`
--
ALTER TABLE `Patient`
  ADD PRIMARY KEY (`id_patient`);

--
-- Index pour la table `Rh`
--
ALTER TABLE `Rh`
  ADD PRIMARY KEY (`id_rh`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
