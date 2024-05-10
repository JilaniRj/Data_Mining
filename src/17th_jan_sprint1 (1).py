#!/usr/bin/env python
# coding: utf-8

# Simulation start and end time
# 

# In[1]:


#importing required libraries to execute the task.
import datetime

# Set Simulation Start Time
start_date = datetime.datetime(2024, 1, 1, 0, 0, 0)  # Year, Month, Day, Hour, Minute, Second

# Set Simulation End Time
simulation_duration_days = 365  # 1 year(sample)
end_date = start_date + datetime.timedelta(days=simulation_duration_days)

# Print Start and End Times
print("Simulation Start Time:", start_date)
print("Simulation End Time:", end_date)


# # Define time increments for simulation steps
# 

# In[ ]:


#SIMULATION STEPS


# In[ ]:


"""1. Problem Definition:
Clearly define the problem that the simulation aims to address. Identify the objectives, constraints, and key performance 
indicators (KPIs) to measure the success of the simulation.

2. Modeling:
Develop a mathematical or computational model that represents the real-world system being simulated. Define the entities,
variables, and relationships within the system. Choose an appropriate simulation paradigm (e.g., discrete-event simulation,
                                                                                        continuous simulation).
3. Input Data Generation:
Collect or generate the input data required for the simulation. This may include historical data, statistical distributions,
or other parameters that influence the behavior of the system.

4. Initialization:
Set the initial conditions of the simulation, including the starting values of variables, states of entities, and any other
relevant parameters.
    
5. Time Management:
Define the simulation time frame and time increments. Manage the simulation clock and progress through time steps or events.

6. State Update:
Update the state of the system based on the events or continuous processes. This involves calculating changes in variables,
entity states, or other relevant parameters.

7. Data Logging:
Log relevant simulation data at specified intervals or when significant events occur. This data is crucial for analysis,
validation, and performance evaluation.

8. Condition Checking:
Check conditions or constraints to determine if specific actions need to be taken. This could involve decision-making based on
predefined rules or criteria.

9. Output Generation:
Generate output data that reflects the state of the system at different points in time. This output may include performance
metrics, visualizations, or reports.

10. Analysis and Validation:
Analyze the simulation results to assess the system's behavior, evaluate performance metrics, and validate the simulation
against real-world data or expectations.

11.Optimization (if applicable):
If the simulation aims to optimize certain parameters, implement optimization algorithms or strategies to improve system
performance based on the simulation results.

12. Scenario Exploration (if applicable):
Explore different scenarios by varying input parameters or conditions to understand how the system responds to different
situations.

13. Documentation:
Document the simulation process, including assumptions, limitations, and any adjustments made during the modeling and execution
phases. This documentation is essential for reproducibility and future reference.

14. Conclusion and Reporting:
Draw conclusions from the simulation results and prepare a final report summarizing key findings, insights, and recommendations."""


# In[2]:


# Define Simulation Time Increment
time_increment_hours = 1  # Example: 1 hour time increment

# Define Simulation Duration
simulation_duration_days = 365  # Example: 1 year simulation

# Calculate the Number of Steps
num_steps = int((simulation_duration_days * 24) / time_increment_hours)  # Convert days to hours

# Print Simulation Parameters
print("Time Increment:", time_increment_hours, "hours")
print("Number of Simulation Steps:", num_steps)


# # Decide if there is any randomization in simulation
# 

# # breakdown hours

# In[1]:


#importing required libraries
import random
#function to simulate breakdown hours
def simulate_breakdown():
    # Set the fixed breakdown hours to 3(as per mm data)
    fixed_breakdown_hours = 3

    # Introduce randomness for breakdown duration
    random_factor = random.uniform(0.8, 1.2)  # data to be provided regarding randomness
    random_breakdown_hours = round(fixed_breakdown_hours * random_factor)

    return random_breakdown_hours

# Example simulation
for _ in range(10):#(require number of steps)
    hours = simulate_breakdown()
    print(f"Simulated breakdown hours: {hours}")


# # variation in resource distribution

# Gold ore

# In[2]:


#gold ore
import random

# Example: Introduce randomization to simulate variations in ore grades
base_ore_grade = 4.56 

# Function to simulate random ore grade variation
def simulate_ore_grade():
    variability = 0.01  # Example: 1% variability
    random_factor = 1 + random.uniform(-variability, variability)
    return base_ore_grade * random_factor

