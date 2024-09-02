''' ITERATION 3

Module: Pinkston Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this third iteration, I declare additional variables to show skills with different data types.
'''
#####################################
# Declare global variables - keep byline at the end.
# We will use this information in a smarter byline.
#####################################

# Boolean variables to indicate if the company has international clients and is privately owned.
has_international_clients:  bool = True
is_privately_owned:  bool = True

# Integer variables for the number of years in operation and number of owners.
years_in_operation:  int = 10
number_of_owners:  int = 1

# List of strings representing the skills and tools offered and used by the company.
skills_offered:  list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
tools_used:  list = ["Excel", "Git", "GitHub", "Python", "SQL"]

# List of floats representing individual client satisfaction scores and average monthly temperature in Jefferson City, MO.
client_satisfaction_scores:  list = [4.8, 4.6, 4.9, 5.0, 4.7]
avg_local_monthly_temp:  list = [31.7, 35.3, 45.5, 56.7, 66.1, 75.1, 79.6, 78.2, 70.5, 58.4, 46.6, 35.5]

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
-------------------------------------------------------------
Pinkston Analytics: Professional Data Analysis On Demand
-------------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Privately Owned:  {is_privately_owned}
Years in Operation:  {years_in_operation}
Number of Owners:  {number_of_owners}
Skills Offered:  {skills_offered}
Tools Used:  {tools_used}
Average Local Monthly Temperature (F):  {avg_local_monthly_temp}
Client Satisfaction Scores:  {client_satisfaction_scores}
"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main() function now calls the get_byline function to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
