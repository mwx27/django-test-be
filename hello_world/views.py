from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from web3 import Web3
from . import rpc

web3 = Web3(Web3.HTTPProvider(rpc.POLYGON_RPC_URL))
if web3.is_connected():
    print("Successfully connected to the blockchain.")
else:
    print("Failed to connect.")

def get_current_block(request):
    current_block_number = web3.eth.block_number
    return HttpResponse(current_block_number)


def say_hello(request):
    return HttpResponse('Hello world!')