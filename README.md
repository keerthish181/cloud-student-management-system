# Cloud-Based Student Management System

This project is a simple cloud-based application that demonstrates how to store and retrieve data using a cloud-hosted database.

## Project Overview
The application allows users to add and view student records through a Python-based command-line interface. All data is securely stored in an Azure SQL Database, ensuring centralized, reliable, and scalable data management.

## Technologies Used
- Microsoft Azure (Azure SQL Database)
- Python
- ODBC Driver for SQL Server
- Azure Portal

## Features
- Add student details
- View stored student records
- Secure cloud database connectivity
- Real-time data storage and retrieval

## How It Works
1. Azure SQL Database is created using Azure Portal.
2. Firewall and authentication are configured for secure access.
3. Python application connects to Azure SQL using ODBC.
4. Student data is inserted and retrieved from the cloud database.

## Real-World Use Case
This type of system is used by educational institutions and organizations to manage user data centrally in the cloud, ensuring scalability, security, and availability.

## How to Run
1. Install Python and ODBC Driver for SQL Server
2. Update database credentials in `app.py`
3. Run the application:
