import pandas as pd
import boto3
from io import StringIO

filename = 'myfile.xls'
buckename = 'mybucket'

df = pd.read_csv('somefile.csv')
df.head()

# buffer object
csv_buffer = StringIO()
df.to_csv(csv_buffer)

client = boto3.client('s3')

response = client.put_object(
    ACL='private',
    Body = csv_buffer.getvalue(),
    Bucket = buckename,
    Key = filter
)


