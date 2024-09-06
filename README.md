# django-test-be
Simple project to familiarize with django

You can fetch block number and balance this way:
http://localhost:8080/hello_world/balance?address=<evm_wallet_address_here>
http://localhost:8080/hello_world/block_number/

To run app: python manage.py runserver 8080

Don't forget to create .env file with alchemy api key