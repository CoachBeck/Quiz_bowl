import sqlite3

conn = sqlite3.connect("quiz_data.db")
cursor = conn.cursor()

questions = [
    # Quality and Productivity Systems
    ("What does Six Sigma aim to reduce?", "Defects", "Quality and Productivity Systems"),
    ("What is the goal of Lean systems?", "Eliminate waste", "Quality and Productivity Systems"),
    ("What tool identifies the root cause of problems?", "Fishbone diagram", "Quality and Productivity Systems"),
    ("What does JIT stand for?", "Just-In-Time", "Quality and Productivity Systems"),
    ("Which chart tracks task progress in time?", "Gantt chart", "Quality and Productivity Systems"),
    ("What quality guru developed the 14 Points?", "W. Edwards Deming", "Quality and Productivity Systems"),
    ("What does PDCA stand for?", "Plan-Do-Check-Act", "Quality and Productivity Systems"),
    ("Which tool displays process steps visually?", "Flowchart", "Quality and Productivity Systems"),
    ("What is poka-yoke?", "Error prevention", "Quality and Productivity Systems"),
    ("What is the main goal of Total Quality Management?", "Continuous improvement", "Quality and Productivity Systems"),

    # Business Strategy
    ("What is a SWOT analysis used for?", "Strategic planning", "Business Strategy"),
    ("What are Porter's Five Forces used to analyze?", "Industry competition", "Business Strategy"),
    ("What is the focus of a differentiation strategy?", "Uniqueness", "Business Strategy"),
    ("What is vertical integration?", "Owning the supply chain", "Business Strategy"),
    ("Who popularized the concept of core competencies?", "Prahalad and Hamel", "Business Strategy"),
    ("What is a vision statement?", "A future-oriented goal", "Business Strategy"),
    ("What does VRIO stand for?", "Value, Rarity, Imitability, Organization", "Business Strategy"),
    ("What is the BCG Matrix used for?", "Portfolio analysis", "Business Strategy"),
    ("What does 'first-mover advantage' mean?", "Benefit from being first to market", "Business Strategy"),
    ("What is cost leadership?", "Competing with the lowest price", "Business Strategy"),

    # Business Applications Development
    ("What is a database?", "An organized collection of data", "Business Applications Development"),
    ("What does CRUD stand for?", "Create, Read, Update, Delete", "Business Applications Development"),
    ("What language is used for web page structure?", "HTML", "Business Applications Development"),
    ("What is the backend of an application?", "Server-side logic", "Business Applications Development"),
    ("What is version control used for?", "Tracking code changes", "Business Applications Development"),
    ("What is GitHub?", "A platform for code collaboration", "Business Applications Development"),
    ("What is the purpose of an API?", "Connect systems and share data", "Business Applications Development"),
    ("What is a framework?", "A prebuilt code structure", "Business Applications Development"),
    ("What language is often used for data analysis?", "Python", "Business Applications Development"),
    ("What is a GUI?", "Graphical User Interface", "Business Applications Development"),

    # Management Information Systems
    ("What does MIS stand for?", "Management Information Systems", "Management Information Systems"),
    ("What is an ERP system?", "Enterprise Resource Planning", "Management Information Systems"),
    ("What does a transaction processing system do?", "Handles daily business operations", "Management Information Systems"),
    ("What is business intelligence?", "Analyzing data for decisions", "Management Information Systems"),
    ("What is the role of a systems analyst?", "Designing and improving information systems", "Management Information Systems"),
    ("What is a database management system?", "Software to manage databases", "Management Information Systems"),
    ("What is cloud computing?", "Accessing services over the internet", "Management Information Systems"),
    ("What is cybersecurity?", "Protecting information systems", "Management Information Systems"),
    ("What is data integrity?", "Accuracy and consistency of data", "Management Information Systems"),
    ("What is a dashboard in MIS?", "Visual display of key data", "Management Information Systems"),

    # Business Intelligence and Analytics
    ("What does BI stand for?", "Business Intelligence", "Business Intelligence and Analytics"),
    ("What is data mining?", "Finding patterns in data", "Business Intelligence and Analytics"),
    ("What is a data warehouse?", "Central storage for business data", "Business Intelligence and Analytics"),
    ("What does a KPI measure?", "Key performance", "Business Intelligence and Analytics"),
    ("What is predictive analytics?", "Forecasting future outcomes", "Business Intelligence and Analytics"),
    ("What is data visualization?", "Graphically displaying data", "Business Intelligence and Analytics"),
    ("What is a heat map?", "Color-coded data visualization", "Business Intelligence and Analytics"),
    ("What is machine learning?", "Algorithms that learn from data", "Business Intelligence and Analytics"),
    ("What is sentiment analysis?", "Evaluating opinion in text", "Business Intelligence and Analytics"),
    ("What tool is commonly used for BI dashboards?", "Tableau", "Business Intelligence and Analytics"),
]

# Insert all questions into the DB
for q, a, s in questions:
    cursor.execute("INSERT INTO questions (question, answer, subject) VALUES (?, ?, ?)", (q, a, s))

conn.commit()
conn.close()
print(f"✅ {len(questions)} questions added to quiz_data.db!")