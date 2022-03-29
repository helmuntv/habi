CREATE TABLE user_property_likes (
  id int(11) NOT NULL AUTO_INCREMENT,
  user_id int(10) NOT NULL,
  property_id int(10) NOT NULL,
  user_like int(1) default 0,
  CONSTRAINT user_property_likes_pk PRIMARY KEY (user_id, property_id)
  CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT property_id_fk FOREIGN KEY (property_id) REFERENCES property (id)
);

--Se crea tabla user_property_likes
--Se crea el campos id como identificador de la tabla
--Se crea campo user_id al cual se le crea un constraint de llave foranea a la tabla auth_user
--Se crea campo property_id al cual se le crea un constraint de llave foranea a la tabla property
--se crea el campo user_like para almacenar el valor de me gusta
--Se crean un constraint como llave primaria para identificar que un usuario solo pueda dar un me gusta a una propiedad
--de acuerdo con esto se podra hacer un conteo de me gusta por property_id y user_like