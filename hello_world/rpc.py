from dotenv import load_dotenv
import os

load_dotenv()
alchemy_key = os.getenv("ALCHEMY_KEY")

POLYGON_RPC_URL = 'https://polygon-mainnet.g.alchemy.com/v2/' + alchemy_key
