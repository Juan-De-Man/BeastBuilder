
CREATE TABLE Dagschema
(
  dagid       INT      NOT NULL AUTO_INCREMENT,
  schemanr    int      NOT NULL,
  gepland     DATE     NULL    ,
  oefnr       int      NOT NULL,
  aantal      int      NULL    ,
  rust        int      NULL    ,
  herhalingen int      NULL    ,
  uitgevoerd  DATETIME NULL    ,
  PRIMARY KEY (dagid)
);

CREATE TABLE Ervaring
(
  ervaringsgraad int         NOT NULL,
  naam           VARCHAR(50) NOT NULL,
  PRIMARY KEY (ervaringsgraad)
);

CREATE TABLE Gemeente
(
  gemeenteid int         NOT NULL AUTO_INCREMENT,
  postcode   VARCHAR(10) NOT NULL,
  naam       VARCHAR(60) NULL    ,
  PRIMARY KEY (gemeenteid)
);

CREATE TABLE Klant
(
  lidnr          int          NOT NULL AUTO_INCREMENT,
  Naam           VARCHAR(50)  NOT NULL,
  vnaam          VARCHAR(50)  NOT NULL,
  geboortejaar   DATE         NOT NULL,
  gewicht        FLOAT        NOT NULL,
  lengte         int          NOT NULL,
  ervaringsgraad int          NOT NULL,
  telnummer      VARCHAR(20)  NULL    ,
  lidstart       DATETIME     NULL    ,
  lidstop        DATETIME     NULL    ,
  gemeenteid     int          NOT NULL,
  straat         VARCHAR(100) NULL    ,
  huisnummer     VARCHAR(10)  NULL    ,
  email          VARCHAR(100) NULL    ,
  PRIMARY KEY (lidnr)
);

CREATE TABLE Oefening
(
  oefnr              int          NOT NULL,
  naam               VARCHAR(50)  NOT NULL,
  moeilijkheidsgraad VARCHAR(5)   NOT NULL,
  beschrijving       VARCHAR(3000) NULL    ,
  instructie         VARCHAR(3000) NULL    ,
  PRIMARY KEY (oefnr)
);

CREATE TABLE Trainingschema
(
  schemanr int         NOT NULL AUTO_INCREMENT,
  naam     VARCHAR(50) NULL    ,
  lidnr    int         NOT NULL,
  startdat DATE        NULL    ,
  einddat  DATE        NULL    ,
  PRIMARY KEY (schemanr)
);

ALTER TABLE Trainingschema
  ADD CONSTRAINT FK_Klant_TO_Trainingschema
    FOREIGN KEY (lidnr)
    REFERENCES Klant (lidnr);

ALTER TABLE Dagschema
  ADD CONSTRAINT FK_Trainingschema_TO_Dagschema
    FOREIGN KEY (schemanr)
    REFERENCES Trainingschema (schemanr);

ALTER TABLE Klant
  ADD CONSTRAINT FK_Gemeente_TO_Klant
    FOREIGN KEY (gemeenteid)
    REFERENCES Gemeente (gemeenteid);

ALTER TABLE Klant
  ADD CONSTRAINT FK_Ervaring_TO_Klant
    FOREIGN KEY (ervaringsgraad)
    REFERENCES Ervaring (ervaringsgraad);

ALTER TABLE Dagschema
  ADD CONSTRAINT FK_Oefening_TO_Dagschema
    FOREIGN KEY (oefnr)
    REFERENCES Oefening (oefnr);
