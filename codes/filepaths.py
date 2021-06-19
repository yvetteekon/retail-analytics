import os

project_parent_directory = '..'


RAW_DIR = os.path.join(project_parent_directory, 'data', 'raw')
EXTERNAL_DIR = os.path.join(project_parent_directory, 'data', 'external')
INTERIM_DIR  = os.path.join(project_parent_directory, 'data', 'interim')
PROCESSED_DIR = os.path.join(project_parent_directory, 'data', 'processed')
DICTIONARY_DIR = os.path.join(project_parent_directory, 'dictionary')

#raw data files
raw_customer_data = os.path.join(RAW_DIR, 'Customer.csv')
raw_city_data = os.path.join(RAW_DIR, 'cities.csv')
raw_us_regions_data = os.path.join(RAW_DIR, 'us census bureau regions and divisions.csv')
raw_transactions_data = os.path.join(RAW_DIR, 'Transactions.csv')
raw_products_data = os.path.join(RAW_DIR, 'prod_cat_info.csv')

#interim data files
clean_transactions_data_v1 = os.path.join(INTERIM_DIR, 'transactions_data_clean_v1.csv')
clean_customer_data_v1 = os.path.join(INTERIM_DIR, 'customer_data_clean_v1.csv')
clean_cities_data_v1 = os.path.join(INTERIM_DIR, 'cities_data_clean_v1.csv')
clean_us_regions_data_v1 = os.path.join(INTERIM_DIR, 'us_regions_data_clean_v1.csv')
derived_transactions_data_v1 = os.path.join(INTERIM_DIR, 'transactions_data_derived_v1.csv')

#processed data files
master_file_data = os.path.join(PROCESSED_DIR, 'master_file.csv')
purchase_frequency_distribution = os.path.join(PROCESSED_DIR, 'purchase_frequency_distribution.csv')
processed_transactions_data = os.path.join(PROCESSED_DIR, 'transactions_data_final.csv')
processed_churn_data =  os.path.join(PROCESSED_DIR, 'churn_data.csv')

#dictionary
dictionary_file = os.path.join(DICTIONARY_DIR, 'nomenclature_dictionary.xlsx')