from pyspark.sql import SparkSession
from pyspark.pandas import DataFrame, read_csv
import pandas as pd

# products = pd.DataFrame({'product': 
#                    ['strings', 'ural_guitar', 'snare_drum', 'bread', 'milk', 'lada', 'uaz', 'toyota', 'ural_guitar', 'lada', 'uaz'], 
#                    'category_id': 
#                    [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3]})

# categories = pd.DataFrame({
#     'category':
#     ['music', 'food', 'cars', 'russian']
# })
# products.to_csv('./products.csv')
# categories.to_csv('./categories.csv')

def get_prodicts_and_categories():

    spark = SparkSession.builder.getOrCreate()

    products = read_csv('./products.csv')
    categories = read_csv('./categories.csv')

    df_merged = products.merge(right = categories, right_index = True, left_on = 'category_id').drop(['_c0_x', '_c0_y', 'category_id'], axis = 1)

    return df_merged