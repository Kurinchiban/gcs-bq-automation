import functions_framework
from googleapiclient.discovery import build
from google.auth import default

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def trigger_gcs(cloud_event):
    credentials, _ = default()
    service = build('dataflow', 'v1b3', credentials=credentials)

    project = "my-first-pipeline-453507"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "gcs-bigquery-pipeline",
        "parameters": {
            "inputFilePattern": "gs://gcs-bq-automation-bucket/commodity_03.csv",
            "JSONPath": "gs://gcs-bq-automation-bucket-metadata/schema.json",
            "outputTable": "my-first-pipeline-453507:agricultural_market.india_commodity",
            "bigQueryLoadingTemporaryDirectory": "gs://gcs-bq-automation-bucket-metadata"
        }
    }

    request = service.projects().locations().templates().launch(
        projectId=project,
        location="us-central1", 
        gcsPath=template_path,
        body={"jobName": "gcs-bigquery-pipeline", "parameters": template_body["parameters"]}
    )

    response = request.execute()
    print(response)
