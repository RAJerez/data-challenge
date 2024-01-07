CREATE TABLE IF NOT EXISTS raw(
    cod_localidad INTEGER NOT NULL,
    id_provicia INTEGER NOT NULL,
    id_departamento INTEGER NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    localidad VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255) NOT NULL,
    codigo VARCHAR(255) NOT NULL,
    numero_telefono VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    web VARCHAR(255) NOT NULL
);