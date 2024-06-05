
# Credit Card Fraud Dataset QueryBot
![WhatsApp Image 2024-06-02 at 11 22 26_5d34f905](https://github.com/arc-ch/Credit-Card-Dataset-QueryBot/assets/134518231/bac07cc3-1150-480b-9227-4fe1d50995bc)

![WhatsApp Image 2024-06-02 at 11 22 38_a0d5d3f6](https://github.com/arc-ch/Credit-Card-Dataset-QueryBot/assets/134518231/f2a708e0-221a-4500-b225-db1a9a0a8042)


## Overview
Welcome to the Credit Card Fraud Dataset QueryBot repository! This project is designed to allow users to interact with a credit card fraud dataset using natural language queries. The application leverages Streamlit for the frontend interface and Google PaLM for processing natural language to SQL conversions. This makes it easy to query the dataset without needing to write SQL manually.

## Features
- **Natural Language to SQL Conversion**: Convert human-readable questions into SQL queries.
- **Streamlit Interface**: User-friendly web interface to interact with the dataset.
- **Custom Response Parsing**: Displays dataframes, plots, and other results directly in the Streamlit app.

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/credit-card-fraud-querybot.git
    cd credit-card-fraud-querybot
    ```

3. **Set up the Google PaLM API key**:
    Replace `YOUR_API_KEY_HERE` in the script with your actual Google PaLM API key.

4. **Prepare the data**:
    - Ensure your dataset files are in the `data` directory.
    - The dataset files should be pickled pandas DataFrames.

## Usage

1. **Run the Streamlit application**:
    ```sh
    streamlit run app.py
    ```

2. **Interacting with the application**:
    - Open the Streamlit app in your browser.
    - Use the text area to input your natural language queries.
    - View the results directly in the app.


## Main Components
### streamlit_app.py
This is the main application file that contains the Streamlit app code, the logic to load the dataset, and the integration with the Google PaLM API for natural language query processing.

### data.py
This script contains functions to load and cache the dataset from pickled pandas DataFrames.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
