import datetime
import os
from reports import generate_report
from emails import generate_email, send_email

#This script is step 4 on the final.
#Generate a PDF report and send it through email


def read_files(dir):
    """This method is also present in main.py"""
    all_image_data = []

    for filename in os.listdir(dir):
        if not filename.endswith(".txt"):
            continue

        source_path = os.path.join(dir, filename)
        with open(source_path, 'r') as opened:
            lines = opened.read().splitlines()
            opened.close()

            image_data = ImageData()
            image_data.name = lines[0]
            image_data.weight = lines[1]
            #print(image_data)
            all_image_data.append(image_data)
    
    return_string = ""
    for d in all_image_data:
        return_string += "name: {}<br/>weight: {}<br/><br/>".format(d.name, d.weight)
    return return_string

class ImageData:
    """This class is also present in main.py"""
    name = None
    weight = None

    def __str__(self):
        results = "name:{}\n".format(self.name)
        results += "weight:{}\n".format(self.weight)
        return results



if __name__ == "__main__":
    
    #read the data from the description text files
    target_dir = r"C:\Repos\CourseraPyGoogleFinal\supplier-data\descriptions"
    paragraph = read_files(target_dir)
    
    attachment = r"C:\Repos\CourseraPyGoogleFinal\tmp\processed.pdf"
    title = "Processed Update on {}".format(datetime.datetime.now().strftime("%m/%d/%Y"))
    #generate the attachment
    generate_report(attachment, title, paragraph)

    #create the email
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully.  A detailed list is attached to this email."
    to = "username@example.com" #replace this with your actual username.
    email_tosend = generate_email("automation@example.com", to, subject, body, attachment)

    #send the email
    send_email(email_tosend, "username", "password")

