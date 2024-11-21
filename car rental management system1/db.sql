creATE database db3;
use db3;

-- Create the table to store car details
CREATE TABLE cars (
    id VARCHAR(10) PRIMARY KEY,
    model VARCHAR(45) NOT NULL,
    brand VARCHAR(30) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,  -- Assuming price is in decimal format
    availability BOOLEAN NOT NULL DEFAULT TRUE  -- To indicate if the car is available for rental
);

-- Insert sample data into the cars table
INSERT INTO cars VALUES ('c001', 'Toyota Camry', 'Toyota', 45.00,true);
INSERT INTO cars VALUES ('c002', 'Honda Accord', 'Honda', 50.00,false);
INSERT INTO cars VALUES ('c003', 'Ford Mustang', 'Ford', 75.00,true);

-- Select all records from the cars table
SELECT * FROM cars;