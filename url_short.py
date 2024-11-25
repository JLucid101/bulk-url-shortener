import requests
import pandas as pd

def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print(f"API Response for {long_url}: {response.text}")  # Debug 
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error shortening URL {long_url}: {e}")
        return None

def process_urls(input_file, output_file):
   
    with open(input_file, "r") as file:
        long_urls = [line.strip() for line in file if line.strip()]
    print("URLs read from file:", long_urls)  # Debug 

    
    result_data = []


    for long_url in long_urls:
        short_url = shorten_url(long_url)
        result_data.append({"Long URL": long_url, "Short URL": short_url})
        print("Current result_data:", result_data)  # Debug

    
    if not result_data:
        print("No data to write. Check input file or API responses.")
        return

    
    df = pd.DataFrame(result_data)
    print(df)  # Debug

    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Short URLs saved to {output_file}")

# File paths
input_file = "long_urls.txt"  # Input file containing long URLs
output_file = "short_urls.xlsx"  # Output Excel file

# Run the process
process_urls(input_file, output_file)
