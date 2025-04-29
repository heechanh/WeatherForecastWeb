CREATE TABLE tblFavoriteCity (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    CityName NVARCHAR(100)
)
INSERT INTO tblFavoriteCity (CityName) VALUES ('Hanoi');
INSERT INTO tblFavoriteCity (CityName) VALUES ('Da Nang');
INSERT INTO tblFavoriteCity (CityName) VALUES ('Ho Chi Minh City');
 
 select * from tblFavoriteCity