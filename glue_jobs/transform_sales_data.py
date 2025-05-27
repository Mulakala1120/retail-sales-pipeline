from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import sys

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load data
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket/data/sales_data.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

# Transform
df = datasource.toDF()
df.createOrReplaceTempView("sales_data")
result_df = spark.sql("""
    SELECT ProductCategory, Region, SUM(TotalAmount) AS TotalRevenue
    FROM sales_data
    GROUP BY ProductCategory, Region
""")

# Convert back
transformed_data = DynamicFrame.fromDF(result_df, glueContext, "transformed_data")

# Write
glueContext.write_dynamic_frame.from_options(
    frame=transformed_data,
    connection_type="s3",
    connection_options={"path": "s3://your-bucket/output/"},
    format="parquet"
)
job.commit()
