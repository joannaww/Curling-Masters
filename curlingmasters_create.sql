SET FOREIGN_KEY_CHECKS = 0;
CREATE OR replace SCHEMA CurlingMasters;

USE CurlingMasters;

CREATE TABLE FutureMatches
(
  FutureID INT      NOT NULL AUTO_INCREMENT,
  Date     DATETIME NOT NULL,
  Team1ID  INT      NOT NULL,
  Team2ID  INT      NOT NULL,
  PRIMARY KEY (FutureID)
);

ALTER TABLE FutureMatches
  ADD CONSTRAINT UQ_FutureID UNIQUE (FutureID);

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

CREATE TABLE ItemCosts
(
  PaymentID INT          NOT NULL AUTO_INCREMENT,
  Date      DATE         NOT NULL,
  Amount    DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (PaymentID)
);

ALTER TABLE ItemCosts
  ADD CONSTRAINT UQ_PaymentID UNIQUE (PaymentID);

CREATE TABLE Items
(
  ItemID    INT          NOT NULL AUTO_INCREMENT,
  Size      VARCHAR(20)  NOT NULL,
  Type      VARCHAR(128) NOT NULL,
  Broken    BOOLEAN      NOT NULL,
  PaymentID INT          NOT NULL,
  PRIMARY KEY (ItemID)
);

ALTER TABLE Items
  ADD CONSTRAINT UQ_ItemID UNIQUE (ItemID);

CREATE TABLE MatchesPlayed
(
  MatchID      INT          NOT NULL AUTO_INCREMENT,
  TicketSales  DECIMAL(8,2) NOT NULL,
  Season       VARCHAR(20)  NOT NULL,
  Date         DATETIME     NOT NULL,
  Score        VARCHAR(20)  NOT NULL,
  WinnerTeamID INT          NOT NULL,
  LoserTeamID  INT          NOT NULL,
  PRIMARY KEY (MatchID)
);

ALTER TABLE MatchesPlayed
  ADD CONSTRAINT UQ_MatchID UNIQUE (MatchID);

CREATE TABLE OtherCosts
(
  OtherPaymentID INT          NOT NULL AUTO_INCREMENT,
  Date           DATE         NOT NULL,
  Amount         DECIMAL(8,2) NOT NULL,
  Description    VARCHAR(128) NOT NULL,
  PRIMARY KEY (OtherPaymentID)
);

ALTER TABLE OtherCosts
  ADD CONSTRAINT UQ_OtherPaymentID UNIQUE (OtherPaymentID);

CREATE TABLE OutsideIncome
(
  IncomeID INT                   NOT NULL AUTO_INCREMENT,
  Amount   DECIMAL(8,2)          NOT NULL,
  Source   ENUM('Private','Gov') NOT NULL,
  Date     DATE                  NOT NULL,
  PRIMARY KEY (IncomeID)
);

ALTER TABLE OutsideIncome
  ADD CONSTRAINT UQ_IncomeID UNIQUE (IncomeID);

CREATE TABLE Players
(
  PlayerID INT NOT NULL AUTO_INCREMENT,
  TeamID   INT NOT NULL,
  InfoID   INT NOT NULL,
  PRIMARY KEY (PlayerID)
);

ALTER TABLE Players
  ADD CONSTRAINT UQ_PlayerID UNIQUE (PlayerID);

CREATE TABLE PlayerTuition
(
  TuitionID INT          NOT NULL AUTO_INCREMENT,
  Date      DATETIME     NOT NULL,
  Amount    DECIMAL(8,2) NOT NULL,
  PlayerID  INT          NOT NULL,
  PRIMARY KEY (TuitionID)
);

ALTER TABLE PlayerTuition
  ADD CONSTRAINT UQ_TuitionID UNIQUE (TuitionID);

CREATE TABLE Salaries
(
  SalaryID   INT          NOT NULL AUTO_INCREMENT,
  Date       DATE         NOT NULL,
  Amount     DECIMAL(8,2) NOT NULL,
  EmployeeID INT          NOT NULL,
  PRIMARY KEY (SalaryID)
);

ALTER TABLE Salaries
  ADD CONSTRAINT UQ_SalaryID UNIQUE (SalaryID);

CREATE TABLE Staff
(
  EmployeeID INT          NOT NULL AUTO_INCREMENT,
  Position   VARCHAR(128) NOT NULL,
  InfoID     INT          NOT NULL,
  PRIMARY KEY (EmployeeID)
);

ALTER TABLE Staff
  ADD CONSTRAINT UQ_EmployeeID UNIQUE (EmployeeID);

CREATE TABLE Teams
(
  TeamID   INT                   NOT NULL AUTO_INCREMENT,
  TeamName VARCHAR(100)          NOT NULL,
  Type     ENUM('MALE','FEMALE') NOT NULL,
  PRIMARY KEY (TeamID)
);

ALTER TABLE Teams
  ADD CONSTRAINT UQ_TeamID UNIQUE (TeamID);

ALTER TABLE Teams
  ADD CONSTRAINT UQ_TeamName UNIQUE (TeamName);

ALTER TABLE FutureMatches
  ADD CONSTRAINT FK_Teams_TO_FutureMatches
    FOREIGN KEY (Team1ID)
    REFERENCES Teams (TeamID);

ALTER TABLE FutureMatches
  ADD CONSTRAINT FK_Teams_TO_FutureMatches1
    FOREIGN KEY (Team2ID)
    REFERENCES Teams (TeamID);

ALTER TABLE MatchesPlayed
  ADD CONSTRAINT FK_Teams_TO_MatchesPlayed
    FOREIGN KEY (WinnerTeamID)
    REFERENCES Teams (TeamID);

ALTER TABLE MatchesPlayed
  ADD CONSTRAINT FK_Teams_TO_MatchesPlayed1
    FOREIGN KEY (LoserTeamID)
    REFERENCES Teams (TeamID);

ALTER TABLE Players
  ADD CONSTRAINT FK_Teams_TO_Players
    FOREIGN KEY (TeamID)
    REFERENCES Teams (TeamID);

ALTER TABLE PlayerTuition
  ADD CONSTRAINT FK_Players_TO_PlayerTuition
    FOREIGN KEY (PlayerID)
    REFERENCES Players (PlayerID);

ALTER TABLE Players
  ADD CONSTRAINT FK_Info_TO_Players
    FOREIGN KEY (InfoID)
    REFERENCES Info (InfoID);

ALTER TABLE Staff
  ADD CONSTRAINT FK_Info_TO_Staff
    FOREIGN KEY (InfoID)
    REFERENCES Info (InfoID);

ALTER TABLE Salaries
  ADD CONSTRAINT FK_Staff_TO_Salaries
    FOREIGN KEY (EmployeeID)
    REFERENCES Staff (EmployeeID);

ALTER TABLE Items
  ADD CONSTRAINT FK_ItemCosts_TO_Items
    FOREIGN KEY (PaymentID)
    REFERENCES ItemCosts (PaymentID);
