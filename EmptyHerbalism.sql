-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: herbalism
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.10.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Climate`
--

DROP TABLE IF EXISTS `Climate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Climate` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Climate`
--

LOCK TABLES `Climate` WRITE;
/*!40000 ALTER TABLE `Climate` DISABLE KEYS */;
/*!40000 ALTER TABLE `Climate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ExpDate`
--

DROP TABLE IF EXISTS `ExpDate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ExpDate` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ExpDate`
--

LOCK TABLES `ExpDate` WRITE;
/*!40000 ALTER TABLE `ExpDate` DISABLE KEYS */;
/*!40000 ALTER TABLE `ExpDate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Herbs`
--

DROP TABLE IF EXISTS `Herbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Herbs` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `climateId` int(6) unsigned DEFAULT NULL,
  `rarityId` int(6) unsigned DEFAULT NULL,
  `ingestionId` int(6) unsigned DEFAULT NULL,
  `cost` int(6) DEFAULT NULL,
  `effect` text,
  `visual` text,
  `lore` text,
  `world` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `climateId` (`climateId`),
  KEY `rarityId` (`rarityId`),
  KEY `ingestionId` (`ingestionId`),
  CONSTRAINT `Herbs_ibfk_1` FOREIGN KEY (`climateId`) REFERENCES `Climate` (`id`),
  CONSTRAINT `Herbs_ibfk_2` FOREIGN KEY (`rarityId`) REFERENCES `Rarity` (`id`),
  CONSTRAINT `Herbs_ibfk_3` FOREIGN KEY (`ingestionId`) REFERENCES `Ingestion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Herbs`
--

LOCK TABLES `Herbs` WRITE;
/*!40000 ALTER TABLE `Herbs` DISABLE KEYS */;
/*!40000 ALTER TABLE `Herbs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HerbsPotions`
--

DROP TABLE IF EXISTS `HerbsPotions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HerbsPotions` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `herbId` int(6) unsigned NOT NULL,
  `potionId` int(6) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `herbId` (`herbId`),
  KEY `potionId` (`potionId`),
  CONSTRAINT `HerbsPotions_ibfk_1` FOREIGN KEY (`herbId`) REFERENCES `Herbs` (`id`),
  CONSTRAINT `HerbsPotions_ibfk_2` FOREIGN KEY (`potionId`) REFERENCES `Potions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HerbsPotions`
--

LOCK TABLES `HerbsPotions` WRITE;
/*!40000 ALTER TABLE `HerbsPotions` DISABLE KEYS */;
/*!40000 ALTER TABLE `HerbsPotions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HerbsSeasons`
--

DROP TABLE IF EXISTS `HerbsSeasons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HerbsSeasons` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `herbId` int(6) unsigned NOT NULL,
  `seasonId` int(6) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `herbId` (`herbId`),
  KEY `seasonId` (`seasonId`),
  CONSTRAINT `HerbsSeasons_ibfk_1` FOREIGN KEY (`herbId`) REFERENCES `Herbs` (`id`),
  CONSTRAINT `HerbsSeasons_ibfk_2` FOREIGN KEY (`seasonId`) REFERENCES `Season` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HerbsSeasons`
--

LOCK TABLES `HerbsSeasons` WRITE;
/*!40000 ALTER TABLE `HerbsSeasons` DISABLE KEYS */;
/*!40000 ALTER TABLE `HerbsSeasons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ingestion`
--

DROP TABLE IF EXISTS `Ingestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Ingestion` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ingestion`
--

LOCK TABLES `Ingestion` WRITE;
/*!40000 ALTER TABLE `Ingestion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ingestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PotionType`
--

DROP TABLE IF EXISTS `PotionType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PotionType` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PotionType`
--

LOCK TABLES `PotionType` WRITE;
/*!40000 ALTER TABLE `PotionType` DISABLE KEYS */;
/*!40000 ALTER TABLE `PotionType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Potions`
--

DROP TABLE IF EXISTS `Potions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Potions` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `cost` int(6) unsigned NOT NULL,
  `rarityId` int(6) unsigned DEFAULT NULL,
  `expDateId` int(6) unsigned DEFAULT NULL,
  `typeId` int(6) unsigned DEFAULT NULL,
  `ingestionId` int(6) unsigned DEFAULT NULL,
  `brewing` text,
  `storing` text,
  `effect` text,
  `visual` text,
  `lore` text,
  `world` varchar(40) DEFAULT NULL,
  `symptomId` int(6) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rarityId` (`rarityId`),
  KEY `expDateId` (`expDateId`),
  KEY `typeId` (`typeId`),
  KEY `ingestionId` (`ingestionId`),
  KEY `symptomId` (`symptomId`),
  CONSTRAINT `Potions_ibfk_1` FOREIGN KEY (`rarityId`) REFERENCES `Rarity` (`id`),
  CONSTRAINT `Potions_ibfk_2` FOREIGN KEY (`expDateId`) REFERENCES `ExpDate` (`id`),
  CONSTRAINT `Potions_ibfk_3` FOREIGN KEY (`typeId`) REFERENCES `PotionType` (`id`),
  CONSTRAINT `Potions_ibfk_4` FOREIGN KEY (`ingestionId`) REFERENCES `Ingestion` (`id`),
  CONSTRAINT `Potions_ibfk_5` FOREIGN KEY (`symptomId`) REFERENCES `SpecSymptom` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Potions`
--

LOCK TABLES `Potions` WRITE;
/*!40000 ALTER TABLE `Potions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Potions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rarity`
--

DROP TABLE IF EXISTS `Rarity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rarity` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rarity`
--

LOCK TABLES `Rarity` WRITE;
/*!40000 ALTER TABLE `Rarity` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rarity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Season`
--

DROP TABLE IF EXISTS `Season`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Season` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Season`
--

LOCK TABLES `Season` WRITE;
/*!40000 ALTER TABLE `Season` DISABLE KEYS */;
/*!40000 ALTER TABLE `Season` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SpecSymptom`
--

DROP TABLE IF EXISTS `SpecSymptom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SpecSymptom` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `symptomId` int(6) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `symptomId` (`symptomId`),
  CONSTRAINT `SpecSymptom_ibfk_1` FOREIGN KEY (`symptomId`) REFERENCES `Symptom` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SpecSymptom`
--

LOCK TABLES `SpecSymptom` WRITE;
/*!40000 ALTER TABLE `SpecSymptom` DISABLE KEYS */;
/*!40000 ALTER TABLE `SpecSymptom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Symptom`
--

DROP TABLE IF EXISTS `Symptom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Symptom` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Symptom`
--

LOCK TABLES `Symptom` WRITE;
/*!40000 ALTER TABLE `Symptom` DISABLE KEYS */;
/*!40000 ALTER TABLE `Symptom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-03 17:32:23
