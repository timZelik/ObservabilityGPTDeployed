# ObservabilityGPT 

## Overview
The ObservabilityGPT Dashboard is a Streamlit-based web application designed to provide intuitive and interactive access to Azure Application Insights data. It leverages a natural language processing interface to allow users to retrieve and visualize application insights data efficiently.

## Features
- **Natural Language Queries**: Users can input natural language queries to fetch data from Azure Application Insights.
- **Dynamic Data Visualization**: The dashboard dynamically generates charts and tables based on the query results.
- **Historical Query Access**: Users can view and interact with a history of their queries and responses.
- **Responsive UI**: A clean and user-friendly interface, ensuring an engaging user experience.

## Installation
To set up the ObservabilityGPT Dashboard, follow these steps:

1. **Clone the Repository**:
git clone https://github.com/timZelik/ObservabilityGPT.git
2. **Install Required Packages**:
Ensure you have Python 3.6+ installed, then install the necessary packages:
pip install streamlit pandas
3. **Environment Variables**:
Set up the necessary environment variables for Azure OpenAI access and other configurations.

## Usage
To run the ObservabilityGPT Dashboard:

1. Navigate to the project directory:
cd ObservabilityGPT
2. Run the Streamlit application:
streamlit run dashboard.py

## Functionality Details
- **Data Retrieval**: The dashboard processes natural language queries using Azure OpenAI and retrieves relevant data from Azure Application Insights.
- **Charts and Tables**: Based on the data fetched, it generates and displays data in various forms, including tables and different types of charts.
- **Interaction History**: Users can review their past queries and responses, and interact with them for further insights.

## Contributing
Contributions to the ObservabilityGPT Dashboard are welcome. Please read the contributing guidelines before submitting your pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact
For any queries or collaborations, feel free to contact Tim Zelikovsky at timzelikw@gmail.com

## Acknowledgements
Shout out to Senior Software Engineer Madhukar Anugu on the BlockWorks Online Team at H&R Block for mentoring me and guiding me through the development of this project. Thank you to my Manager Tyler Yoder for encouraging me to follow through with this tool.

