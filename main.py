# https://docs.askui.com/introduction/01-introduction/01-overview




from dotenv import load_dotenv
from askui import VisionAgent
import subprocess
import time

# Load environment variables
load_dotenv()


with VisionAgent() as agent:
    # Open Upwork desktop app
    # subprocess.Popen(['open', '-a', 'Upwork'])
    
    # # Wait for the application to load
    # time.sleep(5)  # Give Postman time to fully load
    
    # # Navigate to contracts section
    # agent.act("Go to the contracts section")
    # time.sleep(3)
    
    # # Find and open Python web development contract
    # agent.act("Find and open the Python web development contract")
    # time.sleep(3)
    
    # # Extract hours worked
    # hours_worked = agent.get("What is the total number of hours worked on this contract?")
    # print(f"Total hours worked: {hours_worked}")
    
    # # Optional: Get more details about the contract
    # contract_details = agent.get("What are the key details of this contract? Show client name, rate, and weekly hours if available")
    # print(f"Contract details: {contract_details}")

    # # Wait for the page to load
    # agent.wait(3)

    # # Click numbers and operators
    # agent.click("7")
    # agent.click("+ right of equals")
    # agent.click("7")
    # agent.click("=")

    # # Extract the result
    # result = agent.get("What is the calculation result?")
    # print(f"The result is: {result}")
    # agent.click("Prettier")

    # Open Downloads folder
    subprocess.Popen(['open', '/Users/rohitkumar/Downloads'])
    time.sleep(3)  # Wait for the folder to open

    # Open the PDF file
    agent.act("Find and open the file 'RAKESH MISHRA.pdf'")
    time.sleep(3)

    # Extract the name from the PDF
    name = agent.get("What is the name in the PDF?")
    print(f"Extracted name: {name}")

    # Extract the date of birth from the PDF
    dob = agent.get("What is the date of birth in the PDF?")
    print(f"Extracted date of birth: {dob}")

    # Extract the time of birth from the PDF
    time_of_birth = agent.get("What is the time of birth in the PDF?")
    print(f"Extracted time of birth: {time_of_birth}")

    # Open Notes app
    subprocess.Popen(['open', '-a', 'Notes'])
    time.sleep(3)  # Wait for the app to open

    # Paste the extracted information into Notes
    note_content = f"Name: {name}\nDate of Birth: {dob}\nTime of Birth: {time_of_birth}"
    agent.act(f"Create a new note and paste the following information: {note_content}")
    time.sleep(3)



# What is the defination of ask?