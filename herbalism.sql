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
-- Table structure for table `Herbs`
--

DROP TABLE IF EXISTS `Herbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Herbs` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `seasonId` int(6) unsigned DEFAULT NULL,
  `climateId` int(6) unsigned DEFAULT NULL,
  `localeId` int(6) unsigned DEFAULT NULL,
  `rarityId` int(6) unsigned DEFAULT NULL,
  `cost` varchar(30) NOT NULL,
  `effect` text,
  `visual` text,
  `lore` text,
  `world` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Herbs`
--

LOCK TABLES `Herbs` WRITE;
/*!40000 ALTER TABLE `Herbs` DISABLE KEYS */;
INSERT INTO `Herbs` VALUES (2,'Test',0,0,0,0,'Testa',NULL,NULL,NULL,NULL),(3,'testaaa',0,0,0,0,'aaaaa',NULL,NULL,NULL,NULL),(4,'testaaa',0,0,0,0,'aaaaa',NULL,NULL,NULL,NULL),(5,'testaaa',0,0,0,0,'aaaaa',NULL,NULL,NULL,NULL);
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
  `herbId` int(6) unsigned DEFAULT NULL,
  `potionId` int(6) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HerbsPotions`
--

LOCK TABLES `HerbsPotions` WRITE;
/*!40000 ALTER TABLE `HerbsPotions` DISABLE KEYS */;
/*!40000 ALTER TABLE `HerbsPotions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-23 21:54:18
