#%%
import pandas as pd 
import altair as alt
import numpy as np
import sqlite3

#%%
# SQlite db 
sqlite_file_name = 'sqlitedb.sqlite'
con = sqlite3.connect(sqlite_file_name)

# make a variable to keep track of things
cursor = con.cursor()






#%% make a datatable
create_table_sql_ = """
CREATE TABLE IF NOT EXISTS apartment (
    formID INTEGER PRIMARY KEY AUTOINCREMENT,
    prepapartment TEXT NOT NULL,
    star TEXT,
    apartment TEXT,
    housing TEXT,
    semester TEXT,
    UpcomingSchoolYear INTEGER,
    ThisSemesterCost INTEGER
);
"""

# the cursor is now calling the execute function using the new table as a parameter.
cursor.execute(create_table_sql_)

# officialize the transaction
con.commit()

# %%
df = pd.read_sql_query("""
    SELECT *
    FROM apartment
""", con)
# %%
df





# %% DELETE A TABLE

# identify the table to be removed.
table_to_remove_ = 'apartments'

#
drop_table_sql_ = f"DROP TABLE IF EXISTS {table_to_remove_};"

#make a variable that deletes a table
cursor.execute(drop_table_sql_)

#make it official
con.commit()

df





# %%
# INSERT DATA INTO THE table
insert_row = """
INSERT INTO apartment (
    preapartment,
    star,
    apartment,
    housing,
    semester,
    UpcomingSchoolYear,
    ThisSemesterCost
)
VALUES('Nauvoo House', 'threeval', 'Nauvoo House', 'Mens', 'Fall', 2024, 1500)
"""
cursor.execute(insert_row)
con.commit()

# %%
df
# %%
df = pd.read_sql_query("""
    SELECT *
    FROM apartment
""", con)
df

#%% insert another data point
insert_row = """
INSERT INTO apartment (
    preapartment,
    star,
    apartment,
    housing,
    semester,
    UpcomingSchoolYear,
    ThisSemesterCost
)
VALUES('Nauvoo House', 'oneval', 'Somerset', 'Womens', 'Spring', 2023, 1080)
"""
cursor.execute(insert_row)
con.commit()
# %%
df
# %%
df = pd.read_sql_query("""
    SELECT *
    FROM apartment
""", con)
df
#%% insert another value
insert_row = """
INSERT INTO apartment (
    preapartment,
    star,
    apartment,
    housing,
    semester,
    UpcomingSchoolYear,
    ThisSemesterCost
)
VALUES('Somerset', 'fourval', 'Bountiful Place', 'Mens', 'Fall', 2021, 1550)
"""
cursor.execute(insert_row)
con.commit()
# %%
df
# %%
df = pd.read_sql_query("""
    SELECT *
    FROM apartment
""", con)
df




# %%
#Delete something from the database
delete_row = """
DELETE FROM apartment 
WHERE preapartment = 'Not Applicable';
"""#this removes everything with a form ID equal to or greater than zero. so everything form the df

cursor.execute(delete_row)

con.commit()
#%%
df = pd.read_sql_query("""
    SELECT *
    FROM apartment
""", con)

df





#%%
# Modify data
update_row = """
UPDATE apartment
SET preapartment = 'The Cove',
    UpcomingSchoolYear = 2025
WHERE apartment = 'Nauvoo House';
"""

cursor.execute(update_row)

con.commit()

df = pd.read_sql_query("""
    SELECT *
    FROM apartment
""", con)
df



#%%
#I mispelled a column name so I am fixing it.
# alter_column = """
# ALTER TABLE apartment
# RENAME COLUMN prevapartment TO preapartment
# """
# cursor.execute(alter_column)

# con.commit()

# df = pd.read_sql_query("""
#     SELECT *
#     FROM apartment
# """, con)

# df

#%%
#use results for something.
# %%
df1 = df
df1 = pd.read_sql_query("""
    SELECT apartment, ThisSemesterCost, UpcomingSchoolYear 
    FROM apartment AS a
    WHERE apartment IN ("Nauvoo House", "The Cove", "Somerset")
""", con)

base = alt.Chart(df1).encode(
        x = alt.X('UpcomingSchoolYear'),
        y = 'ThisSemesterCost',
        color=alt.Color('apartment:N')#chatgpt helped with the color line. It made the color different depending on the teamkey:n
    ).mark_line()
# %%
base
# %%
