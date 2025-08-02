🏆 Secret Auction Program — Python CLI Project
Welcome to the Secret Auction Program, a fun and simple Python script that simulates a private bidding war between multiple participants.
Run it from the terminal and determine the highest bidder without revealing others’ bids. Great for learning basic I/O, loops, and dictionaries!

🎯 Objective
Allow multiple users to submit their name and bid amount privately, then declare the highest bidder at the end.

✨ Features
🧾 Accepts multiple name + bid entries

🔄 Repeats until no new bidder

🎉 Declares the winner with the highest bid

🧼 Simulated screen clearing for fairness

🖼️ Includes ASCII logo using the art library

🚀 How to Run
Install the art module (if not already):

bash
Copy
Edit
pip install art
Run the script:

bash
Copy
Edit
python secret_auction.py
🧠 Concepts Used
Dictionaries (offers) for tracking names and bids

while loops for continuous bidding

max() function with key for selecting the highest bidder

Simulated screen clearing with print("\n" * 100)

ASCII Art integration from external module

💡 Sample Output
text
Copy
Edit
~~ Welcome To Secret Auction Program ~~
What's your name? : Alice
What's ur bid? : $150
Are there any other bidders? Type 'yes' or 'no'.
> yes

[screen clears]

What's your name? : Bob
What's ur bid? : $175
Are there any other bidders? Type 'yes' or 'no'.
> no

Congrats! for BOB you win the bid, amount of bid is $175.
✅ Possible Improvements
Replace print("\n" * 100) with os.system('cls') or 'clear' for actual screen clearing

Add input validation for non-numeric or negative bids

Encrypt or anonymize bid records

Export results to a file

Add bidding limit or time-based closing

👤 Author
Created with 💻 by GanggaSwara
Use it for fun, learning, or even classroom demonstrations on dictionaries and loops!

Let the highest bidder win! 💰