# Example usage
randomized_ore_grade = simulate_ore_grade()
print("Randomized Ore Grade:", randomized_ore_grade)


# siver ore

# In[3]:


#silver ore
import random

# Example: Introduce randomization to simulate variations in ore grades
base_ore_grade = 92 

# Function to simulate random ore grade variation
def simulate_ore_grade():
    variability = 0.1  # Example: 10% variability
    random_factor = 1 + random.uniform(-variability, variability)
    return base_ore_grade * random_factor

# Example usage
randomized_ore_grade = simulate_ore_grade()
print("Randomized Ore Grade:", randomized_ore_grade)


# zinc ore

# In[4]:


#zinc ore
import random

# Example: Introduce randomization to simulate variations in ore grades
base_ore_grade = 7.8 

# Function to simulate random ore grade variation
def simulate_ore_grade():
    variability = 0.01  # Example: 1% variability
    random_factor = 1 + random.uniform(-variability, variability)
    return base_ore_grade * random_factor

# Example usage
randomized_ore_grade = simulate_ore_grade()
print("Randomized Ore Grade:", randomized_ore_grade)


# iron ore

# In[5]:


#Iron ore
import random

# Example: Introduce randomization to simulate variations in ore grades
base_ore_grade = 62 

# Function to simulate random ore grade variation
def simulate_ore_grade():
    variability = 0.1  # Example: 10% variability
    random_factor = 1 + random.uniform(-variability, variability)
    return base_ore_grade * random_factor

# Example usage
randomized_ore_grade = simulate_ore_grade()
print("Randomized Ore Grade:", randomized_ore_grade)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Define KPI

#  KPI stands for Key Performance Indicator. A KPI is a measurable value that demonstrates how effectively a company or an
# #organization is achieving its key business objectives. KPIs are used to evaluate the success or performance of a particular
# #activity, process, or overall business.

# In[ ]:


# 1. Relevance: KPIs are directly tied to the organization's goals and objectives. They reflect critical success factors that are 
 #   important for the organization's overall performance.

#2. Measurability: KPIs must be quantifiable and measurable. This involves having a clear, defined method for collecting and 
 #   analyzing data related to the KPI.

#3. Specificity: KPIs should be specific and well-defined, providing a clear understanding of what is being measured and why it 
 #   is important.

#4. Timeliness: KPIs are often associated with a specific timeframe, allowing organizations to track progress over time and make 
 #   informed decisions based on recent performance.

#5. Actionability: KPIs should provide insights that can drive action and decision-making. They help organizations identify 
 #   areas for improvement or areas where they are excelling.


# In[ ]:


#Operational KPIs:

#Overall equipment effectiveness (OEE)
#Cycle time
#Inventory turnover


# # Identify KPIs to measure the success of simulation
# 

# In[ ]:


"""Simulation Accuracy:

Objective: To assess how well the simulation replicates the real-world system.
KPIs:
Deviation between simulated and actual data.
Root Mean Square Error (RMSE) or other statistical measures of accuracy.
Model Validation:

Objective: To verify that the simulation model accurately represents the system it is simulating.
KPIs:
Comparison of simulated results with historical or empirical data.
Validation against known benchmarks.
Resource Utilization:

Objective: To optimize the use of resources within the simulated system.
KPIs:
Equipment utilization rates.
Workforce productivity.
Efficient use of available materials.
Optimization Effectiveness:

Objective: To evaluate the success of optimization strategies implemented in the simulation.
KPIs:
Cost reduction achieved through optimization.
Increased production or throughput.
Scenario Analysis:

Objective: To explore different scenarios and assess their impact on the system.
KPIs:
Identification of optimal scenarios.
Sensitivity analysis results.
Decision Support:

Objective: To evaluate the value of the simulation in supporting decision-making.
KPIs:
Timeliness of decision-making based on simulation results.
Number of decisions influenced by simulation insights.
Model Complexity:

Objective: To assess the appropriateness of the simulation model's complexity.
KPIs:
Model computation time.
Trade-off between model complexity and accuracy.
Stakeholder Satisfaction:

Objective: To measure the satisfaction of stakeholders with the simulation results.
KPIs:
Feedback from decision-makers.
User satisfaction surveys.
Robustness:

Objective: To evaluate the ability of the simulation to handle uncertainties and variations.
KPIs:
Performance under different input scenarios.
Resilience to changes in model parameters.
Communication Effectiveness:

Objective: To assess how well simulation results are communicated to stakeholders.
KPIs:
Clarity of simulation reports.
Understanding of simulation outputs by non-technical stakeholders."""


