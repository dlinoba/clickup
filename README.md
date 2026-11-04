# ClickUp API Data Integration with Python and MySQL
Python-based ETL pipeline for extracting, transforming, and storing ClickUp data in a MySQL database using the ClickUp REST API and SQLAlchemy.

# Key Features
1.ClickUp API Authentication: Connects to the ClickUp REST API using token-based authentication.<br>
2.Space Retrieval: Retrieves all Spaces associated with the configured ClickUp team.<br>
3.Standalone List Retrieval: Fetches Lists that are not associated with any Folder.<br>
4.Folder Retrieval: Retrieves Folders within each Space.<br>
5.Folder List Retrieval: Fetches Lists contained within each Folder.<br>
6.Task Extraction: Iterates through all retrieved Lists to collect both active and archived tasks, handling paginated API responses.<br>
7.MySQL Data Persistence: Uses Python classes and SQLAlchemy to structure and persist the extracted data in a MySQL database.<br>

Architecture / Data Flow<br>
The project follows an ETL architecture to extract data from the ClickUp REST API, process it using Python, and store it in a MySQL relational database.<br>
<img width="779" height="697" alt="diagrama_arquitetura" src="https://github.com/user-attachments/assets/e0e82514-fdd7-412d-b516-fdaf2287fcce" />
