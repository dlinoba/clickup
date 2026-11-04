# ClickUp API Data Integration with Python and MySQL
Python-based ETL pipeline for extracting, transforming, and storing ClickUp data in a MySQL database using the ClickUp REST API and SQLAlchemy.

# Key Features
1.ClickUp API Authentication: Connects to the ClickUp REST API using token-based authentication.
2.Space Retrieval: Retrieves all Spaces associated with the configured ClickUp team.
3.Standalone List Retrieval: Fetches Lists that are not associated with any Folder.
4.Folder Retrieval: Retrieves Folders within each Space.
5.Folder List Retrieval: Fetches Lists contained within each Folder.
6.Task Extraction: Iterates through all retrieved Lists to collect both active and archived tasks, handling paginated API responses.
7.MySQL Data Persistence: Uses Python classes and SQLAlchemy to structure and persist the extracted data in a MySQL database.
