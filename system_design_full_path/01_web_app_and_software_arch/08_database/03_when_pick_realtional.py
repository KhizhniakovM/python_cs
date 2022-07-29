# When should you pick a relational database?
# In this lesson, I will discuss when to pick a relational database for a project.

# You should pick a relational database if you need strong consistency, transactions, or relationships. Typical examples of apps needing strong consistency are stock trading, personal banking, etc., and relational data is common in apps like Facebook, LinkedIn, etc.

# Transactions and data consistency
# If you are writing software that has anything to do with money or numbers that makes transactions, ACID and data consistency super important to you.

# Relational DBs shine when it comes to transactions and data consistency. They comply with the ACID rule, have been around for ages, and are battle-tested. More on strong consistency in the upcoming lessons.

# Large community
# Additionally, relational databases have a large community. Seasoned engineers on the tech are readily available. You don’t have to go too far looking for them.

# Storing relationships
# If your data has a lot of relationships that we typically come across in social networking apps like what friends of yours live in a particular city, which of your friends already ate at the restaurant you plan to visit today, etc. Relational databases suit well for storing this kind of data.

# Relational databases are built to store relationships. They have been tried and tested and are used by big guns in the industry. Facebook leverages a relational database as their main user-facing DB.

# Popular relational databases
# Some of the popular relational databases used in the industry are:

# MySQL, an open-source relationship database written in C and C++, has been around since 1995.

# PostgreSQL, an open-source RDBMS written in C.

# Microsoft SQL Server, a proprietary RDBMS written by Microsoft in C and C++.

# MariaDB, Amazon Aurora, Google Cloud SQL, etc.

# Folks!, that’s all on the relational databases. Let’s understand non-relational databases in the lesson up next.
