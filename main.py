from web3 import Web3
from eth_account import Account
import json
import time
from dotenv import load_dotenv
import os
from pathlib import Path
from anthropic import Anthropic
from web3.middleware import construct_sign_and_send_raw_middleware
from prompts import ZORDON_SYSTEM_PROMPT

env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

RPC_URL = os.getenv('RPC_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

w3 = Web3(Web3.HTTPProvider(RPC_URL))
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

# Add middleware for account management
from web3.middleware import construct_sign_and_send_raw_middleware

# Your account setup
account = Account.from_key(PRIVATE_KEY)
my_address = account.address

# Inject the middleware
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
w3.eth.default_account = my_address

print(f"Connected with address: {my_address}")
print(f"Current balance: {w3.eth.get_balance(my_address)} wei")

def monitor_messages():
    """Monitor incoming transactions/messages to your address"""
    last_block = w3.eth.block_number
    
    while True:
        try:
            current_block = w3.eth.block_number
            if current_block > last_block:
                # Check new blocks for transactions
                block = w3.eth.get_block(current_block, full_transactions=True)
                
                for tx in block.transactions:
                    if tx['to'] and tx['to'].lower() == my_address.lower():
                        # Check if transaction contains data (message)
                        if tx.get('input') and tx['input'] != '0x':
                            handle_message(tx)
                
                last_block = current_block
            
            time.sleep(12)  # Wait for ~1 block
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(12)

def handle_message(tx):
    """Process incoming message and generate AI response"""
    try:
        # Decode the message - improved hex handling
        input_data = tx['input']
        if isinstance(input_data, (bytes, bytearray)):
            input_data = input_data.hex()
        elif isinstance(input_data, str) and input_data.startswith('0x'):
            input_data = input_data[2:]
            
        # Clean the hex string and ensure even length
        input_data = ''.join(filter(lambda x: x in '0123456789abcdefABCDEF', input_data))
        if len(input_data) % 2 != 0:
            input_data = '0' + input_data
            
        # Add this before decoding
        if len(input_data) < 2:  # Minimum valid hex data length
            print("Message too short, skipping")
            return
            
        message = bytes.fromhex(input_data).decode('utf-8', errors='ignore')
        sender = tx['from']
        
        # Add this after decoding
        if not message.strip():  # Check if message is empty after decoding
            print("Empty message after decoding, skipping")
            return
        
        print(f"Received message: {message}")  # Debug line
        print(f"From sender: {sender}")  # Debug line
        
        # Generate AI response using Claude with correct format
        response = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            system=ZORDON_SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": f"Please respond to this blockchain message: {message}"
            }]
        )
        
        ai_response = response.content[0].text
        # Send response
        send_response(sender, ai_response)
        
    except Exception as e:
        print(f"Error handling message: {e}")
        print(f"Raw input data: {tx['input']}")  # Debug line

def send_response(to_address, message):
    """Send on-chain response"""
    try:
        print(f"\nSending message to {to_address}:")
        print(f"Message content: {message}\n")
        
        # Prepare transaction
        nonce = w3.eth.get_transaction_count(my_address)
        
        tx = {
            'from': my_address,
            'nonce': nonce,
            'to': to_address,
            'value': 0,
            'gas': 100000,
            'gasPrice': w3.eth.gas_price + (50 * 10**9),  # current gas price + 50 gwei
            'data': '0x' + message.encode('utf-8').hex()
        }
        
        # Send transaction
        tx_hash = w3.eth.send_transaction(tx)
        print(f"Response sent: {w3.to_hex(tx_hash)}")
        
    except Exception as e:
        print(f"Error sending response: {e}")
        print(f"Transaction details: {tx}")

if __name__ == "__main__":
    print(f"Monitoring messages for address: {my_address}")
    monitor_messages()
