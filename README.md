# Stock Price Filter ETL Project

This ETL (Extract, Transform, Load) project is designed to help users filter stocks based on a specified price threshold for further analysis and potential investment. By setting a target price (e.g., 40 rupees), the system retrieves all stocks with prices below that threshold, allowing users to identify investment opportunities in lower-priced stocks.

## Key Features

- **Dynamic Stock Price Filtering**: Filter stocks based on user-specified price criteria (e.g., below 40 rupees).
- **Automated Data Fetching**: Uses API requests to retrieve real-time stock prices.
- **Secure Data Handling**: Includes password validation for secure user access.
- **PostgreSQL Integration**: Stores stock price data efficiently using PostgreSQL.
- **Data Transformation**: The project cleans and processes raw stock price data for analysis.
- **SQL Queries**: Leverages SQL to filter and retrieve relevant stock price information.

## Technologies Used

- **Python**: Core scripting language for ETL operations.
- **PostgreSQL**: Database for storing and managing stock price data.
- **API Requests**: Fetching real-time stock prices from external APIs.
- **SQL**: Querying the database for specific stock price conditions.
- **Password Validation**: Ensures secure user access.

## Usage

1. Set your PostgresSQL database credential in 'Backend_Crypto.py' file.
2. Set your desired stock price threshold (e.g., below 40 rupees).
3. The system fetches real-time stock prices and filters out those that meet the criteria.
4. Filtered data is stored in PostgreSQL for further analysis.
5. The results can be queried and analyzed to make informed investment decisions.
