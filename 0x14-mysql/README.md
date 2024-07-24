# 0x14. MySQL
### DevOps
### SysAdmin
### MySQL

by <joemwangala@gmail.com>
## Learning Objectives

What is the main role of a database
What is a database replica
What is the purpose of a database replica
Why database backups need to be stored in different physical locations
What operation should you regularly perform to make sure that your
database backup strategy actually works

```c
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'holberton_user'@'localhost';

### Sql commands used to create user in web servers 01 and 02