# In[ ]:





# In[16]:


#importing required libraries
import random
#creating class
class OreExtractionSimulation:
    def __init__(self, total_simulation_hours):#creating constructor
        self.total_simulation_hours = total_simulation_hours
        self.ore_extraction_rate = 0
        self.equipment_downtime = 0
        
    def simulate(self):
        for hour in range(self.total_simulation_hours):
            # Simulate ore extraction rate 
            ore_extraction_rate = random.uniform(15, 1492)  # range of ore extracted in ton by time in hours
            self.ore_extraction_rate += ore_extraction_rate

            # Simulate equipment downtime 
            equipment_downtime = random.uniform(0, 3)  # break down time is 3
            self.equipment_downtime += equipment_downtime

        

        # Calculate KPIs
        self.production_efficiency = (self.total_simulation_hours - self.equipment_downtime) / self.total_simulation_hours * 100
        self.throughput = self.ore_extraction_rate / self.total_simulation_hours
        

if __name__ == "__main__":
    # Example simulation with 100 hours
    simulation = OreExtractionSimulation(total_simulation_hours=100)# require data 
    simulation.simulate()

    # Print KPI results
    print(f"Production Efficiency: {simulation.production_efficiency:.2f}%")
    print(f"Throughput: {simulation.throughput:.2f} tons per hour")
    


# # Specify how the simulation data will be logged and stored for analysis
# 

# In[ ]:


"""1. Logging Data:
    
Logging Frameworks or Libraries:
Utilize logging frameworks or libraries available in your programming language (e.g., Python's logging, Java's log4j). 
These frameworks provide standardized ways to log messages, warnings, and errors.

Define Log Levels:
Use different log levels (info, debug, warning, error) to distinguish between various types of messages. This helps filter 
and analyze logs effectively.

Timestamps:
Include timestamps in log entries to record when events occurred. This is crucial for time-series analysis and correlating 
events.

Structured Logging:
Consider using structured logging formats (e.g., JSON or CSV) to facilitate easy parsing and analysis. Each log entry can 
include relevant metadata.

2. Storage Options:
    
File-Based Storage:
Simple simulations may log data to text files (e.g., CSV, JSON). Each line or entry in the file corresponds to a logged event.

Relational Databases:
For more complex simulations, store data in relational databases (e.g., MySQL, PostgreSQL) with tables representing different
aspects of the simulation.

Time-Series Databases:
Time-series databases (e.g., InfluxDB, TimescaleDB) are suitable for simulations with time-dependent data. They efficiently
handle large datasets with timestamps.

NoSQL Databases:
NoSQL databases (e.g., MongoDB) can be chosen for their flexibility, especially when dealing with semi-structured or 
unstructured data."""


# In[6]:


#importing required libraries
import logging

# Configure logging
logging.basicConfig(filename='simulation.log', level=logging.INFO)

# Log some data
logging.info('Simulation started')
logging.warning('Warning: Resource depletion detected')
logging.error('Error: Equipment failure')


# In[9]:


#importing required libraries
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='Madhuneha', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database mydb1''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()


# # Identify and list the python libraries required for simulation script 
# 

# In[ ]:


#1. Numpy: Numerical computing, especially for handling large, multi-dimensional arrays and matrices.

#2. Pandas: Data manipulation and analysis library, providing data structures like DataFrames for efficient handling of 
           #structured data

#3. scipy: Built on top of NumPy, it provides additional functionality for scientific computing, including optimization, 
          #integration, interpolation, and more.
        
#4. matplotlib: Data visualization library for creating static, animated, and interactive plots and charts.
    
#5. simpy: Discrete-event simulation library for modeling and simulating complex systems.
    
#6. networkx: Library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
    
#7. scikit-learn:  Machine learning library that includes various tools for statistical modeling, classification, regression,
                  #clustering, and more.
        
#8. tensorflow or pytorch: Deep learning libraries for building and training neural networks.
    
#9. SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python. Useful for working with databases.
    
#10. datetime: Standard Python library for working with dates and times.
    

