CREATE TABLE "Peliculas" (
	"id"	INTEGER NOT NULL,
	"titulo"	TEXT NOT NULL,
	"descripcion"	TEXT,
	"genero"	TEXT,
	"actores"	TEXT,
	"duracion"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);


CREATE TABLE "Usuarios" (
	"id"	INTEGER NOT NULL,
	"usuario"	TEXT UNIQUE,
	"contraseña"	TEXT,
	"nombre"	TEXT,
	"apellido"	TEXT,
	"esActivo"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Salas" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT,
	"filas"	INTEGER,
	"butacas/fila"	INTEGER,
    "estado"	INTEGER DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Reservas" (
	"id"	INTEGER NOT NULL,
	"hora"	TEXT,
	"sala"	INTEGER,
	"pelicula"	INTEGER,
	"usuario"	INTEGER,
	"fechaReserva"	TEXT,
	"precio"	INTEGER,
    "estado"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Descuentos" (
	"id"	INTEGER NOT NULL,
	"dia"	TEXT,
	"tasa"	REAL,
    "estado"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);