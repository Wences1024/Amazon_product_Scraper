# Amazon Product Scraper

#### Description:

The Amazon Product Scraper is a Python script designed to simplify the process of searching for products on Amazon.co.uk. This project aims to provide a convenient way for users to find desired items on Amazon without the need for manual browsing.

#### How to Use:

To use the Amazon Product Scraper, follow these simple instructions:

1. Clone or download the project repository to your local machine.

2. Ensure that you have Python installed on your system. If not, you can download it from the official Python website: [Python.org](https://www.python.org/).

3. Install the required dependencies by running the following command in your terminal or command prompt:
   
pip install -r requirements.txt


4. Once the dependencies are installed, you can run the script by executing the following command:

python amazon_scraper.py -i [item_name] -n [quantity] -p [True/False]


Replace `[item_name]` with the name of the product you want to search for, `[quantity]` with the number of items to retrieve (if not specify only 1 product will be prenseted), and `[True/False]` with either `True` or `False` to specify whether you want to print the item information to the terminal.

5. Sit back and let the script do the work! Once the search is complete, you'll receive a message thanking you for using the script, and the results will be displayed in the terminal or command prompt and your csv file with all the information (Product name, price and URL).

### Functionality:

The script offers several features to enhance the user experience:

1. **Command-Line Interface:** Users can specify the item they want to search for and the number of items to retrieve directly from the command line using arguments. This approach eliminates the need for manual input, streamlining the search process.

2. **Web Scraping:** Leveraging the BeautifulSoup and Selenium libraries, the script dynamically scrapes product information from Amazon.co.uk. It navigates through search result pages, extracts relevant data such as product names, prices, and URLs, and stores them for further processing. By automating this task, users can quickly gather comprehensive information about multiple products.

3. **Translation:** The script supports translation of search queries using the Google Translate API. Users can input search terms in their preferred language, and the script will translate them to English before executing the search on Amazon.co.uk. This feature facilitates accessibility for non-English speakers, allowing them to conduct searches effectively.

4. **CSV Export:** The retrieved product information is exported to a CSV file named "amazon_products.csv". This file includes columns for product name, price, and URL, providing users with a structured format for analyzing the data. By exporting the results to a CSV file, users can easily manipulate the data or integrate it into other applications for further analysis or reporting.

5. **Curious Gestures:** The script employs a curious gesture for the user's amusement and engagement. Upon completion of the search, a whimsical touch is added by incorporating the "cowsay" library, which displays a playful ASCII art of a cow along with a synthesized message that says, "Thanks for using this script. Here are the results." This unique gesture not only conveys gratitude to the user but also adds an element of surprise and delight to the script's output. Subsequently, the search results are presented in the terminal for the user's convenience and enjoyment.

### Design Choices:

- **Error Handling:** The script incorporates try-except blocks to handle potential errors gracefully, such as invalid user input or permission issues when writing to files. This robust error handling mechanism ensures a smoother user experience by providing informative error messages and preventing unexpected crashes.

- **Argument Parsing:** The argparse library is used for parsing command-line arguments, enabling users to customize their search criteria without modifying the script itself. By providing a flexible interface for specifying search parameters, the script enhances usability and accommodates diverse user preferences.

- **Optimized Web Scraping:** To minimize resource usage and maximize efficiency, the script iterates through search result pages within a single browser session. This approach avoids the overhead of repeatedly opening and closing browser windows, resulting in faster execution times and a more responsive user experience.

- **Feedback Mechanisms:** The use of text-based feedback (cowsay) and audio feedback (pyttsx3) enhances user engagement and provides a more interactive experience. These feedback mechanisms not only convey information effectively but also add a touch of personality to the script's output, making it more enjoyable to use.

### Conclusion:

The Amazon Product Scraper project embodies my intention to create a practical tool for everyday tasks, such as searching for items online. Drawing inspiration from concepts covered in programming courses, I implemented robust error handling using try-except blocks to ensure smooth script execution even in the face of unexpected errors. Additionally, I integrated the argparse library to facilitate user interaction, allowing users to input search parameters directly from the command line without relying on traditional input methods like "input()".

During the development process, I encountered challenges in organizing functions efficiently, particularly due to the nature of web scraping, where multiple browser instances are opened and closed. To address this, I optimized the script to minimize resource usage and maximize efficiency by iterating through search result pages within a single browser session. This approach significantly improves performance and responsiveness, enhancing the overall user experience.

Furthermore, I leveraged the power of the csv library to easily store and organize retrieved product information in a structured format. This enables users to analyze the data or integrate it into other applications seamlessly, adding value and versatility to the script's functionality.

Lastly, I found joy in experimenting with the "cowsay" and "pyttsx3" libraries, which added a playful element to the script's output. Witnessing the animated ASCII art of a cow and hearing the synthesized voice reading out the results provided a fun and interactive learning experience. These libraries not only enhanced the script's functionality but also contributed to a more engaging and enjoyable user interaction.

In conclusion, the Amazon Product Scraper represents a culmination of technical skills, creativity, and a passion for exploring new possibilities in Python programming. By combining practical utility with whimsical touches, the script aims to simplify online shopping tasks while fostering curiosity and delight among users.
