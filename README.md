#Project_2 : Data Cleaning (Basic)_2

##Overview

This project is a continuation of guided practice exercise using similar simulated dataset format from project_1_data_cleaning_basic. It focuses on additional **data cleaning basics** and simple **visualization techniques**.

###Methods used

-**Date & Time Handling**: `pd.to_datetime`
-**String Format Handling**: `.str.strip`, `str.lower`, `str.replace`
-**Missing Data Handling**: `fillna.`, `dropna`
-**Temporary anonymous function Expression**: `lambda`
-**Data Aggregation**: `.groupby`
-**Visualization**: simple charts with matplotlib

##Environment Setup

1. Clone the repo
2. Create environment:

conda env create -f environment.vml
conda activate project_2

3. Copy /data/raw/messy_sales_data.csv into /scripts
4. Run python:

python scripts/analysis.py

##Project Structure

```
project_2_data_cleaning_basic/
|
|--data/
|  |__raw/				<-raw dataset (ignored by git)
|     |__messy_sales_data.csv
|
|--results/
|   |__cleaned_sales.csv		<-cleaned dataset
|   |__monthly_sales.csv		
|   |__Item Distribution.png
|   |__revenue_by_region.png
|
|--scripts/				<- Python Scripts
|  |__analysis.py
|
|--environment.yml			<- dependencies
|
|--README.md

```
## Results

- **cleaned_sales.csv** : Cleaned version of the raw dataset
- **monthly_sales.csv** : Aggregated monthly sales data
- ** Item Distribution.png** : Visulization of item sales makeup via pie chart
- ** revenue_by_region.png** Visulization of revenue (by region)

** Contributions

This is a personal learning project. Suggestion are welcome via issues or pull requests.