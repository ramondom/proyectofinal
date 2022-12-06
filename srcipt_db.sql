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
	"mail"	TEXT,
	"dni"	TEXT,
	"fechaNacimiento"	TEXT,
	"idRol"	INTEGER,
	"activo"	INTEGER DEFAULT 0,
	FOREIGN KEY("idRol") REFERENCES "Roles"("idRol"),
	PRIMARY KEY("id" AUTOINCREMENT)
)

CREATE TABLE "Salas" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT,
	"capacidad"	INTEGER DEFAULT 0,
	"formato"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)


CREATE TABLE "Reservas" (
	"id"	INTEGER NOT NULL,
	"idFuncion"	INTEGER,
	"idUsuario"	INTEGER,
	"fecha"	TEXT,
	"precio"	REAL DEFAULT 0,
	"idButaca"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("idFuncion") REFERENCES "Funciones"("id"),
	FOREIGN KEY("idUsuario") REFERENCES "Usuarios"("id")
)


CREATE TABLE "Descuentos" (
	"id"	INTEGER NOT NULL,
	"dia"	TEXT,
	"tasa"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
)


CREATE TABLE "Roles" (
	"idRol"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL UNIQUE,
	"activo"	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("idRol")
)


CREATE TABLE "Funciones" (
	"id"	INTEGER NOT NULL,
	"fecha"	TEXT,
	"idSala"	INTEGER,
	"idPelicula"	INTEGER,
	"hora"	TEXT,
	FOREIGN KEY("idSala") REFERENCES "Salas"("id"),
	FOREIGN KEY("idPelicula") REFERENCES "Peliculas"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)

CREATE TABLE "Butacas" (
	"id"	INTEGER NOT NULL,
	"fila"	INTEGER,
	"numero"	INTEGER,
	"idSala"	INTEGER,
	FOREIGN KEY("idSala") REFERENCES "Salas"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)
