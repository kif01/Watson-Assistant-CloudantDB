# Watson-Assistant-CloudantDB
This repo shows how we can integrate Watson Assistant with a database to add advanced functionalities. In this example we are using CloudantDB a noSQL database, where we will be doing reading and writing operations from Watson Assistant through a cloud function. 
The example built here is regarding an assistant for a virtual food/restaurants app where you can sign in to check your points and book a table.

# Technologies
- Watson Assistant
- Cloud Functions
- CloudantDB

# Scenarios
## Authentication/ Checking Balance (Points)
In this case, the databse is already prefilled with user data. The assistant asks you to enter your account number (which shoud pre-filled in the database) and then it checks if its valid and gets your current balance from the database.
You can ask:
- I want to check my balance
- I want to check my points
- How many points do I have?

## Booking
Here, the assistant asks you to fill some information for the booking. Once it's done these information will be sent and stored in the database.
You can ask:
- I want to make a booking
- I want to book a table
- Can I reserve a table?

# Architecture Flow
<img width="736" alt="Screen Shot 2021-01-21 at 11 18 00 AM" src="https://media.github.ibm.com/user/273026/files/dd603500-5bda-11eb-8ab3-4bb8a172f665">

1. We prefill our database with some sample user data (This is needed for the authentication part to check the credentials that the user will be entering). </br>
2. The user uses an interface to communicate with the virtual assistant </br>
3. The user's query are sent to the assistant </br>
4. Cloud Function will receive the query through a webhook and will process it </br>
5. Cloud Function accesses the database : If the query is regarding the authentication the cloud function performs a read operation to get the corresponding information using the user's account number. </br>
If the query is regarding a booking, then the cloud function performs a write operation to store the booking info in the database.</br>

# Implementation (Steps)
1. Sign in to your [IBM Cloud Account](https://cloud.ibm.com/login). </br>
2. Create a **Cloudant DB** service. </br>
3. Create a database inside Cloudant name it **users-db** and fill it with dummmy data like name, and balance. This db will contain users documents. Each document has its own **id** and this **id** will be used as the account number of each user (For the authentication part, to find the corresponding user). </br>
4. Create a an action in the **Cloud Function** (Choose **Python** for runtime environment). </br>
5. Copy the **cf-code.py** into this action. If the users needs authentication to fulfill his query, the action access the **users-db** to find the user. If the user wants to make a booking, the action automatically creates another database named **booking-db** that stores the booking information that the user asked for.
6. Open the parameters tab and add the **username** and **apikey** that you have from your CloudantDB service in **Service credentials**. Make sure to name the parameters **username** and **apikey** (If you named them something else, make sure to change their names in the code). 
7. Create a **Watson Assistant** service.
8. Import the dialog skill **Cloudant-Skill.json** to the assistant.
9. Get the public endpoint from the cloud function and add it in the webhook url configuration in **Watson Assistant**. Do not forget to add **.json** at the end of the url.

