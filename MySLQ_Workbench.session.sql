CREATE TABLE User (
    Username varchar(255), --USER Adjusted data type and added length
    password varchar(50), --USER
    Name varchar(255), -- USER-Adjusted data type and added length
    PRIMARY KEY(Username) --USER
);

CREATE TABLE Ingredients(
    Ingredient_Name varchar(200), --YOLO-Ingredient name from yolo/user 
    Number_of_days_left int,  --USER-input number of days left from user
    PRIMARY KEY(Ingredient_Name)
);

CREATE TABLE Recipes ( --if we are looking into recicpes 
    Recipe_id INT AUTO_INCREMENT,
    Recipe_name VARCHAR(500),
    PRIMARY KEY (Recipe_id)
);


Select * from ingredients;