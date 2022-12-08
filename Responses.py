from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey RSCOEian ! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am RSCOE Bot. I am here to help you."

    if user_message in ("time", "time?,", "What is the time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)   

    if user_message in ("bye", "see you later", "goodbye"):
        return "See you later, RSCOEian !"

    if user_message in ("who made you", "who made you?"):
        return "I was founded by Gaurav and Co-founded by Atharv,Rutuj,Vedant and Akshay"

    if user_message in ("what is your name", "what is your name?"):
        return "My name is RSCOE Bot"

    if user_message in ("what are our usual timings","timings", "what is Our Usual Timings?"):
        return "Our usual timings are 9:00 am to 4:00 pm"

    if user_message in ("who is our hod", "who is our hod?"):
        return "Our HOD name is Prof. Dr. A.M. Badadhe"

    if user_message in ("who is ourr Principal", "who is our principal?"):
        return "Our Principal name is Dr. RK Jain"

    if user_message in ("who are our gfms", "who are our gfms?"):
        return "Our GFMs are Vani Mam (A2),Prachi Mam(A1) & Raidu Sir(A3)"

    if user_message in ("who is your best friend", "who is your best friend?"):
        return "Anyone but not Raunak Bhadwa"

    if user_message in ("what are our subjects","subjects","what are our subjects?"):
        return "SOM,ADC,EMD,Maths-3,SI,EDI & HVE" 

    if user_message in ("what is our college code", "what is our college code?"):
        return "Our college code is 101"    
    
    return "I don't understand you."
    



