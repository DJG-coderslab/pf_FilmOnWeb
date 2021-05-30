/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*!40000 ALTER TABLE "filmonweb_app_genre" DISABLE KEYS */;
INSERT INTO "filmonweb_app_genre" ("name") VALUES
	('horror'),
	('kryminał'),
	('dramat'),
	('przygodowy'),
	('dokumentalny'),
	('thriller'),
	('obyczajowy'),
	('wojenny'),
	('sensacyjny'),
	('psychologiczny');
/*!40000 ALTER TABLE "filmonweb_app_genre" ENABLE KEYS */;

/*!40000 ALTER TABLE "filmonweb_app_movie" DISABLE KEYS */;
INSERT INTO "filmonweb_app_movie" ("title", "year", "rating", "director_id", "screenplay_id") VALUES
	('Trzeci', 2005, 7.7, 12, 13);
	('Drugi', 1986, 3.3, 12, 6);
	('Pograbek', 1992, 8.8, 14, 14);
	('Psy', 1992, 7.9, 18, 18);
	('Psy 2. Ostatnia krew', 1994, 8.3, 18, 18);
	('Demony wojny według Goi', 1998, 8.5, 18, 18);
	('Bandyta', 1997, 9.8, 27, 28);
	('300 mil do nieba', 1989, 8.9, 27, 28);
	('Kroll', 1991, 7.8, 18, 18);
/*!40000 ALTER TABLE "filmonweb_app_movie" ENABLE KEYS */;

/*!40000 ALTER TABLE "filmonweb_app_movie_genre" DISABLE KEYS */;
INSERT INTO "filmonweb_app_movie_genre" ("movie_id", "genre_id") VALUES
	(3, 7),
	(1, 7),
	(4, 2),
	(4, 3),
	(5, 2),
	(6, 8),
	(6, 9),
	(6, 3),
	(7, 10),
	(7, 3),
	(7, 7),
	(8, 10),
	(8, 7),
	(9, 9),
	(9, 3);
/*!40000 ALTER TABLE "filmonweb_app_movie_genre" ENABLE KEYS */;

/*!40000 ALTER TABLE "filmonweb_app_person" DISABLE KEYS */;
INSERT INTO "filmonweb_app_person" ("first_name", "last_name") VALUES
	('Wiesław', 'Dymny'),
	('Jan', 'Hryniak'),
	('Wojciech', 'Zimiński'),
	('Małgorzata', 'Szumowska'),
	('Krzysztof', 'Kieślowski'),
	('Andrzej', 'Wajda'),
	('Tadeusz', 'Konwicki'),
	('Krzysztof', 'Krauz'),
	('Andrzej', 'Munk'),
	('Krzysztof', 'Zanussi'),
	('Jerzy', 'Andrzejewski'),
	('Tadeusz', 'Chmielewski'),
	('Stanisław', 'Dygat'),
	('Jan Jakub', 'Kolski'),
	('Grażyna', 'Błęcka-Kolska'),
	('Mariusz', 'Saniternik'),
	('Franciszek', 'Pieczka'),
	('Władysław', 'Pasikowski'),
	('Bogusław', 'Linda'),
	('Marek', 'Kondrat'),
	('Cezary', 'Pazura'),
	('Artur', 'Zmijewski'),
	('Magdalena', 'Dourian'),
	('Tadeusz', 'Huk'),
	('Mirosław', 'Baka'),
	('Olaf', 'Lubaszenko'),
	('Maciej', 'Dejczer'),
	('Cezary', 'Harasimowicz'),
	('Til', 'Schweiger'),
	('Polly', 'Walker'),
	('Ida', 'Jabłońska'),
	('Wojciech', 'Klata'),
	('Adrianna', 'biedrzyńska'),
	('Jadwiga', 'Jankowska-Cieślak'),
	('Andrzej', 'Mellin'),
	('Rafał', 'Zimowski'),
	('Dariusz', 'Kordek'),
	('Maciej', 'Kozłowski'),
	('Ewa', 'Bukowska'),
	('Agnieszka', 'Różańska');
/*!40000 ALTER TABLE "filmonweb_app_person" ENABLE KEYS */;

/*!40000 ALTER TABLE "filmonweb_app_personmovie" DISABLE KEYS */;
INSERT INTO "filmonweb_app_personmovie" ("role", "movie_id", "person_id") VALUES
	('kucharz', 1, 7),
	('blacharz', 1, 3),
	('baron', 2, 3),
	('Kaczuba', 3, 17),
	('Kuśtyczka', 3, 15),
	('Waldemar Morawiec', 4, 21),
	('Franciszek Mauer', 4, 19),
	('Franciszek Mauer', 5, 19),
	('Radosław Wolf', 5, 22),
	('Nadia', 5, 23),
	('mjr Edward Keller', 6, 19),
	('mjr Czesław Kusz', 6, 24),
	('por. Czacki', 6, 26),
	('plut. Cichy', 6, 25),
	('Brut', 7, 29),
	('Mara', 7, 30),
	('Elena', 7, 31),
	('Grześ Kwiatkowski', 8, 32),
	('Jędrek Kwiatkowski', 8, 36),
	('Tadeusz Kwiatkowski, ojciec', 8, 35),
	('Barbara Kwiatkowska, matka', 8, 34),
	('dziennikarka', 8, 33),
	('Marcin Kroll', 9, 26),
	('por. Arek', 9, 19),
	('Kuba Berger', 9, 37),
	('kapral Edward Wiaderny', 9, 21),
	('kapitan', 9, 38),
	('Agata, żona Krolla', 9, 39),
	('Marta, siostra Krolla', 9, 40);
/*!40000 ALTER TABLE "filmonweb_app_personmovie" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
