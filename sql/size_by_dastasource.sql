DROP TABLE IF EXISTS size_by_datasource;
CREATE TABLE size_by_datasource
(
    id_size_by_datasource serial NOT NULL,
    fuente VARCHAR(200),
    cantidad integer,
    job_date date,
    PRIMARY KEY (id_size_by_datasource)
);