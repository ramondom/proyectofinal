CREATE TABLE "Peliculas" (
	"id"	INTEGER NOT NULL,
	"titulo"	TEXT NOT NULL,
	"descripcion"	TEXT,
	"genero"	TEXT,
	"actores"	TEXT,
	"duracion"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)


CREATE TABLE "Usuarios" (
	"id"	INTEGER NOT NULL,
	"usuario"	TEXT UNIQUE,
	"contraseña"	TEXT,
	"nombre"	TEXT,
	"apellido"	TEXT,
	"esActivo"	INTEGER NOT NULL,
	"mail"	REAL,
	"dni"	TEXT,
	"fechaNacimiento"	TEXT,
	"idRol"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("idRol") REFERENCES "Roles"("idRol")
)

CREATE TABLE "Salas" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT,
	"filas"	INTEGER,
	"butaca_fila"	INTEGER,
	"tipo"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)

CREATE TABLE "Reservas" (
	"id"	INTEGER NOT NULL,
	"hora"	TEXT,
	"sala"	INTEGER,
	"pelicula"	INTEGER,
	"usuario"	INTEGER,
	"fecha"	TEXT,
	"precio"	INTEGER,
	"estado"	INTEGER DEFAULT 0,
	"butaca"	INTEGER,
	FOREIGN KEY("butaca") REFERENCES "Butacas"("id"),
	FOREIGN KEY("sala") REFERENCES "Salas"("id"),
	FOREIGN KEY("pelicula") REFERENCES "Peliculas"("id"),
	FOREIGN KEY("usuario") REFERENCES "Usuarios"("id"),
	FOREIGN KEY("precio") REFERENCES "Descuentos"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)


CREATE TABLE "Descuentos" (
	"id"	INTEGER NOT NULL,
	"dia"	TEXT,
	"tasa"	REAL,
	"estado"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
)


CREATE TABLE "Roles" (
	"idRol"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL UNIQUE,
	"activo"	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("idRol")
)


CREATE TABLE "HistorialEntradas" (
	"id"	INTEGER NOT NULL,
	"usuario"	INTEGER,
	"fecha"	TEXT,
	"reserva"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("usuario") REFERENCES "Usuarios"("id"),
	FOREIGN KEY("reserva") REFERENCES "Reservas"("id")
)

CREATE TABLE "Butacas" (
	"id"	INTEGER NOT NULL,
	"fila"	INTEGER,
	"columna"	INTEGER,
	"estado"	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT)
)
