DROP SCHEMA IF EXISTS `playertrack`;

CREATE SCHEMA `playertrack`;

use `playertrack`;


DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_first_name` varchar(45) NOT NULL,
  `player_last_name` varchar(45) NOT NULL,
  `birth_date` date NOT NULL,
  `nationality` varchar(45) NOT NULL,
  `club_name` varchar(45) DEFAULT NULL,
  `number_player` int(2) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  
   PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `matches`;
CREATE TABLE `matches` (
  `match_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_team` varchar(45) NOT NULL,
  `second_team` varchar(45) NOT NULL,
  `match_date` date NOT NULL,
  `stadium` varchar(45) NOT NULL,
  `result` varchar(45) NOT NULL,
  
   PRIMARY KEY (`match_id`)
   
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
  
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
   `video_id` int(11) NOT NULL AUTO_INCREMENT,
   `video_name` varchar(255) DEFAULT NULL UNIQUE,
   `id_match` int(11) DEFAULT NULL,

   PRIMARY KEY(`video_id`),
   KEY `FK_DETAIL_idx` (`id_match`),
   CONSTRAINT `FK_Match_ID` FOREIGN KEY (`id_match`) REFERENCES `matches` (`match_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `performance_player`;
CREATE TABLE `performance_player` (
  `performance_player_id` int(11) NOT NULL AUTO_INCREMENT,
  `id_player` int(11) DEFAULT NULL,
  `id_match` int(11) DEFAULT NULL,
  `distance_covered` float(20) DEFAULT NULL,
  `avg_speed` float(20) DEFAULT NULL,
  
  PRIMARY KEY (`performance_player_id`),
  
  KEY `FK_PLAYER_idx` (`id_player`),
  
  CONSTRAINT `FK_PLAYER_PERFORMANCE` FOREIGN KEY (`id_player`) 
  REFERENCES `player` (`player_id`) 
  ON DELETE NO ACTION ON UPDATE NO ACTION,
  
  CONSTRAINT `FK_MATCH_PERFORMANCE` FOREIGN KEY (`id_match`) 
  REFERENCES `matches` (`match_id`) 
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


SELECT id_player
FROM performance_player
LEFT OUTER JOIN player
ON performance_player.id_player = player.player_id;


SELECT match_id
FROM performance_player
LEFT OUTER JOIN matches
ON performance_player.id_match = matches.match_id;



DROP TABLE IF EXISTS `coordinates_player`;
CREATE TABLE `coordinates_player` (
  `coordinates_player_id` int(11) NOT NULL AUTO_INCREMENT,
  `id_player` int(11) DEFAULT NULL,
  `id_match` int(11) DEFAULT NULL,
  `x_coordinate` int(8) DEFAULT NULL,
  `y_coordinate` int(8) DEFAULT NULL,
  `current_frame` int(4) DEFAULT NULL,
  
  PRIMARY KEY (`coordinates_player_id`),
  
  KEY `FK_PLAYER_idx` (`id_player`),
  
  CONSTRAINT `FK_PLAYER_COORDINATES` FOREIGN KEY (`id_player`) 
  REFERENCES `player` (`player_id`) 
  ON DELETE NO ACTION ON UPDATE NO ACTION,
  
  CONSTRAINT `FK_MATCH_COORDINATES` FOREIGN KEY (`id_match`) 
  REFERENCES `matches` (`match_id`) 
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



SELECT id_player
FROM coordinates_player
LEFT OUTER JOIN player
ON coordinates_player.id_player = player.player_id;


SELECT match_id
FROM coordinates_player
LEFT OUTER JOIN matches
ON coordinates_player.id_match = matches.match_id;





 












