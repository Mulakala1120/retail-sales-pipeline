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

## Resume Entry
**Retail Sales Analytics Pipeline – GitHub**  
**May 2024 – Jun 2024**  
• Developed a serverless data pipeline using AWS Glue, S3, and Athena to process and analyze retail sales data in real time.  
• Built a PySpark-based ETL job in AWS Glue to ingest, clean, and transform CSV data from S3, generating aggregated sales metrics.  
• Designed and deployed Athena SQL queries for fast, serverless reporting on daily revenue, region-based sales, and product trends.  
• Created a reusable and scalable Glue job framework with schema evolution support and automated partitioning.  
• Architected the pipeline using modular components with full CI/CD and version control, enabling easy enhancements and debugging.
