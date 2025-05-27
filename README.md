# Retail Sales Analytics Pipeline

A fully serverless, scalable data pipeline built on AWS services to automate the processing and analysis of retail sales data. Designed with production-grade ETL practices using AWS Glue, S3, and Athena, this pipeline delivers efficient, cost-effective insights through SQL-based reporting.

## Project Summary

This project demonstrates a real-time analytics solution for retail data. Daily CSV files are ingested from Amazon S3, cleaned and transformed using AWS Glue (PySpark), and made queryable using Athena. The architecture is designed to be modular, extensible, and cloud-native.

## Project Structure
- data/: Sample input CSV file.
- glue_jobs: AWS Glue ETL script using PySpark.
- athena_queries: SQL scripts to create and query tables in Athena.
- architecture: Architecture diagrams.

## Architecture Overview

- Amazon S3: Stores both raw input data and processed outputs.
- AWS Glue: Performs ETL operations via PySpark scripts; handles schema transformation and partitioning.
- Amazon Athena: Executes analytical queries on transformed datasets stored in S3.
- GitHub: Maintains version control for the codebase and deployment artifacts.

## Key Features

- End-to-End Serverless Architecture: No servers or clusters to manage.
- Automated ETL with AWS Glue: Processes and transforms large volumes of sales data using PySpark.
- Partitioned Output: Enables optimized querying and cost savings in Athena.
- Schema Evolution: Dynamically handles changes in incoming data structure.
- Reusability & Modularity: Built for easy maintenance and extension.
- SQL-Based Reporting: Athena queries provide real-time insights on sales trends, revenue, and product performance.

## Use Case Scenario

> A retail chain uploads daily sales reports (CSV) to an S3 bucket. The pipeline:
> 1. Triggers AWS Glue ETL to clean and transform data
> 2. Outputs partitioned data to an S3 target location
> 3. Executes Athena queries to:
> Calculate total revenue per day
> Analyze sales by region and product category
> Identify top-selling products and trends


## Technologies Used

Data Storage, Amazon S3, ETL Framework, AWS Glue (PySpark), Analytics Engine, Amazon Athena, Programming, Python, SQL, Version Control, Git, GitHub

## How to Use
1. Upload `sales_data.csv` to your S3 bucket (`s3://your-bucket/data/`).
2. Create the Glue job using the script in `glue_jobs/transform_sales_data.py`.
3. Run Athena DDL from `athena_queries/create_sales_table.sql`.
4. Query results using `athena_queries/query_sales_summary.sql`.

## Future Enhancements
Integrate with Amazon EventBridge or Lambda for event-driven processing
- Add CI/CD using AWS CodePipeline or GitHub Actions
- Visualize outputs using Amazon QuickSight or Looker
- Convert job definitions to infrastructure-as-code with Terraform or AWS CDK

