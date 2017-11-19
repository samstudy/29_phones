# Microservice for Search Index of Phone Numbers

#### The scenario is that: Pizza shop works have some uncomfortable flow,customer care specialist looking for clients by telephone numbers,those have been writed without any format like +79291112233 or 8 929 111-22-33.The task is make those numbers easy to search without country code and strict standart


## How to use
  - First we need make copy source db as local to do it run script **python create_local_db.py**
  - Second we need insert all date into the local db ,to do it run script **python copy_db.py**
  - Third we need add a new column for updated numbers for this purpose we will use [Alembic](http://alembic.zzzcomputing.com/en/latest/):
    * Before pushing the script don't forget insert your db URI in file alembic.ini(38 row)
    * Run the script **alembic upgrade head**
  - Last step is run the script **python make_beutiful.number.py**(this script will executed each 3 minutes on background in endless cycle)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
