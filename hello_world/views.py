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
    return JsonResponse({"blockNumber": current_block_number})

def get_balance(request):
    address = request.GET.get('address')

    if not Web3.is_address(address):
        return JsonResponse({'error': 'Invalid address'}, status=400)

    checksum_address = Web3.to_checksum_address(address)
    balance_wei = web3.eth.get_balance(checksum_address)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return JsonResponse({"balance": balance_eth}, status=200)


def say_hello(request):
    return HttpResponse('Hello world!')
