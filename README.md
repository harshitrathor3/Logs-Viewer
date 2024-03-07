<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">Logs Viewer</h3>
</div>


![ss1](https://github.com/dyte-submissions/november-2023-hiring-harshitrathor3/assets/105155118/5bb94ea4-0a5a-4381-8043-36c02995085e)


<!-- ABOUT THE PROJECT -->
## About The Project

A log ingestion system that efficiently handles vast volumes of log data and offers a simple interface for querying this data using full-text search or specific field filters.


<!-- BUILT WITH -->
### Built With

- [Python 3.10.10](https://www.python.org/)
- make sure you are using the same Python version otherwise you may get errors

  
### Installation

Clone the repo
   ```sh
   git clone https://github.com/your_username/log-ingestor.git
   ```
Create virtual environment
   ```
   python -m venv venv
   ```
Activate the virtual environment

this command sometimes fails in Powershell in Windows so make use of the command prompt if you have a problem with the power shell
   ```
   venv\Scripts\activate
   ```
Install required libraries
   ```
   pip install -r requirements.txt
   ```
You won't need to set up any database because I am using the cloud database.


You can now start the server using this and your script to call the POST API running at http://127.0.0.1:3000.
```
py run.py
```
- for query purposes, you can start searching from the form given. Just use one or more than one filter and hit submit.
- your result will be ready right there on that page only.

A sample log injector file is present in the code for your reference named injesting_data_sample.py. You can simply run this script and data is automatically stored in MySQL and Mongo DB Cloud database.


### USP

- Volume: Yes my system is capable of handling massive logs.
- Speed: I have created indexed in both MySQL and MongoDB so the search results will be much faster.
- Scalability: The cloud database can be changed by just changing a single line in the whole code. (i.e. a variable in the config.py file). The system is very easily scalable and currently uses a free-tier cloud database.
- Usability: I have created a user-friendly interface so that you can easily search for logs.
- Readability: The code consists of comments so it's easily readable and understandable.

### Features Included
- User-friendly UI to search for logs
- Included filters based on each column given
- Very efficient and quick search results with indexes on database columns
- Hybrid solution with MySQL + Mongo DB cloud database
- Very easily scalable

### Advanced Features Included
- Allowing combining multiple filters.
- Provided real-time log ingestion and searching capabilities.


I have tested the system on all sample queries.

### Important
Please reach out to me if you face any issue in setting up the environment, running the code, understanding any part of the code, or anything else.
<p>Email: <a href='harshitrathorelink@gmail.com'>harshitrathorelink@gmail.com</a></p>
<p>Mobile: +91-9926546160</p>
