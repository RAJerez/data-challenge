DROP TABLE IF EXISTS size_by_category;
CREATE TABLE size_by_category
(
    id_size_by_category serial NOT NULL,
    categoria VARCHAR(120),
    cantidad integer,
    job_date date,
    PRIMARY KEY (id_size_by_category)
);