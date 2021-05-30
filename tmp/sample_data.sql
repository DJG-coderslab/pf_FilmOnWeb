INSERT INTO public.album_app_tperson (first_name,last_name) VALUES
	 ('Małgorzata','Szumowska'),
	 ('Krzysztof','Kieślowski'),
	 ('Andrzej','Wajda'),
	 ('Tadeusz','Konwicki'),
	 ('Krzysztof','Krauze'),
	 ('Andrzej','Munk'),
	 ('Krzysztof','Zanussi'),
	 ('Jerzy','Andrzejewski'),
	 ('Tadeusz','Chmielewski'),
	 ('Stanisław','Dygat');
INSERT INTO public.album_app_tperson (first_name,last_name) VALUES
	 ('Wiesław','Dymny'),
	 ('Jan','Hryniak'),
	 ('Wojciech','Zimiński');

INSERT INTO public.album_app_tgenre ("name") VALUES
	 ('horror'),
	 ('kryminał'),
	 ('dramat'),
	 ('przygodowy'),
	 ('dokumentalny'),
	 ('thriller');
	 
INSERT INTO public.album_app_tmovie (title,"year",rating,director_id,screenplay_id) VALUES
	 ('Trzeci',2005,7.7,12,13),
	 ('Drugi',1986,3.3,12,6);
	 

INSERT INTO public.album_app_moviesstars ("role",movie_id,person_id) VALUES
	 ('kucharz',1,7),
	 ('blacharz',1,3),
	 ('baron',2,3);
