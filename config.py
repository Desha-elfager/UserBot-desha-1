import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID" "12339829"))
API_HASH = os.getenv("API_HASH" "685177285c55dd5f9a1f9bba0e443bce")
SESSION = os.getenv("SESSION" "BACLdIxRzzMypw1rX8vcGlNNjOWVS4KNB3vTGv2OHjffuh5S-80DuEqJobNa2eDTggbTAYoXyUrqaBLw9YbYw8sryOxGGkY6aDyh0f__eA5rlrMLDjywz6F4tVCKwoe4gCGchMwwPY_Xmx5c_QkxIdfi38mxGMDV3QP-6FDfQDt2v1RO0zy7g6101g5hSkaAYgqP2tZm9sGaFDaX4eqNJjlBwUr3lp4aO4PmwE-cLINWVIDuzpE60GVdqRZEjZg1KFKvkXYtt221PWlmvEUtzhiVf6Ok_P0fgiT9ig9hMyLZ3r4Cy91-hjnw6DrwxPifoPWyJ-NuClEi5WtGepTBVjtUewl7hwA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VcUserBot"))
call_py = PyTgCalls(bot)
