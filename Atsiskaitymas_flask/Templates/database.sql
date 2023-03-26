CREATE TABLE users (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password CHAR(60) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE groups (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  creator_email VARCHAR(255) NOT NULL,
  active TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  FOREIGN KEY (creator_email) REFERENCES users(email)
);

CREATE TABLE bills (
  id INT(11) NOT NULL AUTO_INCREMENT,
  amount DECIMAL(10,2) NOT NULL,
  group_id INT(11) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (group_id) REFERENCES groups(id)
);

INSERT INTO users (name, email, password) VALUES ('Jonas Jonaitis', 'jonas@mail.com', 'password123')
