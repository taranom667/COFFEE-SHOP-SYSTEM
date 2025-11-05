-- ============================================
-- DATABASE SCHEMA FOR SELLING SYSTEM
-- Exact match with Model __init__ parameters
-- ============================================

-- customers: (customer_id, first_name, last_name, phone_number, order_id)
create table if not exists customers
(
    id  integer primary key autoincrement,
    first_name   text    not null,
    last_name    text    not null,
    phone_number text    not null,
    order_id     integer not null
);

--Employees:(id,first_name, last_name,role,username,password,salary)
create table if not exists employees
(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    role text not null,
    username text not null,
    password  integer not null,
    salary integer not null


);
--delivery :(id,order_id,rider,status,address)
create table if not exists deliveries(

    id integer  primary key autoincrement,
    order_id integer not null,
    rider text not null,
    status text not null,
    address text not null
);

--dish :(id, name,quantity, price, category, available, ingredients)
create table if not exists dishes(

    id integer  primary key autoincrement,
    name text not null,
    quantity integer not null,
    price integer not null,
    category text not null,
    available boolean not null,
    ingredients text not null
);

--order :(id, customer_name, dish, status, total_price, delivery_id, date_time)
create table if not exists orders(

    id integer  primary key autoincrement,
    customer_name text not null,
    dish text not null,
    status text not null,
    total_price integer not null,
    delivery_id integer not null,
    date_time text not null
);

--inventory :( id, name, material, manager, location, capacity)
create table if not exists inventories(

    id integer  primary key autoincrement,
    name text not null,
    material text not null,
    manager text not null,
    location text not null,
    capacity integer not null
);
--payment :( id,order_id,total_price,payment_type,date_time,customer_id,status,factor_id)
create table if not exists payments(

    id integer  primary key autoincrement,
    order_id text not null,
    total_price integer not null,
    payment_type text not null,
    date_time text not null,
    customer_id integer not null,
    status text not null,
    factor_id integer not null

);

--Raw_material:(id, name, category, unit, quantity, price, purchase_date, expiry_date, location)
create table if not exists Raw_materials(

    id integer  primary key autoincrement,
    name text not null,
    category text not null,
    unit text not null,
    quantity integer not null,
    price integer not null,
    purchase_date text not null,
    expiry_date text not null,
    location text not null

);