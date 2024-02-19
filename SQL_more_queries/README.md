
# **Author**

- ***Brandon Montezuma*** [@Bmontezuma](https://github.com/Bmontezuma)

# ***SQL - More queries***


![SQL](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/66988091.jpg)

# MySQL Database Management Guide

This guide provides resources and references for managing MySQL databases, including creating users, granting permissions, utilizing constraints, and various SQL techniques.

## Resources

### Tutorials and Guides

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-adminsitration/mysql-grant/)
- [MySQL constraints](https://www.mysqltutorial.org/mysql-constraint/)
- [SQL technique: subqueries](https://www.sqltutorial.org/sql-subquery/)
- [Basic query operation: the join](https://www.sqlshack.com/sql-join-overview/)
- [SQL technique: multiple joins and the distinct keyword](https://www.sqlshack.com/sql-join-overview/)
- [SQL technique: join types](https://www.sqlshack.com/sql-join-overview/)
- [SQL technique: union and minus](https://www.sqlshack.com/sql-union-overview/)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

### Extra Resources on Relational Database Model Design

- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

# MySQL Database Management Guide

This guide provides resources and references for managing MySQL databases, including creating users, granting permissions, utilizing constraints, and various SQL techniques.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## More Info

### Comments for your SQL file:

```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

...

mysql> quit
Bye

