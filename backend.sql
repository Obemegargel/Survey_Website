CREATE DATABASE rateapartmentdb;

-- create apartment database
CREATE TABLE apartment (
    formID int NOT NULL AUTOINCREMENT,--autoincrement
    apartmentname string,
    stars int,
    semester string, --Fall, Spring, Summer, Winter but also has chance of listing multiple this will be the linking table
    year int,
    housing string, -- male female, married etc
    costsemester int,
    PRIMARY KEY (formID)--declare PRIMARY KEY
    

   ....
);

-- Do stuff to database
--INSERT
--1
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('Nauvoo House', 5, 'Fall', 2023, 'Mens', 1400);
--2
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('Bountiful Place', 1, 'Fall-Winter', 2020, 'Mens', 800);
--3
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('The Cove', 3, 'Winter', 2020, 'Womens', 975);
--3
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('Somerset', 3, 'Summer-Winter', 2022, 'Womens', 1015);
--4
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('Alpine-Chalet', 4, 'Spring', 2022, 'Married', 1000);
--5
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('Alpine-Chalet', 4, 'Fallen', 2022, 'Married', 1000);
--6
INSERT INTO apartment (apartmentname, stars, semester, year, housing, costsemester)
VALUES ('Bountiful Place', 1, 'Fall-Winter', 2020, 'Married', 800000);
--7
INSERT INTO apartment (apartmentname, semester, year, housing, costsemester)
VALUES ('other', 'Fall-Winter', 2020, 'Married', 800000);

--Modify
-- as far as I can tell this would be things like UPDATE etc. because I do not see 
-- anything that particularly says "Modify"
--for INSERT --6
UPDATE apartment
SET housing='Mens'
Where apartmentname='Bountiful Place';
--for INSERT --7
UPDATE apartment
SET apartmentname'This apartment does not exist, hahahahahah', housing='Mens', costsemester='30', stars='4'
Where apartmentname='other';

--Delete
DELETE FROM apartment WHERE semester = 'Fallen';

--Queries
SELECT * 
FROM apartment;
