# Datasets

The following datasets are available in the repo:

## Sample

This the most simple dataset available.

| area    |  sales | profit | 
|:--------|-------:|-------:|
| North   |     5  |      2 |  
| East    |    25  |      8 |  
| West    |    15  |      6 |  
| South   |    20  |      5 |  
| Central |    10  |      3 |  

Metadata
- Filename: `sample.csv`
- Observations `(n)` : 5
- Dimensions `(p)`   : 3


## Churn

This is a sample dataset for a Telo aiming predicting customer behavior to retain them. The key target of the analysis is the churn feature - customers that left the service with the last month. Each row represents a customer, each column contains customer’s attributes described on the column Metadata.


|CustomerID|Gender|SeniorCitizen|Partner|Dependents|Tenure|PhoneService|MultipleLines   |InternetService|OnlineSecurity     |OnlineBackup       |DeviceProtection   |TechSupport        |StreamingTV        |StreamingMovies    |Contract      |PaperlessBilling|PaymentMethod            |MonthlyCharges|TotalCharges|Churn|
|----------|------|-------------|-------|----------|------|------------|----------------|---------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|--------------|----------------|-------------------------|--------------|------------|-----|
|7590-VHVEG|Female|0            |Yes    |No        |1     |No          |No phone service|DSL            |No                 |Yes                |No                 |No                 |No                 |No                 |Month-to-month|Yes             |Electronic check         |29.85         |29.85       |No   |
|5575-GNVDE|Male  |0            |No     |No        |34    |Yes         |No              |DSL            |Yes                |No                 |Yes                |No                 |No                 |No                 |One year      |No              |Mailed check             |56.95         |1889.5      |No   |
|3668-QPYBK|Male  |0            |No     |No        |2     |Yes         |No              |DSL            |Yes                |Yes                |No                 |No                 |No                 |No                 |Month-to-month|Yes             |Mailed check             |53.85         |108.15      |Yes  |
|7795-CFOCW|Male  |0            |No     |No        |45    |No          |No phone service|DSL            |Yes                |No                 |Yes                |Yes                |No                 |No                 |One year      |No              |Bank transfer (automatic)|42.3          |1840.75     |No   |
|9237-HQITU|Female|0            |No     |No        |2     |Yes         |No              |Fiber optic    |No                 |No                 |No                 |No                 |No                 |No                 |Month-to-month|Yes             |Electronic check         |70.7          |151.65      |Yes  |
|9305-CDSKC|Female|0            |No     |No        |8     |Yes         |Yes             |Fiber optic    |No                 |No                 |Yes                |No                 |Yes                |Yes                |Month-to-month|Yes             |Electronic check         |99.65         |820.5       |Yes  |
|1452-KIOVK|Male  |0            |No     |Yes       |22    |Yes         |Yes             |Fiber optic    |No                 |Yes                |No                 |No                 |Yes                |No                 |Month-to-month|Yes             |Credit card (automatic)  |89.1          |1949.4      |No   |


Data Columns

- Customer Account Information
  - `CustomerID`: Unique ID for the customer *(unique String)*?
  - `Churn`: Customers who left within the last month *(Yes or No)*?
  - `Tenure`: How long they’ve been a customer *(In months, Integer)*?
  - `Contract`: What type of contract do they have *(Month-to-month, One year, Two year)*?
  - `PaymentMethod`: What payment method is used by the customer *(Electronic check, Mailed check, Bank transfer, or Credit card)*?
  - `PaperlessBilling`: Whether the customer has subscribed to paperless billing *(Yes or No)*?
  - `MonthlyCharges`: What was the monthly charges for the customer (Amount, Float)?
  - `TotalCharges`: What were the total charges for the customer (Amount, Float)?
- Customer Demographics 
  - `Gender`: What is the gender of the customer *(Male or Female)*?
  - `SeniorCitizen`: Whether the customer is a Senior Citizen or not *(0 or 1)*?
  - `Partner`: Whether the customer has a partner *(Yes or No)*?
  - `Dependents`: Whether the customer has any dependents *(Yes or No)*?
