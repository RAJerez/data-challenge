DROP TABLE IF EXISTS size_by_datasource;
CREATE TABLE size_by_datasource
(
    id_size_by_datasource serial NOT NULL,
    source VARCHAR(200),
    count integer,
    PRIMARY KEY (id_size_by_datasource)
);