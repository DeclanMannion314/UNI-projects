-- Create table courses
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    department_id INT,
    course_name VARCHAR(20) UNIQUE NOT NULL,
    course_desc TEXT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);


-- Create table students
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    course_id INT,
    student_first_name VARCHAR(50) NOT NULL,
    student_mid_name VARCHAR(50),
    student_last_name VARCHAR(50) NOT NULL,
    student_dob DATE NOT NULL,
    student_addr1 VARCHAR(50) NOT NULL,
    student_addr2 VARCHAR(50),
    student_city VARCHAR(50) NOT NULL,
    student_postcode VARCHAR(8) NOT NULL,
    student_country VARCHAR(30) NOT NULL,
    student_email VARCHAR(100) UNIQUE NOT NULL,
    student_phone VARCHAR(15) UNIQUE,
    student_study_level ENUM('4', '5', '6', '7') NOT NULL,
    student_grades DECIMAL(5, 2),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


-- Create table departments
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) UNIQUE NOT NULL,
    department_desc TEXT,
    department_type VARCHAR(12) NOT NULL
);


-- Create table student_subjects
CREATE TABLE student_subjects (
    student_id INT,
    subject_id INT,
    student_grade FLOAT,
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);


-- Create table grades
CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade_value DECIMAL(5, 2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);


-- Create table students_sessions
CREATE TABLE students_sessions (
    student_id INT,
    session_id INT,
    PRIMARY KEY (student_id, session_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);


-- Create table roles
CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(30) UNIQUE NOT NULL,
    role_desc TEXT
);


-- Create table subjects
CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    course_id INT,
    subject_name VARCHAR(50) UNIQUE NOT NULL,
    subject_desc TEXT,
    subject_level ENUM('4', '5', '6', '7') NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


-- Create table sessions
CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    subject_id INT,
    staff_id INT,
    session_duration TIME,
    session_date DATE NOT NULL,
    session_status VARCHAR(15) NOT NULL,
    session_topic TEXT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);


-- Create table staff_students
CREATE TABLE staff_students (
    staff_id INT,
    student_id INT,
    first_teach_date DATE NOT NULL,
    sessions_completed INT,
    PRIMARY KEY (staff_id, student_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


-- Create table staff_roles
CREATE TABLE staff_roles (
    staff_id INT,
    role_id INT,
    PRIMARY KEY (staff_id, role_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);


-- Create table staff
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    department_id INT,
    staff_first_name VARCHAR(50) NOT NULL,
    staff_mid_name VARCHAR(50),
    staff_last_name VARCHAR(50) NOT NULL,
    staff_dob DATE NOT NULL,
    staff_addr1 VARCHAR(50) NOT NULL,
    staff_addr2 VARCHAR(50),
    staff_city VARCHAR(50) NOT NULL,
    staff_postcode VARCHAR(8) NOT NULL,
    staff_country VARCHAR(30) NOT NULL,
    staff_email VARCHAR(100) UNIQUE NOT NULL,
    staff_phone VARCHAR(15) UNIQUE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
