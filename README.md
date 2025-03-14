# Travel-Track

## Overview
Travel-Track is a train ticket booking and management system developed using Python, Tkinter, and MySQL. It provides a user-friendly interface for booking tickets, checking PNR status, and web check-in.

## Features
- **User Authentication**: Secure login system using MySQL database.
- **Ticket Booking**: Allows users to book train tickets by selecting source, destination, date, class, and entering passenger details.
- **PNR Status Check**: Users can verify their booking details using a PNR number and Aadhar number.
- **Web Check-In**: Enables users to confirm their travel plans online by entering their PNR and contact number.
- **GUI Interface**: Built using Tkinter for an interactive experience.
- **Database Interaction**: MySQL is used to store user login details, ticket bookings, and check-in statuses.

## Technologies Used
- **Python** (Tkinter for GUI)
- **MySQL** (Database for storing user and booking data)

## Installation Guide
### Prerequisites
- Python installed on your system
- MySQL server installed and running

### Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Shubhaaaaam/Travel-Track.git
   cd Travel-Track
   ```
2. **Install Dependencies**
   ```sh
   pip install mysql-connector-python
   ```
3. **Set Up the Database**
   - Open MySQL and create a new database:
     ```sql
     CREATE DATABASE travel_track;
     ```
   - Create a login table to store user authentication details:
     ```sql
     CREATE TABLE info (
         userid VARCHAR(50) PRIMARY KEY,
         password VARCHAR(50) NOT NULL
     );
     ```
   - Import the provided SQL script (if available) to create additional tables for bookings and check-ins.
4. **Run the Application**
   ```sh
   python "main.py"
   ```

## Usage
- **Booking Tickets**: Enter travel details (source, destination, date, class, passenger details) to book a ticket and generate a PNR.
- **PNR Verification**: Verify booking details by entering the PNR and Aadhar number.
- **Web Check-In**: Confirm travel plans by entering the PNR and contact number. The system updates the check-in status as "Confirmed" (CNF) or "Cancelled" (CNL).


## Contact
For any queries, reach out via GitHub Issues or email the repository owner.