- Customer Signed Up Service Status
  - `PhoneService`: Signed up for Phone Service *(Yes or No)*?
  - `MultipleLines`: Signed up for Multiple Lines *(Yes or No or No Phone Service)*?
  - `InternetService`: Signed up for Internet Service *(DSL or Fiber optic or No)*?
  - `OnlineSecurity`: Signed up for Online Security *(Yes or No or No internet service)*?
  - `OnlineBackup`: Signed up for Online Backup *(Yes or No or No internet service)*?
  - `DeviceProtection`: Signed up for Device Protection plan *(Yes or No or No internet service)*?
  - `TechSupport`: Signed up for Tech Support *(Yes or No or No internet service)*?
  - `StreamingTV`: Signed up for Streaming TV *(Yes or No or No internet service)*?
  - `StreamingMovies`: Signed up for Streaming Movies *(Yes or No or No internet service)*?

Metadata
- Filename: `churn.csv`
- Observations `(n)` : 7043
- Dimensions `(p)`   : 21

Source: Kaggle Telcom Customer Churn @ https://www.kaggle.com/blastchar/telco-customer-churn


## Notes

This dataset was inspired by the demonetisation of INR 500 and INR 1000 notes in India conducted in 2016.

| year    | type   |  denom |  value |   money | number |
|--------:|:-------|-------:|-------:|--------:|-------:|
| 1977    | Notes  |   0001 |      1 |    2.72 |  2.720 |
| 1977    | Notes  |   1000 |   1000 |    0.55 |  0.001 |
| 1977    | Notes  |   0002 |      2 |    1.48 |  0.740 |
| 1977    | Notes  |   0050 |     50 |    9.95 |  0.199 |
| ...     | ...    |    ... |    ... |     ... |    ... |
| 2015    | Notes  |   0500 |    500 | 7853.75 | 15.708 |
| 2015    | Notes  |   0001 |      1 |    3.09 |  3.090 |
| 2015    | Notes  |   0010 |     10 |  320.15 | 32.015 |
| 2015    | Notes  |   1000 |   1000 | 6325.68 |  6.326 |

Metadata
- Filename: `notes.csv`
- Observations `(n)`: 351
- Features `(p)`    : 6
  - `year`  : The year of circulation
  - `type`  : The type of currency
  - `denom` : The denomination of the currency
  - `value` : The face value of the currency
  - `money` : The monetary value of currency in circulation (in INR Billion)
  - `number`: The number of currency in circulation (in INR Billion)
- Source: It is taken from Reserve Bank of India’s - Handbook of Statistics on Indian Economy 2016. Within it, Table 160 deals with [Notes and Coins in Circulation](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=17293) and this dataset is only about the Notes circulation.


## Cars

A list of Indian cars and basic stats 

| brand   | model  |  price |   kmpl | type      |   bhp  |
|:--------|:-------|-------:|-------:|:----------|-------:|
| Tata    | Nano   |    199 |   23.9 | Hatchback |    38  |
| Suzuki  | Alto800|    248 |   22.7 | Hatchback |    47  |
| Hyundai | EON    |    302 |   21.1 | Hatchback |    55  |
| Nissan  | Datsun |    312 |   20.6 | Hatchback |    67  |
| ...     | ...    |    ... |    ... | ...       |   ...  |
| Suzuki  | Ciaz   |    725 |   20.7 | Sedan     |    91  |
| Skoda   | Rapid  |    756 |   15.0 | Sedan     |   104  |
| Hyundai | Verna  |    774 |   17.4 | Sedan     |   106  |
| VW      | Vento  |    785 |   16.1 | Sedan     |   104  |

Metadata
- Filename: `cars.csv`
- Observations `(n)`: 42
- Dimensions `(p)`  : 6
  - `brand`: brand
  - `model`: model name
  - `price`: price in '000 INR 
  - `kmpl` : efficiency of the car in km per liter 
  - `type` : type either Hatchback or Sedan
  - `bhp`  : brake horsepower 
- Source: Adapted from a car comparison website



## Vega Datasets

Additional datasets are available to play with from `vega_datasets` repository. You can access them as below.

```
from vega_datasets import data 
gapminder = data.gapminder()
gapminder.head()
```