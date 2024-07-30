# Scrape Extension and Script

For scraping images and tweets from X (twitter), i started experimenting with js script. What this script does is scrolls to the bottom of the page, extract every tweet on the go and saves them in a json file. 
<br/>
Similarly for images, first it checks if the tweet has media or not and then only extracts which have media.
<br/>
If tweets are too much or there is infinite scrolling a maxScroll of 100 is set.

## How to Use?

- Go to `Settings` > `Extensions` in Google Chrome.
  ![image](https://github.com/user-attachments/assets/57a51f6f-ede9-4d15-867d-2f0dc53667e3)
- Turn on the developer mode from top right.
- Click Load Unpacked and select `scrape_extension` folder.

![image](https://github.com/user-attachments/assets/1ffc6eb5-9096-48dc-b87a-ef63a7360c85)

Now you can use the extension. Check out the demo video on main readme to see how to use.

Actual idea for this type of scraping was shared by someone on X (twitter).
