# 🎯 Polymarket Python Integration - 2026 Edition

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Polymarket](https://img.shields.io/badge/Polymarket-Prediction%20Markets-purple.svg)](https://polymarket.com/)

> 🚀 **Complete Python integration for Polymarket's prediction markets** - Discover markets, analyze odds, and trade programmatically with this comprehensive 2026 quickstart guide.

## 📋 Table of Contents

- [🎯 What is Polymarket?](#-what-is-polymarket)
- [⚡ Quick Start](#-quick-start)
- [🛠️ Installation & Setup](#️-installation--setup)
- [📚 Features](#-features)
- [🔒 Safety & Risk Management](#-safety--risk-management)
- [📖 Usage Examples](#-usage-examples)
- [🔧 API Documentation](#-api-documentation)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 What is Polymarket?

Polymarket is a leading **decentralized prediction market platform** that allows users to trade on the outcome of real-world events. Unlike traditional betting platforms, Polymarket uses blockchain technology to create transparent, censorship-resistant markets where users can buy and sell shares representing their beliefs about future outcomes.

### How Prediction Markets Work

- **Market Questions**: Each market represents a question about a future event (e.g., "Will Candidate X win the election?")
- **Outcome Shares**: Markets typically have two or more outcomes (e.g., "Yes" or "No")
- **Price as Probability**: Shares trade between $0 and $1, where price represents implied probability
- **Wisdom of Crowds**: Aggregates information to produce forecasts that often outperform individual experts
- **Real Money**: Trading involves actual cryptocurrency (USDC.e on Polygon)

### What This Project Provides

This Python integration offers:
- 📊 **Market Discovery**: Browse and filter active markets
- 📈 **Real-time Analysis**: Monitor prices and order books
- 💰 **Programmatic Trading**: Place limit and market orders
- 🎯 **Position Management**: Track and manage your portfolio
- 🔒 **Safe Learning**: Mock demonstrations for risk-free practice

## ⚡ Quick Start

Get started in under 5 minutes with these simple steps:

### 1. Clone and Install
```bash
git clone https://github.com/yourusername/polymarket-python.git
cd polymarket-python
pip install -r requirements.txt
```

### 2. Set Up Environment
```bash
cp .env.example .env
# Edit .env with your Polymarket API credentials
```

### 3. Run Your First Market Query
```python
from polymarket_client import PolymarketClient

# Initialize client (read-only mode)
client = PolymarketClient()

# Get top 5 active markets
markets = client.get_markets(limit=5)
for market in markets:
    print(f"📊 {market['question']}")
    print(f"   💰 Volume: ${market['volume']}")
    print(f"   📅 Expires: {market['expires_at']}")
```

### 4. Launch the Interactive Notebook
```bash
jupyter notebook poly-integrate.ipynb
```

## 🛠️ Installation & Setup

### System Requirements

- **Python 3.8+** (recommended: 3.9+)
- **Polygon Wallet** with:
  - MATIC tokens for gas fees
  - USDC.e tokens for trading
- **Basic understanding** of Python and blockchain concepts

### Package Installation

Install the required packages using pip:

```bash
pip install requests py-clob-client python-dotenv pandas plotly web3
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file with your credentials:

```bash
# Polymarket API Credentials
POLY_API_KEY=your_api_key_here
POLY_API_SECRET=your_api_secret_here

# Wallet Configuration
# For EOA wallets (signature_type=0)
PRIVATE_KEY=your_private_key_here  # Never share or commit this!
WALLET_ADDRESS=your_wallet_address_here

# For proxy/email wallets (signature_type=1)
FUNDER_ADDRESS=your_funder_address_here
```

### Wallet Setup

#### Option 1: EOA Wallet (Recommended for Developers)
- Traditional Ethereum wallet where you control the private key
- Requires MATIC for gas fees
- Full control over your funds

#### Option 2: Proxy/Email Wallet
- Polymarket's email-based wallets
- Funder address pays for gas fees
- Easier for beginners

## 📚 Features

### 🔍 Market Discovery
- Browse all active markets
- Filter by category, volume, or search terms
- Get detailed market information including outcomes and prices
- Retrieve necessary identifiers for trading

### 📊 Real-time Price Monitoring
- Current market prices and implied probabilities
- Order book depth analysis
- Price history and trends
- Market liquidity metrics

### 💰 Programmatic Trading
- **Limit Orders**: Set specific prices for precise entry/exit
- **Market Orders**: Execute immediately at best available price
- **Order Management**: Cancel, modify, and track orders
- **Position Tracking**: Monitor your portfolio in real-time

### 📈 Data Analysis & Visualization
- Interactive charts with Plotly
- Market trend analysis
- Volume and price correlations
- Custom analytics dashboards

### 🔒 Safety Features
- Mock trading mode for learning
- Comprehensive error handling
- Transaction confirmation prompts
- Risk management tools

## 🔒 Safety & Risk Management

### ⚠️ Financial Risk Warnings

- **Real Money Involved**: All trades involve actual cryptocurrency (USDC.e)
- **No Guarantees**: Past performance is not indicative of future results
- **Start Small**: Begin with small amounts until comfortable
- **Never Invest More Than You Can Afford to Lose**

### 🔐 Security Best Practices

- **Private Key Security**: Never expose private keys or API credentials
- **Use Environment Variables**: Store sensitive data in `.env` files
- **API Rate Limits**: Respect Polymarket's API rate limits
- **Regular Backups**: Keep secure backups of your wallet data

### 🛡️ Trading Safety

```python
# Example: Safe trading with confirmation
def safe_trade_example():
    # Always use small test amounts first
    test_size = 1.0  # 1 USDC
    
    # Confirm before placing real orders
    confirm = input("Place real order? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Order cancelled for safety")
        return
    
    # Place the order with additional safety checks
    # ... trading code here
```

## 📖 Usage Examples

### Example 1: Market Discovery

```python
import requests
import pandas as pd

def get_political_markets():
    """Get active political markets with high volume"""
    params = {
        'category': 'Politics',
        'active': 'true',
        'sort': 'volume',
        'sortDirection': 'desc',
        'limit': 10
    }
    
    response = requests.get('https://gamma-api.polymarket.com/markets', params=params)
    markets = response.json()
    
    # Create readable DataFrame
    df = pd.DataFrame([{
        'Question': m['question'],
        'Volume': f"${int(float(m['volume'])):,}",
        'Expires': m['expiresAt'],
        'Yes Price': m['outcomes'][0]['price']
    } for m in markets['markets']])
    
    return df

# Usage
political_markets = get_political_markets()
print(political_markets.head())
```

### Example 2: Price Monitoring

```python
def monitor_market_price(market_id):
    """Monitor real-time price changes for a specific market"""
    client = PolymarketClient()
    
    while True:
        try:
            # Get current prices
            prices = client.get_market_prices(market_id)
            
            # Calculate price change
            if hasattr(monitor_market_price, 'last_price'):
                change = prices['Yes'] - monitor_market_price.last_price
                change_pct = (change / monitor_market_price.last_price) * 100
                print(f"Price: ${prices['Yes']:.4f} ({change_pct:+.2f}%)")
            else:
                print(f"Initial Price: ${prices['Yes']:.4f}")
            
            monitor_market_price.last_price = prices['Yes']
            time.sleep(30)  # Update every 30 seconds
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Wait longer on error
```

### Example 3: Automated Trading Strategy

```python
def simple_momentum_strategy(market_id, threshold=0.05):
    """
    Simple momentum trading strategy
    Buys when price increases by threshold, sells when it decreases
    """
    client = setup_trading_client()
    last_price = None
    position = None
    
    while True:
        try:
            current_price = client.get_price(market_id)
            
            if last_price:
                price_change = (current_price - last_price) / last_price
                
                # Buy on upward momentum
                if price_change > threshold and position != 'long':
                    print(f"🟢 Buying at ${current_price:.4f}")
                    client.place_market_order(market_id, 'buy', 10)
                    position = 'long'
                
                # Sell on downward momentum
                elif price_change < -threshold and position == 'long':
                    print(f"🔴 Selling at ${current_price:.4f}")
                    client.place_market_order(market_id, 'sell', 10)
                    position = None
            
            last_price = current_price
            time.sleep(60)  # Check every minute
            
        except Exception as e:
            print(f"Strategy error: {e}")
            time.sleep(300)  # Wait 5 minutes on error
```

## 🔧 API Documentation

### Gamma API (Public)

The Gamma API provides public access to market data without authentication:

#### Endpoints

```python
# Get all markets
GET https://gamma-api.polymarket.com/markets

# Get specific market
GET https://gamma-api.polymarket.com/markets/{market_id}

# Get market price history
GET https://gamma-api.polymarket.com/markets/{market_id}/price-history
```

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `active` | boolean | Filter active markets only |
| `category` | string | Filter by category (Politics, Crypto, Sports) |
| `limit` | integer | Maximum number of results |
| `search` | string | Search term for market questions |
| `sort` | string | Sort field (volume, liquidity, created) |
| `sortDirection` | string | Sort direction (asc, desc) |

### ClobClient (Trading)

The ClobClient provides authenticated access to trading functionality:

#### Authentication Methods

```python
# EOA Wallet (signature_type=0)
client = ClobClient(
    host="https://clob.polymarket.com",
    api_key="your_api_key",
    api_secret="your_api_secret",
    signature_type=0,
    wallet_address="your_wallet_address",
    private_key="your_private_key"
)

# Proxy Wallet (signature_type=1)
client = ClobClient(
    host="https://clob.polymarket.com",
    api_key="your_api_key",
    api_secret="your_api_secret",
    signature_type=1,
    funder_address="your_funder_address"
)
```

#### Key Methods

```python
# Market Data
client.get_markets(limit=10, category="Politics")
client.get_ticker(token_id)
client.get_order_book(token_id, depth=10)

# Trading
client.create_and_post_order(token_id, side, size, price)
client.create_market_order(token_id, side, size)
client.cancel_order(order_id)

# Account Management
client.get_balances()
client.get_positions()
client.get_order_history()
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup

```bash
# Fork the repository
git clone https://github.com/yourusername/polymarket-python.git
cd polymarket-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### Contribution Guidelines

1. **Code Style**: Follow PEP 8 and use black for formatting
2. **Testing**: Add tests for new features
3. **Documentation**: Update README and docstrings
4. **Safety**: Never commit real API keys or private keys
5. **Pull Requests**: Provide clear descriptions of changes

### Areas for Contribution

- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **New Features**: Additional trading strategies, indicators
- 📚 **Documentation**: Improve guides and examples
- 🧪 **Testing**: Add comprehensive test coverage
- 🎨 **UI/UX**: Better visualizations and dashboards

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Legal Disclaimer

- **Not Financial Advice**: This project is for educational purposes only
- **Risk Acknowledgment**: Users are responsible for their own trading decisions
- **Compliance**: Ensure compliance with local laws and regulations
- **Terms of Service**: Usage implies agreement with Polymarket's Terms of Service

## 🔗 Useful Links

- [Polymarket Official Site](https://polymarket.com/)
- [Polymarket Documentation](https://docs.polymarket.com/)
- [py-clob-client Repository](https://github.com/Polymarket/py-clob-client)
- [Polygon Network](https://polygon.technology/)
- [USDC.e Information](https://www.circle.com/usdc)

## 📞 Support

- 📧 **Email**: support@polymarket.com
- 💬 **Discord**: [Polymarket Discord](https://discord.gg/polymarket)
- 🐦 **Twitter**: [@PolymarketHQ](https://twitter.com/PolymarketHQ)
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/polymarket-python/issues)

---

<div align="center">

**⭐ Star this repository if it helped you!**

Made with ❤️ for the Polymarket community

</div>
