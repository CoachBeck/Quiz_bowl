import sqlite3

conn = sqlite3.connect("quiz_data.db")
cursor = conn.cursor()

questions = [
    # Quality and Productivity Systems
    ("What is the goal of Six Sigma?", "Reduce costs", "Reduce waste", "Reduce defects", "Increase speed", "C", "Quality and Productivity Systems"),
    ("What is the purpose of Lean systems?", "Maximize inventory", "Eliminate waste", "Increase defects", "Hire more staff", "B", "Quality and Productivity Systems"),
    ("What does JIT stand for?", "Just-In-Time", "Job in Transition", "Joint Input Task", "Justified Inventory Tracking", "A", "Quality and Productivity Systems"),
    ("Which chart is commonly used to visualize a process timeline?", "Fishbone", "Pareto", "Gantt", "Flow", "C", "Quality and Productivity Systems"),
    ("Which quality tool is also called a cause-and-effect diagram?", "Histogram", "Gantt chart", "Control chart", "Fishbone diagram", "D", "Quality and Productivity Systems"),
    ("Who developed the 14 Points of Management?", "Peter Drucker", "W. Edwards Deming", "Frederick Taylor", "Elon Musk", "B", "Quality and Productivity Systems"),
    ("What does PDCA stand for?", "Plan-Do-Check-Act", "Prepare-Develop-Control-Act", "Predict-Define-Create-Adjust", "Plan-Drive-Confirm-Analyze", "A", "Quality and Productivity Systems"),
    ("What does a flowchart represent?", "Task schedules", "Budget analysis", "Steps in a process", "Employee ratings", "C", "Quality and Productivity Systems"),
    ("What is poka-yoke?", "Employee evaluation", "A type of audit", "Error prevention technique", "Inventory check", "C", "Quality and Productivity Systems"),
    ("What is the aim of TQM?", "More marketing", "Lower prices", "Total quality improvement", "Continuous improvement", "D", "Quality and Productivity Systems"),

    # Business Strategy
    ("What is a SWOT analysis used for?", "Developing org charts", "Strategic planning", "Calculating costs", "Hiring staff", "B", "Business Strategy"),
    ("Which of Porter’s Five Forces focuses on pricing pressure?", "Supplier power", "Buyer power", "Substitutes", "Rivalry", "B", "Business Strategy"),
    ("What is the goal of a differentiation strategy?", "Lower prices", "Better logistics", "Uniqueness", "More suppliers", "C", "Business Strategy"),
    ("What is vertical integration?", "Going public", "Owning the supply chain", "Hiring executives", "Selling services", "B", "Business Strategy"),
    ("Who introduced the core competency concept?", "Elon Musk", "Michael Porter", "Prahalad and Hamel", "Peter Drucker", "C", "Business Strategy"),
    ("What is a vision statement?", "A financial report", "Short-term task", "Future-focused purpose", "Performance goal", "C", "Business Strategy"),
    ("What does VRIO stand for?", "Vision, Revenue, Insight, Objectives", "Value, Rarity, Imitability, Organization", "Value, Risk, Investment, Outlook", "Validate, Rank, Integrate, Optimize", "B", "Business Strategy"),
    ("What does the BCG Matrix evaluate?", "IT systems", "Employees", "Product portfolios", "Supplier relationships", "C", "Business Strategy"),
    ("What is the 'first-mover advantage'?", "Last company in a market", "Better management", "Being first to market", "Higher inventory", "C", "Business Strategy"),
    ("What is cost leadership?", "Competing on price", "Being first to market", "Being innovative", "Focusing on design", "A", "Business Strategy"),

    # Business Applications Development
    ("What does CRUD stand for?", "Create, Review, Undo, Debug", "Create, Read, Update, Delete", "Compute, Read, Upload, Download", "Compile, Run, Update, Deploy", "B", "Business Applications Development"),
    ("Which language is used for website structure?", "Python", "HTML", "SQL", "Java", "B", "Business Applications Development"),
    ("What is an API used for?", "Running GUIs", "Building hardware", "Connecting systems", "Compiling code", "C", "Business Applications Development"),
    ("What is a database?", "Email system", "Data warehouse", "Organized data collection", "Firewall", "C", "Business Applications Development"),
    ("What is GitHub?", "Video platform", "Code hosting service", "Data cleaner", "CRM software", "B", "Business Applications Development"),
    ("What is the role of version control?", "Speeding up the program", "Tracking code changes", "Improving GUI design", "User authentication", "B", "Business Applications Development"),
    ("What is a GUI?", "Graphical User Interface", "Generic Utility Input", "Global User Integration", "Graphic Upload Installer", "A", "Business Applications Development"),
    ("Which language is best for analyzing data?", "HTML", "JavaScript", "Python", "C++", "C", "Business Applications Development"),
    ("What is a framework?", "Code editor", "Library", "Pre-built code structure", "Operating system", "C", "Business Applications Development"),
    ("What is backend development?", "Making presentations", "Client-side code", "Server-side logic", "Photoshop work", "C", "Business Applications Development"),

    # Management Information Systems
    ("What does MIS stand for?", "Managed IT Systems", "Management Information Systems", "Mainframe Input Structure", "Modular Information Strategy", "B", "Management Information Systems"),
    ("What is an ERP system?", "Email Routing Protocol", "Enterprise Resource Planning", "External Revenue Predictor", "Enhanced Routing Platform", "B", "Management Information Systems"),
    ("What is the purpose of a TPS?", "Hiring workers", "Handling daily operations", "Storing emails", "Customer satisfaction", "B", "Management Information Systems"),
    ("What does a dashboard show?", "Employee hours", "Visual data insights", "Organizational chart", "Meeting schedule", "B", "Management Information Systems"),
    ("What is business intelligence?", "Marketing strategy", "Data entry", "Analyzing data for decision-making", "HR practices", "C", "Management Information Systems"),
    ("What is cloud computing?", "Remote server access", "Big data backup", "Spreadsheet sharing", "File deletion", "A", "Management Information Systems"),
    ("What does cybersecurity protect?", "Furniture", "User interfaces", "Data and systems", "Passwords only", "C", "Management Information Systems"),
    ("What is a DBMS?", "Data Bank Management Sheet", "Database Management System", "Distributed Base Model System", "Direct Business Model Software", "B", "Management Information Systems"),
    ("What is data integrity?", "Making data look good", "Data consistency and accuracy", "Hiding data", "Encrypting files", "B", "Management Information Systems"),
    ("What does a systems analyst do?", "Manages HR", "Builds marketing plans", "Designs and improves information systems", "Creates advertisements", "C", "Management Information Systems"),

    # Business Intelligence and Analytics
    ("What does BI stand for?", "Business Infrastructure", "Business Insight", "Business Intelligence", "Base Integration", "C", "Business Intelligence and Analytics"),
    ("What is data mining?", "Storing large datasets", "Extracting insights from data", "Building websites", "Securing files", "B", "Business Intelligence and Analytics"),
    ("What is a KPI?", "Key Performance Indicator", "Knowledge Program Integration", "Kinetic Project Info", "Known Public Index", "A", "Business Intelligence and Analytics"),
    ("What is a data warehouse?", "Physical storage unit", "Spreadsheet with macros", "Central data storage for reporting", "Smartphone app", "C", "Business Intelligence and Analytics"),
    ("What is predictive analytics?", "Guessing future weather", "Forecasting outcomes using data", "Finding system bugs", "Hacking detection", "B", "Business Intelligence and Analytics"),
    ("What is Tableau?", "Web browser", "BI dashboard tool", "Database engine", "Firewall program", "B", "Business Intelligence and Analytics"),
    ("What is machine learning?", "Hard coding behavior", "Algorithms learning from data", "Printing reports", "Manual data review", "B", "Business Intelligence and Analytics"),
    ("What is a heat map?", "Temperature graph", "Color-coded data visualization", "User login tracker", "Cloud tool", "B", "Business Intelligence and Analytics"),
    ("What is data visualization?", "Editing Excel sheets", "Graphically displaying data", "Hiding raw data", "Encrypting data", "B", "Business Intelligence and Analytics"),
    ("What is sentiment analysis?", "Checking customer feedback tone", "Password cracking", "Market size evaluation", "Product pricing", "A", "Business Intelligence and Analytics"),
]

# Insert questions
for q, a, b, c, d, correct, subject in questions:
    cursor.execute('''
        INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, subject)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (q, a, b, c, d, correct, subject))

conn.commit()
conn.close()
print(f"✅ {len(questions)} multiple choice questions added to quiz_data.db!")