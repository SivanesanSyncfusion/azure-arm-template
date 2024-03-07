import dlt
import elasticsearch
try:
    from .filesystem import FileItemDict, filesystem, readers, read_csv, read_jsonl, read_parquet  # type: ignore
except ImportError:
    from filesystem import (
        FileItemDict,
        filesystem,
        readers,
        read_csv,
        read_jsonl,
        read_parquet,
    )
from elasticsearch import Elasticsearch
import pandas as pd
from datetime import datetime, timedelta
import duckdb
import json
import tempfile
import os


# Elasticsearch configuration
ELASTICSEARCH_HOST = '{0}:{1}'
INDEX_NAME = '{2}'
API_KEY = '{3}'
{10}
# Function to fetch data from Elasticsearch with pagination and load into DataFrame
def fetch_data_and_load_into_dataframe(scroll_size={4}):
    es = Elasticsearch([ELASTICSEARCH_HOST], {11})    
    
    res = es.search(
        index=INDEX_NAME,
        scroll='1m',  # Specify how long Elasticsearch should keep the search context alive
        size=scroll_size
        {9}
    )
    scroll_id = res['_scroll_id']
    total_docs = res['hits']['total']['value'] # Total number of documents (available from Elasticsearch 7.x)

    # Store initial results
    hits = res['hits']['hits']
    all_records = [hit['_source'] for hit in hits]

    # Scroll through the results
    while len(all_records) < total_docs:
        res = es.scroll(scroll_id=scroll_id, scroll='1m')
        hits = res['hits']['hits']
        all_records.extend([hit['_source'] for hit in hits])


    # Load data into DataFrame
    print("Total records count:", len(all_records))
    temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json', dir="{7}")
    json.dump(all_records, temp_file)
    temp_file.close()
    print(format(temp_file.name))
    conn = duckdb.connect('{5}')
    conn.execute("CREATE SCHEMA IF NOT EXISTS {6}")
    conn.execute("{8}".format(temp_file.name))
    print("Data fetched successfully")

# Call function to fetch data and load into DataFrame
fetch_data_and_load_into_dataframe()

# Display DataFrame
