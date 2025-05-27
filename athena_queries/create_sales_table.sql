CREATE EXTERNAL TABLE IF NOT EXISTS retail_sales (
    OrderID STRING,
    OrderDate DATE,
    CustomerID STRING,
    ProductID STRING,
    ProductCategory STRING,
    Quantity INT,
    UnitPrice FLOAT,
    TotalAmount FLOAT,
    Region STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
) LOCATION 's3://your-bucket/data/'
TBLPROPERTIES ('has_encrypted_data'='false');
