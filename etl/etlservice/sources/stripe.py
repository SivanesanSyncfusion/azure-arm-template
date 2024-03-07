import dlt
from dlt.sources.helpers import requests
from dlt.common import pendulum


@dlt.source
def stripe_source(api_secret_key=dlt.secrets.value):
    return stripe_resource(api_secret_key)


def _create_auth_headers(api_secret_key):
    """Constructs Bearer type authorization header which is the most common authorization method"""
    headers = {"Authorization": f"Bearer {api_secret_key}"}
    return headers


@dlt.resource(write_disposition="append")
def stripe_resource(api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)

    # check if authentication headers look fine
    print(headers)

    # make an api call here
    # response = requests.get(url, headers=headers, params=params)
    # response.raise_for_status()
    # yield response.json()

    # test data for loading validation, delete it once you yield actual data
    test_data = [{"id": 0}, {"id": 1}]
    yield test_data


if __name__ == "__main__":
    # configure the pipeline with your destination details
    pipeline = dlt.pipeline(
        pipeline_name='{0}_pipeline', destination='duckdb', dataset_name='{0}'
    )

{1}

    # Load all data from another table
   # genome = sql_table(table="genome")

    # Run the resources together
    info = pipeline.run({2})

    # pretty print the information on data that was loaded
    print(info)
