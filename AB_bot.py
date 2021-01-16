#imports
import praw
import config
import time
import os

# log in definition
def bot_login():
    reddit = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = 'MBC Facts Bot v0.1')
    return reddit
#how to run the bot
def run_bot(reddit, comments_replied_to):
    print('obtaining 25 comments....')

    for comment in reddit.subreddit('test').comments(limit = 25):
        if '!MBC' in comment.body and comment.id not in comments_replied_to and not comment.author == reddit.user.me():
            print('comment found ' + comment.id)
            comment.reply('''Credit for list to uForYeWhoArtLiterate bot by unakadie

- Live-streamed Tomlin's locker room speech
- Drove 100 down McKnight Road in Pittsburgh, which has a 45 MPH speed limit
- Trashed a condo and threw furniture out a window, almost hit some people, notably a child
- Killed a home aquarium full of piranhas and refused to pay the man who installed the tank
- Refused to play week 17 for the Steelers
- Dyed his mustache blonde
- Refused to pay a chef because he thought he threatened him by placing a fish head in the freezer (the fish head was saved to make a soup)
- Farted on a doctor
- Demanded a trade from the Steelers
- Became "Mr. Big Chest"
- Threw a fit over Juju winning team MVP and trashed him on social media
- Nixed the Bills trade
- Showed up to Raiders training camp in a hot air balloon
- Held out and refused to show up to training camp because the NFL would not approve his helmet because it was too old for their safety standards
- Froze his feet
- Tried to paint over his old helmet, hoping no one would notice I guess
- Acquired a newer version of the same model of helmet, which the NFL refused to let him use
- Picked out a new helmet and finally showed up to the Raiders
- Got fined by the Raiders for not attending camp
- Tweeted the fines
- Tried to fight Mike Mayock, called him a cracker, had to be held back by Vontaze Burfict, then punted a football down the practice field and said "fine me for that"
- Got fined for that
- Released a video were he used audio of Jon Gruden, who didn't know he was being recorded, which is illegal in California (full disclosure, Gruden has said he gave permission, but the generally accepted theory is that he said that in the hope that it would help get him to show up to the facility and not alienate him)
- Demanded a release from the Raiders
- Was released
- "GRANDMA I’M FREEEEEE! FLY LIKE A FREEEEE!"
- Made a lot of crazy tweets saying stuff like 'Devil is a lie', a proverb about burning down a village... he made a lot of crazy tweets is the point
- Liked a tweet about Mayock getting raped in the ass
- Signed with the Patriots
- The sexual assault allegations came out (the one were he's getting sued)
- The sexual harassment allegations came out (the one were he's not getting sued)
- Threatened the woman not suing him in a group text that included his lawyer and had a picture of her kids in the text
- Got released by the Patriots
- Went off on a tweet storm and said a lot of crazy shit about a lot of people, and was supportive of people sending threats to the writer of the article detailing the sexual harassment allegations
- Said he was done with the NFL
- Went back to college via online classes
- Tried to outsource his homework to Twitter
- Wants to come back to the NFL
- Filed several grievances to try and get more than $40 million from the Raider's and Patriots
- Was ordered to show up for a deposition regarding trashing the condo
- Was accused of "reprehensible behavior" during the deposition [(which is it's own insane thread, btw)](https://old.reddit.com/r/nfl/comments/dcw3mj/yahoo_lawyer_accuses_antonio_brown_of/), which included, but was not limited too:
    1. "Arrived nearly 30 minutes late to the deposition."
    2. “[C]hanted, over and over, as if a mantra, a narrative of his own warped concept of the proceeding”.
    3. “Acting as if he was above the rule of law, [Brown] proceeded to make a mockery of the deposition process. [Brown’s] antics were so unreasonable that barely twenty [20] minutes into the deposition, his counsel asked for a break [so] he could speak with [Brown] about his demeanor.
    4. “After approximately 20-30 minutes, [Brown] required another break. When the deposition resumed [Brown] increased his level of obstructive behavior. At one point, [Brown] refused to answer any questions, instead saying “next question” no less than 10 times.”
    5. “Soon thereafter, [Brown] started announcing a countdown, starting at ‘five (5) minutes,’ and counting down the minutes thereafter. Before noon [Brown] left the conference room.”

- Said that the Patriots have to pay him anyway, so they might as well let him play
- Tweeted a couple of bizarre tweets about the Raiders using him for HBO ratings and the Patriots trying to steal his stuff and kept using this weird chicken based metaphor
- Tried out for the Saints and brought an entourage and film crew to shoot a music video with him when specifically told not to do that
- Called out Robert Kraft for his rub and tug massage session in Florida
- Starting training for a boxing match with Logan Paul (I'm as shocked as you are)
- "No more white woman 2020"
- The attorney representing him in the suit involving the condo quit
- Used a bunch of slurs and profane language towards cops in an Instagram video he posted
- A police youth football league cut ties with him and returned a donation after the release of the video saying there was a "irreparable rift" between the department and AB
- Waved a bag of gummy candy dicks at the cops in a video he posted
- Got dropped by his agent
- Was involved in a disputed with movers at his home where he allegedly threw rocks at the movers and moving vans. He is currently being investigated for battery by the police.
- His trainer was arrested and he is still a suspect in the battery case.
- Warrant issued for the arrest of AB.''')
            print('replied to comment ' + comment.id)

            comments_replied_to.append(comment.id)

        with open ('comments_replied_to.txt', 'a') as f:
            f.write(comment.id + '\n')

    print('sleeping for 10 seconds')
    #sleep for 10 seconds
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to


reddit = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(reddit,comments_replied_to)
