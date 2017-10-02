# Microservice for Search Index of Phone Numbers

#### The scenario is that: Pizza shop has some uncomfortable work flow,customer care specialist looking for clients by telephone numbers,those has been writed any format like +79291112233 or 8 929 111-22-33.The task is make those numbers easy to search without country code and strict standart


## How to use
  - First we need to copy source db as local to do it run script **python copy_db.py**
  - Second we need add a new column for updated numbers for this purpose we will use [Alembic](http://alembic.zzzcomputing.com/en/latest/):
    * Before pushing the script don't forget insert your db URI in file alembic.ini(38 row)
    * Run the script **alembic upgrade head**
  - Last step is run the script **python make_beutiful.number.py**(this script will executed each 3 minutes on background in endless cycle)


### Sample result
![db](https://user-images.githubusercontent.com/22424468/31056651-daf05684-a6f6-11e7-8105-f5ee796ba535.JPG)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
