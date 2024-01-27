import scratchattach as scratch3
from scratchattach import Encoding

session = scratch3.Session(".eJxVT89PgzAU_l96nkhpu8Jum5cZzRKXmLgTebQPqEC70OKMxv_dNuGy28v3vp-_ZPE4W5iQ7IgZ3ReCNROMXlCyITUsoa8TozY6EmghWFlRyeIvoA_KucEk5c3NA-p7RQNqQJtkCUMbjIJgnM3Wh8_OeB1X8LCSo6-LR8oCharJKWcgOLIGKFKmqGK8UcBzvTsX38_NMB7fTwfeHqfX5ml_-Vjw5a300WZ0nbEP5hqdym1WyoxWNCt4qjiC7RboUu-YtCH6MwKuDmbCH2cTvJ9wjsUeT3irL3Ha_bAefB9JrW6hElIWrJVAuVZVgaqQuZZYMVriVghJJZTk7x9ja3Pc:1rT2ty:FicJaCJBl1llywxXuJfkVpe7L-k", username="iloveanimals51") #replace with your session_id and username
conn = session.connect_cloud("956295976") #replace with your project id

client = scratch3.CloudRequests(conn)

@client.request
def follow(usert): #called when client receives request
    print(usert)
    who="hcr5"
    reciever=usert
    amount=-10
    
    conn = session.connect_cloud("669020072")
    encwho=Encoding.encode(f"bal&{who}")
    encto=Encoding.encode(f"give&{reciever}&{amount}")

    user = session.connect_user(usert)
    user.follow()

    print(conn)
    
    conn.set_var("Cloud", encwho)
    conn.set_var("Cloud", encwho)
    conn.set_var("verification", "0")
    conn.set_var("Cloud", encto)
    conn.set_var("Cloud", encwho)

    return "recieved"

@client.request
def check():
    return "server running"
    
@client.event
def on_ready():
    print("Request handler is running")

client.run() #make sure this is ALWAYS at the bottom of your Python file
