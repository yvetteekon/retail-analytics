import os

project_parent_directory = '..'


RAW_DIR = os.path.join(project_parent_directory, 'data', 'raw')
EXTERNAL_DIR = os.path.join(project_parent_directory, 'data', 'external')
INTERIM_DIR  = os.path.join(project_parent_directory, 'data', 'interim')
PROCESSED_DIR = os.path.join(project_parent_directory, 'data', 'processed')

#raw data directories
raw_customer_data = os.path.join(RAW_DIR, 'Customer.csv')
raw_transactions_data = os.path.join(RAW_DIR, 'Transactions.csv')
raw_products_data = os.path.join(RAW_DIR, 'prod_cat_info.csv')

#processed data directories
master_file_data = os.path.join(PROCESSED_DIR, 'master_file.csv')
