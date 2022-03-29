CREATE TABLE user_property_likes (
  id int(11) NOT NULL AUTO_INCREMENT,
  user_id int(10) NOT NULL,
  property_id int(10) NOT NULL,
  user_like int(1) default 0,
  CONSTRAINT user_property_likes_pk PRIMARY KEY (user_id, property_id)
  CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT property_id_fk FOREIGN KEY (property_id) REFERENCES property (id)
);

--Se genera una una llave foranea entre 