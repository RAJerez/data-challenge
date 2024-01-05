DROP TABLE IF EXISTS cine_insights;
CREATE TABLE cine_insights
(
    id_cine_insights serial NOT NULL,
    provincia VARCHAR(120),
    cant_pantallas integer,
    cant_butacas integer,
    cant_espacios_incaa integer,
    job_date date,
    PRIMARY KEY (id_cine_insights)
);