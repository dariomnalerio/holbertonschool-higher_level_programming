-- creates the table id_not_null
CREATE TABLE IF NOT EXISTS unique_id (
    id int UNIQUE DEFAULT 1,
    name VARCHAR(256)
);