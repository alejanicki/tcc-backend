use tcc;

create table `address` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    zip_code varchar(8) NOT NULL,
    street_name varchar(255) NOT NULL,
    state_user varchar(2) NOT NULL,
    city varchar(255) NOT NULL,
    neighborhood varchar(255) NOT NULL,
    address_number varchar(5) NOT NULL,
    complement varchar(255),
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `user` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    id_address BIGINT,
    name_user varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    date_birth date NOT NULL,
    cpf varchar(11) NOT NULL UNIQUE,
    cellphone varchar(30) NOT NULL,
    email varchar(30) NOT NULL UNIQUE,
    password_user varchar(255) NOT NULL,
    Credit BIGINT,
    terms_conditions boolean,
    PRIMARY KEY (id),
    FOREIGN KEY (id_address) REFERENCES `address`(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `prizes` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name_prize varchar(255) NOT NULL,
    cost BIGINT NOT NULL,
    description_prize varchar(255) NOT NULL,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `trade` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    date_trade date NOT NULL,
    id_user BIGINT,
    id_prize BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES `user`(id),
    FOREIGN KEY (id_prize) REFERENCES `prizes`(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `battery` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    type_battery varchar(4) NOT NULL,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `transaction` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    date_transaction date NOT NULL,
    id_user BIGINT,
    earn BIGINT,
    id_battery BIGINT,
    number_of_batteries BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES `user`(id),
    FOREIGN KEY (id_battery) REFERENCES `battery`(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;