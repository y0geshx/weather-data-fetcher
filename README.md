<div align="center">
	<img  src="https://github.com/user-attachments/assets/ab977bae-3d0a-423e-88c9-819dfed708e2">
</div>

# Weather Data Fetcher

This project fetches weather data for a list of cities using the OpenWeatherMap API. It retrieves both current city data and forecast data.

## Features

- Fetches current weather data for a list of cities.
- Fetches forecast data for each city.
- Displays the collected data in a readable format.
- Exports data in CSV, XML, HTML, and JSON formats.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library
- `tqdm` library

## Installation

1. Clone the repository:
    ```sh
	git clone https://github.com/y0geshx/weather-data-fetcher.git
    cd weather-data-fetcher
    ```
2. To activate a Python virtual environment in your project, follow these steps:

3. **Create a virtual environment** (if you haven't already):
    ```sh
    python -m venv venv
    ```
4. **Activate the virtual environment**:
    ```sh
    source venv/bin/activate
    ```
	After activating the virtual environment, you can install the required dependencies and run your scripts within this isolated environment.

5. Install the required libraries:
    ```sh
    pip install requests pandas tqdm
    ```
6. Or use:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set your OpenWeatherMap API key in the weather.py script:
    ```python
    API_KEY = 'your_api_key_here'
    ```

2. Prepare a CSV file with a list of cities. The CSV should have a column named `City`.

3. Run the script:
    ```sh
    python weather.py
    ```

4. The script will fetch and display the weather data for the listed cities.

5. Export the data in the desired format:
    ```python
    # Example for exporting data
    data.to_csv('weather_data.csv')
    data.to_json('weather_data.json')
    data.to_html('weather_data.html')
    data.to_xml('weather_data.xml')
    ```

## Example

Here is an example of how to use the script:

1. Create a CSV file named `in_cities.csv` with the following content:
    ```csv
    City
    London
    Paris
    New York
    ```

2. Run the script:
    ```sh
    python weather.py
    ```

3. The script will fetch and display the weather data for the listed cities.

4. Export the data in the desired format:
    ```python
    data.to_csv('weather_data.csv')
    data.to_json('weather_data.json')
    data.to_html('weather_data.html')
    data.to_xml('weather_data.xml')
    ```
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.