<body>
  <h1>
    <img src="https://i.ibb.co/853WF7T/icon.jpg" alt="AeroNet Logo", style="height:30px">
    AeroNet
  </h1>
  <p>AeroNet is a concept project designed with the aim of developing a realistic semi-autonomous Air Traffic Management (ATM) system. The primary objective is to alleviate the workload of Air Traffic Controllers (ATCs) by automating routine tasks and providing intelligent decision support. By streamlining operations and enhancing situational awareness, AeroNet seeks to elevate the safety and efficiency of airspace management </p>

  <h2>Project Objectives</h2>
  <ul>
    <li>Reducing workload of  ATCs, allowing more room for critical-thinking when crucial.</li>
    <li>Streamlining the process of deciding flight paths</li>
    <li>Preventing mid-air collisions</li>
    <li>Providing effective guidance on navigation</li>
  </ul>

  <h2>System Features</h2>
  <ul>
    <li>Autonomous flight guidance</li>
    <li>Real-time data analysis</li>
    <li>Collision addressing system</li>
    <li>NAVAID integration</li>
  </ul>

  <h2>Technology Stack</h2>
  <ul>
    <li>Front-end: Python Tkinter</li>
    <li>Back-end: Python with MySQL database</li>
    <li>Programming languages: Python</li>
    <li>Libraries:
      <ul>
        <li>mysql-connector-python8.0.0</li>
        <li>numpy 2.1.0</li>
        <li>pillow 10.2.0</li>
        <li>tkinter</li>
        <li>math</li>
        <li>random</li>
        <li>heapq</li>
      </ul>
    </li>
  </ul>

  <h2>Hardware/Software Requirements</h2>
  <ul>
    <li>Operating System: Windows 10/11 or above</li>
    <li>Platform: Python IDLE 3.10.1 or similar IDE</li>
    <li>Database: MySQL</li>
    <li>Processor: Octa-core or above (recommended)</li>
    <li>Hard Disk: 100 GB or above</li>
    <li>RAM: 8 GB or above (recommended)</li>
  </ul>

  <h2>Scope and Limitations</h2>
  <p>Designed for simulation and research purposes. Integrates seamlessly with human ATCs for handling emergencies. Future potential for real-world integration with aircraft flight computers.</p>
  <p>Limitations: May not account for all potential emergency scenarios.</p>

  <h2>Airspace Design</h2>
  <ol> <li>1. Two parallel runways 09 L and 27 R, both in N-S direction.</li>
  <li> 2. Tiered structure of waypoints (20 total) strategically arranged for optimized air traffic flow and enhanced safety.
    <ul>
      <li>Primary Waypoints (12): Distance - 25 nautical miles</li>
      <li>Secondary Waypoints (6): Distance - 15 nautical miles</li>
      <li>Tertiary Waypoints (2): Distance - 5 nautical miles</li>
    </ul>
     This approach ensures efficient routing and avoids congestion within the airspace.</li>

  </ol>
    <img src="https://i.ibb.co/XCjfr3R/image.png" alt="Airspace Design">
  </p>

  <h2>Getting Started</h2>
  <ol>
    <li>Install the required libraries (`pip install mysql-connector-python8.0.0 numpy pillow`).</li>
    <li>Set up a MySQL database.</li>
    <li>Configure database connection details in the code.</li>
    <li>Run the main script (`python main.py`).</li>
  </ol>

  <h2>Contributing</h2>
  <p>We welcome contributions to this project! Please create a pull request on GitHub for any bug fixes, enhancements, or new features.</p>
</body>
</html>
