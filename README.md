Railway Booking System

Project Overview
The Railway Booking System is a comprehensive and dynamic reservation system designed to facilitate seamless train ticket booking and cancellation. It ensures real-time updates, passenger management, and train status tracking. The system efficiently integrates multiple data sources and provides a user-friendly front-end interface with images to enhance the booking experience.
Features
•	Real-Time Booking & Cancellation: The system updates availability instantly upon booking or cancellation.
•	Passenger Management: Stores and retrieves passenger details securely.
•	Train Management: Maintains train schedules, fare categories, and availability.
•	Live Seat Tracking: Monitors premium and general seat occupancy.
•	User-Friendly Interface: A visually appealing front-end for seamless interaction.


Database Structure
The system is built on multiple structured tables to efficiently manage reservations, train details, and passenger information.
1. Booking Table (booking.csv)
Column Name	Description
Passanger_ssn	Unique SSN of the passenger
Train_Number	Train number associated with booking
Ticket_Type	Type of ticket (Premium/General)
Staus	Booking status (Confirmed/Pending)

2. Passenger Table (Passenger.csv)
Column Name	Description
first_name	Passenger's first name
last_name	Passenger's last name
address	Passenger's address
city	City of residence
county	County of residence
phone	Contact number
SSN	Social Security Number (Unique ID)
bdate	Birth date

3. Train Table (Train.csv)
Column Name	Description
Train Number	Unique identifier for a train
Train Name	Name of the train
Premium Fair	Cost for premium seats
General Fair	Cost for general seats
Source Station	Departure station
Destination Station	Arrival station

4. Train Status Table (Train_status.csv)
Column Name	Description
TrainDate	Date of the train journey
TrainName	Name of the train
PremiumSeatsAvailable	Available premium seats
GenSeatsAvailable	Available general seats
PremiumSeatsOccupied	Number of occupied premium seats
GenSeatsOccupied	Number of occupied general seats

Project Files
File Name	Description
Code.py	Main script handling booking, cancellation, and updates
booked.csv	Stores records of confirmed bookings
Passenger.csv	Stores passenger details
RRS.db	Database file managing all system data
Train.csv	Stores train details, fares, and stations
Train_status.csv	Tracks real-time seat availability and train statuses

Installation & Setup
Prerequisites
•	Python 3.x
•	SQLite (for database management)
•	Pandas library for data handling
Steps to Run the Project
1.	Download the project files.
2.	Install dependencies using: 
3.	pip install pandas sqlite3
4.	Run Code.py to start the system: 
5.	python Code.py
6.	Follow the on-screen prompts to book or cancel tickets.

Front-End Design
The system includes an intuitive front-end interface with images to enhance the user experience. The UI allows users to:
•	Search for available trains.
•	Select ticket types (Premium/General).
•	View real-time seat availability.
•	Enter passenger details for booking.
•	Receive confirmation upon successful booking.

Future Enhancements
•	Online Payment Integration for hassle-free transactions.
•	User Authentication System for secure and personalized bookings.
•	Automated Alerts via email/SMS for booking updates.
•	Mobile Application for easy ticket booking on the go.

Conclusion
This Railway Booking System provides a robust, real-time, and user-friendly platform for managing train reservations. With its structured database, seamless user interface, and dynamic updates, it aims to enhance the railway booking experience for passengers and administrators alike.

