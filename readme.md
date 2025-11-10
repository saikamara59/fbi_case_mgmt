# 🕵️‍♂️ FBI Case Management System (AI Facial Recognition)

## 🔍 Overview
The **FBI Case Management System** is a full-stack web application designed to help agencies manage, analyze, and track criminal cases efficiently.  
This system integrates **AI-powered facial recognition** to identify and match suspect images in real time, enhancing investigative workflows and case accuracy.

Built with scalability, security, and real-world use cases in mind — this project demonstrates how AI can streamline case tracking and evidence management in law enforcement and GovTech sectors.

---

## ⚙️ Features
- 🧠 **AI Facial Recognition:** Automatically detects and matches suspect faces using image input.  
- 🗂️ **Case Management:** Create, update, and organize case files securely.  
- 🔒 **User Authentication:** Role-based access using JWT for secure operations.  
- 🧩 **RESTful API Design:** Modular Flask backend with structured endpoints.  
- 🐳 **Dockerized Environment:** Consistent and portable deployment setup.  
- 🗃️ **PostgreSQL Database:** Secure and scalable relational data storage.  
- 📜 **Logging & Auditing:** Track user actions and system performance for accountability.  

---

## 🧠 Tech Stack
**Frontend:** React (Planned for integration)  
**Backend:** Flask (Python)  
**Database:** PostgreSQL  
**AI Engine:** Face Recognition (dlib / face_recognition Python library)  
**Containerization:** Docker, docker-compose  
**API Documentation:** Swagger  
**Authentication:** JWT  

---

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL (optional for local testing)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saikamara59/fbi_case_mgmt.git
   cd fbi_case_mgmt

2.	Set up environment variables
Create a .env file in the root directory:
 DATABASE_URL=postgresql://username:password@db:5432/fbi_cases
SECRET_KEY=your_secret_key

3.	Run with Docker
   docker compose up --build

4. Access the app
Visit: http://localhost:5000￼

⸻

🧩 API Endpoints (Sample)

Method
Endpoint
Description
POST
/register
Register a new user
POST
/login
Authenticate user and get JWT
GET
/cases
Retrieve all cases
POST
/cases
Add a new case
POST
/add-suspect-face
Upload and register a suspect image
POST
/match-face
Match an image against database records


🧠 AI Facial Recognition Logic
	•	Uses the face_recognition library (built on dlib) to encode facial features.
	•	Stores encodings in PostgreSQL for efficient matching.
	•	Compares uploaded images using Euclidean distance between encodings.
	•	Returns match results with confidence scores.

🧰 Future Enhancements
	•	Integrate React frontend dashboard.
	•	Add case analytics and visualization with Chart.js.
	•	Implement multi-level user access (Admin, Investigator, Analyst).
	•	Deploy using Render or AWS ECS.
	•	Expand to include object and text recognition in case files.


🛡️ Disclaimer

This project is a personal portfolio project built for educational and demonstration purposes.
It is not affiliated with or endorsed by the FBI or any government entity.

⭐ Support

If you found this project interesting or useful, please ⭐ the repository — it helps others discover it and supports my journey as an aspiring GovTech software engineer!

