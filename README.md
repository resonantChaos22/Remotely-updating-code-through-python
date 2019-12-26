# Remotely-updating-code-through-python
I used python to create a code-updater that can update any code and run it using web scraping.

This works like this.....


Every time the file runs, it logs into a website(Check.php) and checks whether it requires an update or not based on a number.
It checks whether the number on device and website is same or not.
If not, it goes to a website with the new code and scrapes the data using bs4.
Then it creates a new file with the new data and starts running that file while updating the number on the device.
The last to last file is deleted and it goes on.
