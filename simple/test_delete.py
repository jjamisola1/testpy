import ibm_boto3
from ibm_botocore.client import Config, ClientError



# Constants for IBM COS values
COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud"
#COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "WaSHFj4WjXclEL8Qvig8hx_P2M5MH8SVo8PQQ1J2wM0W" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/222f62ff44394e36a897716d033a11ab:1f688e65-472c-426c-8901-e57f39ea8165::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# Create client 
cos = ibm_boto3.client("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

def create_text_file(bucket_name, item_name, file_text):
    bucket_name = bucketjptok0001
    print("Creating new item: {0}".format(item_name))
    try:
        cos.Object(bucket_name, item_name).put(
            Body=file_text
        )
        print("Item: {0} created!".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to create text file: {0}".format(e))

#create_text_file(bucketjptok0001,new_text,file_text)


try:
    res = cos.delete_object(Bucket='bucketjptok0001', Key='test.txt')
except Exception as e:
    print(Exception, e)
else:
    print('File Deleted')

#https://ibm.github.io/ibm-cos-sdk-python/reference/services/s3.html#S3.Client.delete_object