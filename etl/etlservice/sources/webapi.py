import dlt
import json
from dlt.common import pendulum
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import base64
import os
import posixpath
from typing import Iterator

import dlt
from dlt.sources import TDataItem, TDataItems

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
    
api_endpoint = '{8}'
{1}


# Set headers with Basic Authentication
{2}
{3}
if response.status_code == 200:
    api_data = json.loads(response.text)
else:
    print("Error: "+ str(response.status_code))
    api_data = None

# Create DataFrame if data is available
if api_data:
    df = pd.json_normalize(api_data)
    print(df.head())
    pipeline = dlt.pipeline("{0}_pipeline", destination="filesystem")
    pipeline.run(df, table_name="{4}", loader_file_format="parquet")
    pipelinef = dlt.pipeline(pipeline_name="{0}_pipeline", destination='duckdb', dataset_name="{0}", )
    # When using the readers resource, you can specify a filter to select only the files you
    # want to load including a glob pattern. If you use a recursive glob pattern, the filenames
    # will include the path to the file inside the bucket_url.

    # JSONL reading (in large chunks!)
    jsonl_reader = readers("{5}", file_glob="*.parquet").read_parquet()
    jsonl_reader1 = readers("{7}", file_glob="*.parquet").read_parquet()
    # load both folders together to specified tables
    load_info = pipelinef.run([jsonl_reader.with_name("{6}"),jsonl_reader1.with_name("{6}")])
    print(load_info)
    print(pipelinef.last_trace.last_normalize_info)
