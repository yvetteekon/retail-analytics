import os

project_parent_directory = '..'


RAW_DIR = os.path.join(project_parent_directory, 'data', 'raw')
EXTERNAL_DIR = os.path.join(project_parent_directory, 'data', 'external')
INTERIM_DIR  = os.path.join(project_parent_directory, 'data', 'interim')
PROCESSED_DIR = os.path.join(project_parent_directory, 'data', 'processed')
DICTIONARY_DIR = os.path.join(project_parent_directory, 'dictionary')

#raw data files
raw_customer_data = os.path.join(RAW_DIR, 'Customer.csv')
raw_transactions_data = os.path.join(RAW_DIR, 'Transactions.csv')
raw_products_data = os.path.join(RAW_DIR, 'prod_cat_info.csv')

#interim data files
interim_transactions_data = os.path.join(INTERIM_DIR, 'transactions_data_clean.csv')
interim_transactions_data_aggregated = os.path.join(INTERIM_DIR, 'transactions_data_aggregated.csv')

#processed data files
master_file_data = os.path.join(PROCESSED_DIR, 'master_file.csv')
purchase_frequency_distribution = os.path.join(PROCESSED_DIR, 'purchase_frequency_distribution.csv')
processed_transactions_data = os.path.join(PROCESSED_DIR, 'transactions_data_final.csv')
processed_churn_data =  os.path.join(PROCESSED_DIR, 'churn_data.csv')

#dictionary
dictionary_file = os.path.join(DICTIONARY_DIR, 'nomenclature_dictionary.xlsx')