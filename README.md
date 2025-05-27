# Retail Sales Analytics Pipeline

A data engineering project to process and analyze retail sales using AWS Glue, S3, Athena, and PySpark.

## Project Structure
- **data/**: Sample input CSV file.
- **glue_jobs/**: AWS Glue ETL script using PySpark.
- **athena_queries/**: SQL scripts to create and query tables in Athena.
- **architecture/**: Architecture diagrams.

## Technologies
- AWS Glue
- AWS S3
- AWS Athena
- Python / PySpark

## How to Use
1. Upload `sales_data.csv` to your S3 bucket (`s3://your-bucket/data/`).
2. Create the Glue job using the script in `glue_jobs/transform_sales_data.py`.
3. Run Athena DDL from `athena_queries/create_sales_table.sql`.
4. Query results using `athena_queries/query_sales_summary.sql`.

## Future Enhancements
Integrate with Amazon EventBridge or Lambda for real-time data ingestion
Add Amazon QuickSight dashboards for visualization
Incorporate Terraform or AWS CDK for infrastructure-as-code deployment
Schedule Glue jobs using workflow triggers and step functions

