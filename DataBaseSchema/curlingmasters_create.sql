SET FOREIGN_KEY_CHECKS = 0;
CREATE OR replace SCHEMA team9;

USE team9;

CREATE TABLE CashFlow
(
  PaymentID      INT          NOT NULL AUTO_INCREMENT,
  Date           DATE         NOT NULL,
  Amount         DECIMAL(9,2) NOT NULL,
  PlayerID       INT          NULL    ,
  StaffID        INT          NULL    ,
  ItemID         INT          NULL    ,
  SponsorID      INT          NULL    ,
  OtherPaymentID INT          NULL    ,
  PRIMARY KEY (PaymentID)
);

ALTER TABLE CashFlow
  ADD CONSTRAINT UQ_PaymentID UNIQUE (PaymentID);

CREATE TABLE Info
(
  InfoID     INT                           NOT NULL AUTO_INCREMENT,
  FirstName  VARCHAR(128)                  NOT NULL,
  LastName   VARCHAR(128)                  NOT NULL,
  Address    VARCHAR(128)                  NOT NULL,
  JoinDate   DATE                          NOT NULL,
  DepartDate DATE                          NOT NULL,
  BirthDate  DATE                          NOT NULL,
  Email      VARCHAR(128)                  NOT NULL,
  Phone      VARCHAR(128)                  NOT NULL,
  Gender     ENUM('MALE','FEMALE','OTHER') NOT NULL,
  PRIMARY KEY (InfoID)
);

ALTER TABLE Info
  ADD CONSTRAINT UQ_InfoID UNIQUE (InfoID);

CREATE TABLE Items
(
  ItemID      INT          NOT NULL AUTO_INCREMENT,
  Size        VARCHAR(20)  NOT NULL,
  Description VARCHAR(128) NOT NULL,
  Price       DECIMAL(9,2) NOT NULL,
  Quantity    INT          NOT NULL,
  PRIMARY KEY (ItemID)
);

ALTER TABLE Items
  ADD CONSTRAINT UQ_ItemID UNIQUE (ItemID);

CREATE TABLE Matches
(
  MatchID    INT         NOT NULL AUTO_INCREMENT,
  Spectators INT         NULL    ,
  Season     VARCHAR(20) NOT NULL,
  Date       DATETIME    NOT NULL,
  ScoreA     INT         NULL    ,
  ScoreB     INT         NULL    ,
  TeamA      INT         NOT NULL,
  TeamB      INT         NOT NULL,
  PRIMARY KEY (MatchID)
);

ALTER TABLE Matches
  ADD CONSTRAINT UQ_MatchID UNIQUE (MatchID);

CREATE TABLE OtherCosts
(
  OtherPaymentID INT          NOT NULL AUTO_INCREMENT,
  Description    VARCHAR(128) NOT NULL,
  Periodic       BOOLEAN      NOT NULL,
  PRIMARY KEY (OtherPaymentID)
);

ALTER TABLE OtherCosts
  ADD CONSTRAINT UQ_OtherPaymentID UNIQUE (OtherPaymentID);

CREATE TABLE OutsideIncome
(
  SponsorID   INT          NOT NULL AUTO_INCREMENT,
  SponsorName VARCHAR(128) NOT NULL,
  Amount      DECIMAL(9,2) NOT NULL,
  StartDate   DATE         NOT NULL,
  EndDate     DATE         NOT NULL,
  PRIMARY KEY (SponsorID)
);

ALTER TABLE OutsideIncome
  ADD CONSTRAINT UQ_SponsorID UNIQUE (SponsorID);

CREATE TABLE PlayerMatchPerformance
(
  Effectiveness DECIMAL(8,2) NULL    ,
  Position      VARCHAR(128) NOT NULL,
  MatchID       INT          NOT NULL,
  PlayerID      INT          NOT NULL
);

CREATE TABLE Players
(
  PlayerID INT     NOT NULL AUTO_INCREMENT,
  TeamID   INT     NOT NULL,
  Active   BOOLEAN NOT NULL,
  InfoID   INT     NOT NULL,
  PRIMARY KEY (PlayerID)
);

ALTER TABLE Players
  ADD CONSTRAINT UQ_PlayerID UNIQUE (PlayerID);

CREATE TABLE Staff
(
  StaffID  INT          NOT NULL AUTO_INCREMENT,
  Position VARCHAR(128) NOT NULL,
  Active   BOOLEAN      NOT NULL,
  InfoID   INT          NOT NULL,
  PRIMARY KEY (StaffID)
);

ALTER TABLE Staff
  ADD CONSTRAINT UQ_StaffID UNIQUE (StaffID);

CREATE TABLE Teams
(
  TeamID      INT                        NOT NULL AUTO_INCREMENT,
  TeamName    VARCHAR(100)               NOT NULL,
  Type        ENUM('MALE','FEMALE')      NOT NULL,
  AgeCategory ENUM('JUNIORS', 'SENIORS') NOT NULL,
  PRIMARY KEY (TeamID)
);

ALTER TABLE Teams
  ADD CONSTRAINT UQ_TeamID UNIQUE (TeamID);

ALTER TABLE PlayerMatchPerformance
  ADD CONSTRAINT FK_Matches_TO_PlayerMatchPerformance
    FOREIGN KEY (MatchID)
    REFERENCES Matches (MatchID);

ALTER TABLE PlayerMatchPerformance
  ADD CONSTRAINT FK_Players_TO_PlayerMatchPerformance
    FOREIGN KEY (PlayerID)
    REFERENCES Players (PlayerID);

ALTER TABLE Staff
  ADD CONSTRAINT FK_Info_TO_Staff
    FOREIGN KEY (InfoID)
    REFERENCES Info (InfoID);

ALTER TABLE Players
  ADD CONSTRAINT FK_Info_TO_Players
    FOREIGN KEY (InfoID)
    REFERENCES Info (InfoID);

ALTER TABLE Matches
  ADD CONSTRAINT FK_Teams_TO_Matches
    FOREIGN KEY (TeamB)
    REFERENCES Teams (TeamID);

ALTER TABLE Matches
  ADD CONSTRAINT FK_Teams_TO_Matches1
    FOREIGN KEY (TeamA)
    REFERENCES Teams (TeamID);

ALTER TABLE Players
  ADD CONSTRAINT FK_Teams_TO_Players
    FOREIGN KEY (TeamID)
    REFERENCES Teams (TeamID);

ALTER TABLE CashFlow
  ADD CONSTRAINT FK_Players_TO_CashFlow
    FOREIGN KEY (PlayerID)
    REFERENCES Players (PlayerID);

ALTER TABLE CashFlow
  ADD CONSTRAINT FK_Staff_TO_CashFlow
    FOREIGN KEY (StaffID)
    REFERENCES Staff (StaffID);

ALTER TABLE CashFlow
  ADD CONSTRAINT FK_Items_TO_CashFlow
    FOREIGN KEY (ItemID)
    REFERENCES Items (ItemID);

ALTER TABLE CashFlow
  ADD CONSTRAINT FK_OutsideIncome_TO_CashFlow
    FOREIGN KEY (SponsorID)
    REFERENCES OutsideIncome (SponsorID);

ALTER TABLE CashFlow
  ADD CONSTRAINT FK_OtherCosts_TO_CashFlow
    FOREIGN KEY (OtherPaymentID)
    REFERENCES OtherCosts (OtherPaymentID);