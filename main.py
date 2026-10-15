# Seatwork 2, Club application
from pyscript import document


def candidate_checker(e):
    club_members = ['Chester Roxas', 'Joel Gonzales', 'Joseph Co', 'Ezekiel Bacay', 'Franco Maglaqui', 'Joald Calpo', 'Joshua Ortiz'] # List of Club members
    
    first_name = document.getElementById('first_name').value.strip().title() 
    last_name = document.getElementById('last_name').value.strip().title()
    
    applicant = first_name + ' ' + last_name
    member_checker = applicant in club_members

    messages = (f'Sorry {applicant}, your name is not on the list', f'Congratulations {applicant}! You are now part of the gaming club') # Returns message

    document.getElementById('result').innerHTML = messages[member_checker]