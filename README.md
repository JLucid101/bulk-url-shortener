# bulk-url-shortener
This Python script processes a list of long URLs from a text file, converts them into short URLs using the TinyURL API, and saves the results in an Excel file. It's a simple and efficient solution for bulk URL shortening.


Features
Bulk Processing: Handles multiple URLs in a single run.
Free API Integration: Uses TinyURL, a free service with no authentication required.
Output to Excel: Results are saved in a structured Excel file for easy sharing and storage.
Error Handling: Skips invalid URLs and logs any issues during the process.
Requirements
Make sure you have Python installed (version 3.7 or higher) along with the following Python libraries:

requests: For making API calls to TinyURL.
pandas: For handling data and creating Excel files.
openpyxl: For Excel file generation.
To install these dependencies, run:

bash
Copy code
pip install requests pandas openpyxl
Usage
1. Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/<your-username>/bulk-url-shortener.git
cd bulk-url-shortener
2. Prepare the Input File
Create a text file named long_urls.txt in the project directory.
Add one URL per line. Example:
arduino
Copy code
https://www.google.com
https://www.github.com
https://www.openai.com
3. Run the Script
Execute the script using Python:

bash
Copy code
python bulk_url_shortener.py
4. Check the Output
The script generates an Excel file named short_urls.xlsx in the same directory.
The file contains two columns:
Long URL
Short URL
Example Output
Long URL	Short URL
https://www.google.com	http://tinyurl.com/abcd1
https://www.github.com	http://tinyurl.com/wxyz2
Error Handling
If any URL cannot be processed, an error message will be printed to the console, and the script will continue processing the remaining URLs.
Ensure that the long_urls.txt file is formatted correctly and contains valid URLs.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality of this script.

License
See the LICENSE file for more details.

Acknowledgements
TinyURL for their free URL shortening service.
Python libraries: requests, pandas, and openpyxl.
