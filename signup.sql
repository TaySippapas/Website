create table if not exists signup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gmail TEXT UNIQUE not NULL,
    username TEXT UNIQUE not null,
    password TEXT not null
); 