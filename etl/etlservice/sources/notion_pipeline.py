import dlt

from notion import notion_databases


def load_databases() -> None:
    """Loads all databases from a Notion workspace which have been shared with
    an integration.
    """
    pipeline = dlt.pipeline(
        pipeline_name="{0}_pipeline",
        destination='duckdb',
        dataset_name="{0}",
    )

    data = {0}

    info = pipeline.run(data)
    print(info)


if __name__ == "__main__":
    load_databases()
