import pandas as pd
import psycopg
from sqlalchemy import create_engine
print("1. Starting program...")
#postgresql+psycopg://USERNAME:PASSWORD@HOST:PORT/DATABASE
# "postgresql+psycopg://postgres@localhost:5432/postgres"


engine = create_engine(
    "postgresql+psycopg://postgres:kavin@localhost:5432/postgres"
)

print("2. Engine created...")

def execute_query(query):
    print("3. Running query...")

    with engine.connect() as conn:
        print("4. Connected to PostgreSQL!")
        df = pd.read_sql(query, conn)

    print("5. Query completed!")
    return df
#To create Dynamic Schema
def get_schema(table_name):
    query = f'''
            SELECT
    table_name ,       
    column_name,
    data_type
    FROM information_schema.columns
    where table_schema= 'public' and table_name = '{table_name}'
    ORDER BY ordinal_position;
        '''
    schema = execute_query(query)
    return schema




#result = execute_query("SELECT * FROM orders")
result=get_schema('orders')

print("6. Result:")
print(result)