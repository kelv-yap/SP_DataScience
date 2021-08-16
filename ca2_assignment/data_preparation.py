from ca2_assignment import mysql_config as config
import sys
import mysql.connector
import sqlalchemy
import numpy as np
import pandas as pd


# DATABASE: MYSQL CONNECTION
user, pw, host, db, sys_db = config.user, config.pw, config.host, config.db, config.sys_db


def region_mapper(town):
    mapper = {
        "SEMBAWANG": "NORTH",
        "WOODLANDS": "NORTH",
        "YISHUN": "NORTH",
        "ANG MO KIO": "NORTH-EAST",
        "HOUGANG": "NORTH-EAST",
        "PUNGGOL": "NORTH-EAST",
        "SENGKANG": "NORTH-EAST",
        "SERANGOON": "NORTH-EAST",
        "BEDOK": "EAST",
        "PASIR RIS": "EAST",
        "TAMPINES": "EAST",
        "BUKIT BATOK": "WEST",
        "BUKIT PANJANG": "WEST",
        "CHOA CHU KANG": "WEST",
        "LIM CHU KANG": "WEST",
        "CLEMENTI": "WEST",
        "JURONG EAST": "WEST",
        "JURONG WEST": "WEST",
        "BISHAN": "CENTRAL",
        "BUKIT MERAH": "CENTRAL",
        "BUKIT TIMAH": "CENTRAL",
        "CENTRAL AREA": "CENTRAL",
        "GEYLANG": "CENTRAL",
        "KALLANG/WHAMPOA": "CENTRAL",
        "MARINE PARADE": "CENTRAL",
        "QUEENSTOWN": "CENTRAL",
        "TOA PAYOH": "CENTRAL"
    }
    return mapper.get(town, "Invalid Town")


def data_collection_and_transformation():
    filtered_columns = ['month', 'town', 'flat_type', 'floor_area_sqm', 'lease_commence_date', 'resale_price']

    # DATA COLLECTION
    df1 = pd.read_csv("data/resale-flat-prices-based-on-approval-date-1990-1999.csv", sep=",")
    df1 = df1[filtered_columns]

    df2 = pd.read_csv("data/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv", sep=",")
    df2 = df2[filtered_columns]

    df3 = pd.read_csv("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv", sep=",")
    df3 = df3[filtered_columns]

    df4 = pd.read_csv("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv", sep=",")
    df4 = df4[filtered_columns]

    df5 = pd.read_csv("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", sep=",")
    df5 = df5[filtered_columns]

    combined_data_count = df1.shape[0] + df2.shape[0] + df3.shape[0] + df4.shape[0] + df5.shape[0]
    print("Data Count (Before Combine): " + str(combined_data_count))

    df_combine = pd.concat([df1, df2, df3, df4, df5])
    print("Data Count (After Combine): {}".format(df_combine.shape[0]))

    # DATA TRANSFORMATION
    region = []
    for i in df_combine['town']:
        region.append(region_mapper(i))
    df_combine['region'] = region

    df_combine['month'] = df_combine['month'].astype(str).str[0:4]
    df_combine['floor_area_sqm'] = np.round(df_combine['floor_area_sqm'] * 10.7639, 2)
    df_combine = df_combine.rename(columns={'month': 'purchase_year',
                                            'floor_area_sqm': 'floor_area_sqft',
                                            'lease_commence_date': 'lease_year'})

    df_combine['price_per_sqft'] = np.round(df_combine['resale_price'] / df_combine['floor_area_sqft'], 2)
    df_combine['price_per_month'] = np.round(df_combine['resale_price'] / ((pd.to_numeric(df_combine['lease_year']) + 99 - pd.to_numeric(df_combine['purchase_year'])) * 12), 2)

    return df_combine


def mysql_create_database():
    connection = mysql.connector.connect(user=user, password=pw, host=host, database=sys_db, use_pure=True)
    cursor = connection.cursor()

    try:
        cursor.execute('DROP DATABASE IF EXISTS ca2db')
        cursor.execute('CREATE DATABASE ca2db')
        print("Database Created Successfully!")

        connection.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit()
    finally:
        cursor.close()
        connection.close()


def mysql_create_table():
    connection = mysql.connector.connect(user=user, password=pw, host=host, database=db, use_pure=True)
    cursor = connection.cursor()

    query_create_table = ('CREATE TABLE resale_hdb('
                          'id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,'
                          'purchase_year VARCHAR(10),'
                          'town VARCHAR(50),'
                          'flat_type VARCHAR(50),'
                          'floor_area_sqft FLOAT,'
                          'lease_year VARCHAR(10),'
                          'resale_price FLOAT,'
                          'region VARCHAR(50),'
                          'price_per_sqft FLOAT,'
                          'price_per_month FLOAT)')

    try:
        cursor.execute(query_create_table)
        print("Tables Created Successfully!")

        connection.commit()

    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit()
    finally:
        cursor.close()
        connection.close()


def mysql_insert_data_to_table(data):
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://{user}:{pw}@{host}/{db}'
                                      .format(user=user, pw=pw, host=host, db=db))
    connection = engine.connect()

    try:
        data.to_sql(con=engine, name='resale_hdb', if_exists='replace', chunksize=25000)
        print("All Records Inserted Successfully!")

    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit()
    finally:
        connection.close()


df = data_collection_and_transformation()
mysql_create_database()
mysql_create_table()
mysql_insert_data_to_table(df)
