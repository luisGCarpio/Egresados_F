CREATE TABLE program (
  id_program INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  program_name VARCHAR(150) NOT NULL,
  id_faculty INT NOT NULL
  creation_date DATE,
  update_date DATE,
  CONSTRAINT fk_faculty FOREIGN KEY (id_faculty) REFERENCES faculty(id_faculty)
);
create table faculty(
  id_faculty INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL unique
  creation_date DATE,
  update_date DATE,
)

CREATE TABLE academic_levels (
  id_level INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  description VARCHAR(50) NOT NULL
  creation_date DATE,
  update_date DATE,
);

CREATE TABLE employment_statuses (
  id_status INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  description VARCHAR(50) NOT NULL
  creation_date DATE,
  update_date DATE,
);

CREATE TABLE sectors ( 
  id_sector INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL
  creation_date DATE,
  update_date DATE,
);

CREATE TABLE contract_types (
  id_type INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  contract_name VARCHAR(50) NOT NULL,
  description VARCHAR(150) NOT NULL,
  duration VARCHAR(19) NOT NULL
  creation_date DATE,
  update_date DATE,
);

CREATE TABLE graduates (
  id_graduate INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  birth_date DATE,
  graduation_year INT NOT NULL,
  id_level INT NOT NULL,
  id_status INT NOT NULL,
  id_program INT NOT NULL,
  creation_date DATE,
  update_date DATE,
  CONSTRAINT fk_level FOREIGN KEY (id_level) REFERENCES academic_levels(id_level),
  CONSTRAINT fk_status FOREIGN KEY (id_status) REFERENCES employment_statuses(id_status),
  CONSTRAINT fk_program FOREIGN KEY (id_program) REFERENCES program(id_program)
);

CREATE TABLE jobs (
  id_job INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  id_graduate INT NOT NULL,
  company VARCHAR(150) NOT NULL,
  id_sector INT,
  position VARCHAR(100) NOT NULL,
  salary DECIMAL(10,2),
  start_date DATE NOT NULL,
  end_date DATE,
  id_type INT,
  related_to_career BOOLEAN,
  creation_date DATE,
  update_date DATE,
  CONSTRAINT fk_graduate FOREIGN KEY (id_graduate) REFERENCES graduates(id_graduate),
  CONSTRAINT fk_sector FOREIGN KEY (id_sector) REFERENCES sectors(id_sector),
  CONSTRAINT fk_type FOREIGN KEY (id_type) REFERENCES contract_types(id_type)
);

CREATE TABLE continuing_education (
  id_continuing_education INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  id_graduate INT NOT NULL,
  description_program VARCHAR(200) NOT NULL,
  education_type VARCHAR(100) NOT NULL,
  time VARCHAR(50),
  education_date DATE,
  creation_date DATE,
  update_date DATE,
  CONSTRAINT fk_ce_graduate FOREIGN KEY (id_graduate) REFERENCES graduates(id_graduate)
);

CREATE TABLE work_supervisor (
  id_supervisor INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  id_program INT NOT NULL,
  frist_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  id_graduate INT NOT NULL,
  id_job INT NOT NULL,
  contact_job VARCHAR(150) NOT NULL,
  creation_date DATE,
  update_date DATE,
  CONSTRAINT fk_ws_program FOREIGN KEY (id_program) REFERENCES program(id_program),
  CONSTRAINT fk_ws_graduate FOREIGN KEY (id_graduate) REFERENCES graduates(id_graduate),
  CONSTRAINT fk_ws_job FOREIGN KEY (id_job) REFERENCES jobs(id_job)
);

CREATE TABLE job_offer (
  id_offer INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  position VARCHAR(150) NOT NULL,
  company VARCHAR(150) NOT NULL,
  salary DECIMAL(10,2),
  id_type INT NOT NULL,
  area VARCHAR(150) NOT NULL,
  email_contact VARCHAR(150) NOT NULL,
  offer_date DATE NOT NULL,
  program VARCHAR(150) NOT NULL,
  creation_date DATE,
  update_date DATE,
  CONSTRAINT fk_offer_type FOREIGN KEY (id_type) REFERENCES contract_types(id_type)
  constraint fk_offer_program FOREIGN KEY (program) REFERENCES program(program_name)
);
