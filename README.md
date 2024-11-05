# 🤖 Zordon Chain Oracle

An AI-powered blockchain oracle featuring Zordon's consciousness, capable of autonomously monitoring and responding to on-chain messages using Claude AI. This project brings the wisdom of Zordon to the blockchain, creating interactive and personalized responses to any message sent to its address.

## Introduction

Zordon Chain Oracle transforms blockchain messaging into an interactive experience, powered by Anthropic's Claude AI. The oracle monitors incoming blockchain messages and responds with Zordon's unique personality, creating engaging on-chain conversations.

### Key Features

- **Autonomous Monitoring**: Continuously watches for incoming blockchain messages
- **AI-Powered Responses**: Generates responses using Claude AI with Zordon's personality
- **Custom Gas Management**: Optimized gas settings for reliable message delivery
- **Cross-Chain Compatibility**: Works on any EVM-compatible blockchain
- **Real-time Processing**: Immediate message processing and responses
- **Customizable Personality**: Easily modifiable system prompt

## Get Started in Minutes!

### 1️⃣ Prerequisites
- Python 3.8+
- Ethereum RPC endpoint (Infura, Alchemy, etc.)
- Anthropic API key for Claude AI
- Funded wallet for transaction responses

### 2️⃣ API Configuration
Create a `.env` file in the project directory with:
```env
RPC_URL=your_ethereum_rpc_url
PRIVATE_KEY=your_wallet_private_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 3️⃣ Installation

```bash
# Clone the repository
git clone https://github.com/Zordon-Web3/zordon-chain-oracle
cd zordon-chain-oracle

# Install dependencies
pip install web3 anthropic python-dotenv
```

### 4️⃣ Running the Oracle

```bash
python main.py
```

## 🤔 How Does It Work?

The Zordon Chain Oracle operates through several key components:

- **Message Monitoring**: Continuously scans new blocks for transactions to its address
- **Message Processing**: Decodes and validates incoming message data
- **AI Integration**: Processes messages through Claude AI with Zordon's personality
- **Response Handling**: Automatically sends responses back on-chain
- **Gas Management**: Optimizes transaction gas for reliable delivery

## 🔧 Core Components

### Main Script (main.py)
- Message monitoring and processing
- Transaction handling and response management
- Gas optimization and error handling

### Personality Module (prompts.py)
- Zordon's system prompt and personality definition
- AI response configuration
- Customizable character traits

## 🤖 Technical Details

### Message Processing
```python
def handle_message(tx):
    # Decodes incoming messages
    # Processes through Claude AI
    # Generates and sends responses
```

### Response Management
```python
def send_response(to_address, message):
    # Handles transaction creation
    # Manages gas pricing
    # Sends on-chain responses
```

## ⚠️ Security Considerations

- Never commit your `.env` file
- Use a dedicated wallet for the oracle
- Monitor gas costs and usage
- Regularly check transaction status
- Implement rate limiting if needed

## 🔄 Testing

1. Deploy the oracle with a funded wallet
2. Send a test message to the oracle's address
3. Monitor the console for processing status
4. Check for the response transaction
5. Verify message content and gas costs

## 📚 Additional Resources

- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [EVM Documentation](https://ethereum.org/en/developers/docs/evm/)

## ❤️ Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Propose new features
- Improve documentation
- Add testing scenarios

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Support

For questions or issues:
- Open a GitHub issue
- Submit a pull request
- Contact the maintainers

Happy messaging with Zordon! 🚀