DROP TABLE IF EXISTS size_by_prov_category;
CREATE TABLE size_by_prov_category
(
    id_size_by_prov_category serial NOT NULL,
    provincia VARCHAR(120),
    categoria VARCHAR(120),
    count integer,
    PRIMARY KEY (id_size_by_prov_category)
);