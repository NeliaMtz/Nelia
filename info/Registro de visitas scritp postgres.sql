CREATE TABLE "Usuarios" (
  "CURP" varchar PRIMARY KEY,
  "Nombre" varchar,
  "Ap_pat" varchar,
  "Ap_Mat" varchar,
  "Edad" varchar,
  "Cve_CT" varchar,
  "Escolaridad" varchar,
  "Funcion" varchar,
  "email" varchar
);

CREATE TABLE "Visita" (
  "id" integer PRIMARY KEY,
  "CURP" varchar,
  "Fecha" datetime,
  "Hora_ini" datetime,
  "Hora_fin" datetime,
  "id_tramite" integer,
  "CURP_Cap" varchar
);

CREATE TABLE "Tramite" (
  "id" interger PRIMARY KEY,
  "Descripcion" varchar
);

CREATE TABLE "Capturista" (
  "CURP_Cap" varchar PRIMARY KEY,
  "Nombre" varchar,
  "Puesto" varchar
);

CREATE TABLE "CT" (
  "CT" varchar PRIMARY KEY,
  "Descripcion" varchar
);

ALTER TABLE "CT" ADD FOREIGN KEY ("CT") REFERENCES "Usuarios" ("Cve_CT");

ALTER TABLE "Visita" ADD FOREIGN KEY ("CURP_Cap") REFERENCES "Capturista" ("CURP_Cap");

ALTER TABLE "Visita" ADD FOREIGN KEY ("id_tramite") REFERENCES "Tramite" ("id");

ALTER TABLE "Visita" ADD FOREIGN KEY ("CURP") REFERENCES "Usuarios" ("CURP");
