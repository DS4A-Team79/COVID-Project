import boto3
import pandas as pd

# if sys.version_info[0] < 3: 
#     from StringIO import StringIO # Python 2.x
# else:
from io import StringIO # Python 3.x

# for per state funding 2020 dataframe
aws_id = 'AWS_ACCESS_KEY'
aws_secret = 'AWS_SECRET_KEY'
bucket_name = "elasticbeanstack_domain"

client1 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
object_key1 = 'per_state_funding_2020.csv'
csv_obj1 = client1.get_object(Bucket=bucket_name, Key=object_key1)
body1 = csv_obj1['Body']
csv_string1 = body1.read().decode('utf-8')

psf_2020_df = pd.read_csv(StringIO(csv_string1))

# for per state funding 2021 dataframe
client2 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
object_key2 = 'per_state_funding_2021.csv'
csv_obj2 = client2.get_object(Bucket=bucket_name2, Key=object_key2)
body2 = csv_obj2['Body']
csv_string2 = body2.read().decode('utf-8')

psf_2021_df = pd.read_csv(StringIO(csv_string2))

# for per capita funding 2020 dataframe
client3 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
object_key3 = 'per_capita_funding_2020.csv'
csv_obj3 = client3.get_object(Bucket=bucket_name, Key=object_key3)
body3 = csv_obj3['Body']
csv_string3 = body3.read().decode('utf-8')

pcf_2020_df = pd.read_csv(StringIO(csv_string3))

# for per capita funding 2021 dataframe
client4 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
object_key4 = 'per_capita_funding_2021.csv'
csv_obj4 = client4.get_object(Bucket=bucket_name4, Key=object_key4)
body4 = csv_obj4['Body']
csv_string4 = body4.read().decode('utf-8')

pcf_2021_df = pd.read_csv(StringIO(csv_string4))