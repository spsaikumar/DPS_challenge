from google.cloud import aiplatform
import os

# Set your project id and region
PROJECT_ID = "your_project_id"
REGION = "your_region"

# Authenticate the GCP client using application default credentials
# Refer to https://cloud.google.com/docs/authentication/production for more details
aiplatform.init(project=PROJECT_ID, location=REGION)

# Create a model resource
model_display_name = "your_model_display_name"
model_artifact_uri = "gs://your-bucket-name/path/to/your/model"
model_container_image_uri = "gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest"
model = aiplatform.Model.create(
    display_name=model_display_name,
    artifact_uri=model_artifact_uri,
    serving_container_image_uri=model_container_image_uri,
)

# Deploy the model to an endpoint
endpoint_display_name = "your_endpoint_display_name"
machine_type = "n1-standard-4"
traffic_percentage = 100
deployed_model_display_name = "your_deployed_model_display_name"
min_replica_count = 1
max_replica_count = 1
endpoint = model.deploy(
    endpoint_display_name=endpoint_display_name,
    deployed_model_display_name=deployed_model_display_name,
    machine_type=machine_type,
    traffic_percentage=traffic_percentage,
    min_replica_count=min_replica_count,
    max_replica_count=max_replica_count,
)


#preetam code
"""  
from google.cloud import aiplatform

# Create a model resource from public model assets
model = aiplatform.Model.upload(
    display_name="mpg-imported",
    artifact_uri="gs://io-vertex-codelab/mpg-model/",
    serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest"
)

# Deploy the above model to an endpoint
endpoint = model.deploy(
    machine_type="n1-standard-4"
)

"""