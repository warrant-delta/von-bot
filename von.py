import discord
from discord.ext import commands
import praw
import random

# Debugging to ensure script is running
print("Bot script is starting...")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

# Reddit API Setup
reddit = praw.Reddit(
    client_id='aSa_wuVLcwmAMZwAbqk52A',
    client_secret='fTisnPowf64rOItpfYFwdAg_knExNA',
    user_agent='discord:kingvon.bot:v1.0 (by u/Ambitious-Range117)'
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')  # This confirms the bot is logged in
    print("Bot is ready!")  # More confirmation that it started

# Command
@bot.command()
async def oblock2011(ctx):
    subreddits = ["KingVon", "Chiraqology", "rap", "hiphopheads", "chicago"]
    selected_subreddit = random.choice(subreddits)
    subreddit = reddit.subreddit(selected_subreddit)

    # Randomly choose listing type
    listing = random.choice(['hot', 'new', 'top'])
    if listing == 'hot':
        posts = subreddit.hot(limit=100)
    elif listing == 'new':
        posts = subreddit.new(limit=100)
    else:
        posts = subreddit.top(limit=100)

    # Filter to image URLs
    image_posts = [post for post in posts if not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(image_posts)

    if image_posts:
        await ctx.send(image_posts[0].url)
    else:
        await ctx.send("No images found right now.")


# Add your bot token below (ensure this token is valid and not exposed publicly)
bot.run('MTM3MDgwMjgzNjYzMTMyMjYzNA.GjxC5A.UOH_RbfeT6pSrHCTW0ol8QD51zGvGcCtvidhsA')
