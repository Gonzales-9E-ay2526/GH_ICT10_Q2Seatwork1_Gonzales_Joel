# Seatwork 2, Club application
from pyscript import document


def candidate_checker(e):
    club_members = ['Chester Roxas', 'Joel Gonzales', 'Joseph Co', 'Ezekiel Bacay', 'Franco Maglaqui', 'Joald Calpo', 'Joshua Ortiz'] # List of Club members
    
    first_name = document.getElementById('first_name').value.strip().title() # Get input values, trims whitespace, and capitalize each word
    last_name = document.getElementById('last_name').value.strip().title()  # Get input values, trims whitespace, and capitalize each word
    
    applicant = first_name + ' ' + last_name # Combines first and last name into a single full name 
    member_checker = applicant in club_members # Returns True or False

    messages = (f'Sorry {applicant}, your name is not on the list', f'Congratulations {applicant}! You are now part of the gaming club') # True or false for member and non member

    document.getElementById('result').innerHTML = messages[member_checker] # displays message
