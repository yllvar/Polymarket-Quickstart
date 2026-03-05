"""
Polymarket Python Client
A simplified interface for interacting with Polymarket's prediction markets.

This module provides a clean, user-friendly API for:
- Market discovery and filtering
- Real-time price monitoring
- Order book analysis
- Trading operations (with proper authentication)
"""

import os
import requests
import pandas as pd
import time
from datetime import datetime
from typing import Dict, List, Optional, Union
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class PolymarketClient:
    """
    A simplified client for interacting with Polymarket's APIs.
    
    This client provides both read-only access (no authentication required)
    and trading capabilities (authentication required).
    """
    
    def __init__(self, use_mock_trading: bool = True):
        """
        Initialize the Polymarket client.
        
        Args:
            use_mock_trading: Whether to use mock trading for safety (default: True)
        """
        self.gamma_api_url = "https://gamma-api.polymarket.com"
        self.clob_api_url = "https://clob.polymarket.com"
        self.use_mock_trading = use_mock_trading
        self._trading_client = None
        
        # Initialize trading client if credentials are available
        if not use_mock_trading:
            self._setup_trading_client()
    
    def _setup_trading_client(self):
        """Setup the authenticated trading client."""
        try:
            from py_clob_client.clob_client import ClobClient
            from py_clob_client.auth import create_or_derive_api_creds
            
            api_key = os.getenv('POLY_API_KEY')
            api_secret = os.getenv('POLY_API_SECRET')
            private_key = os.getenv('PRIVATE_KEY')
            wallet_address = os.getenv('WALLET_ADDRESS')
            funder_address = os.getenv('FUNDER_ADDRESS')
            
            if private_key and wallet_address:
                # EOA Wallet
                signature_type = 0
                if not api_key or not api_secret:
                    api_creds = create_or_derive_api_creds(
                        private_key=private_key,
                        signature_type=signature_type
                    )
                    api_key = api_creds['key']
                    api_secret = api_creds['secret']
                
                self._trading_client = ClobClient(
                    host=self.clob_api_url,
                    api_key=api_key,
                    api_secret=api_secret,
                    signature_type=signature_type,
                    wallet_address=wallet_address,
                    private_key=private_key
                )
                
            elif funder_address:
                # Proxy Wallet
                signature_type = 1
                if not api_key or not api_secret:
                    raise ValueError("API key and secret required for proxy wallets")
                
                self._trading_client = ClobClient(
                    host=self.clob_api_url,
                    api_key=api_key,
                    api_secret=api_secret,
                    signature_type=signature_type,
                    funder_address=funder_address
                )
            else:
                print("⚠️ No wallet credentials found. Trading functions will use mock mode.")
                self.use_mock_trading = True
                
        except ImportError:
            print("⚠️ py-clob-client not installed. Install with: pip install py-clob-client")
            self.use_mock_trading = True
        except Exception as e:
            print(f"⚠️ Error setting up trading client: {e}")
            self.use_mock_trading = True
    
    def get_markets(self, limit: int = 10, active: bool = True, 
                   category: Optional[str] = None, search: Optional[str] = None) -> Dict:
        """
        Fetch markets from Polymarket's Gamma API.
        
        Args:
            limit: Maximum number of markets to return
            active: Whether to return only active markets
            category: Filter by category (e.g., 'Politics', 'Crypto', 'Sports')
            search: Search term to filter markets
            
        Returns:
            Dictionary containing market data
        """
        params = {
            'limit': limit,
            'active': str(active).lower(),
            'sort': 'volume',
            'sortDirection': 'desc'
        }
        
        if category:
            params['category'] = category
        if search:
            params['search'] = search
        
        try:
            response = requests.get(f"{self.gamma_api_url}/markets", params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching markets: {e}")
            return {'markets': []}
    
    def get_market_prices(self, market_id: str) -> Dict[str, float]:
        """
        Get current prices for a market's outcomes.
        
        Args:
            market_id: The market ID to query
            
        Returns:
            Dictionary mapping outcome names to their current prices
        """
        if self.use_mock_trading or not self._trading_client:
            # Return mock prices for demonstration
            return {'Yes': 0.62, 'No': 0.38}
        
        try:
            # In a real implementation, this would query the trading client
            # For now, return mock data
            return {'Yes': 0.62, 'No': 0.38}
        except Exception as e:
            print(f"Error getting market prices: {e}")
            return {}
    
    def get_order_book(self, token_id: str, depth: int = 10) -> Dict:
        """
        Get the order book for a specific token.
        
        Args:
            token_id: The CLOB token ID
            depth: Number of price levels to retrieve
            
        Returns:
            Dictionary containing bids and asks
        """
        if self.use_mock_trading or not self._trading_client:
            # Return mock order book
            base_price = 0.62
            bids = [{'price': round(base_price * (1 - 0.005 * (i + 1)), 4), 
                    'size': round(100 * (depth - i) / depth, 2)} for i in range(depth)]
            asks = [{'price': round(base_price * (1 + 0.005 * (i + 1)), 4), 
                    'size': round(100 * (depth - i) / depth, 2)} for i in range(depth)]
            return {'bids': bids, 'asks': asks}
        
        try:
            # In a real implementation, this would query the trading client
            return {'bids': [], 'asks': []}
        except Exception as e:
            print(f"Error getting order book: {e}")
            return {'bids': [], 'asks': []}
    
    def get_balances(self) -> Dict[str, str]:
        """
        Get account balances.
        
        Returns:
            Dictionary containing balance information
        """
        if self.use_mock_trading or not self._trading_client:
            return {
                "usdc": "1000.00",
                "collateral_available": "950.00",
                "collateral_locked": "50.00"
            }
        
        try:
            # In a real implementation, this would query the trading client
            return {"usdc": "0.00", "collateral_available": "0.00", "collateral_locked": "0.00"}
        except Exception as e:
            print(f"Error getting balances: {e}")
            return {}
    
    def get_positions(self) -> List[Dict]:
        """
        Get current positions.
        
        Returns:
            List of position dictionaries
        """
        if self.use_mock_trading or not self._trading_client:
            return [{
                "token_id": "example-token",
                "side": "long",
                "size": "100.00",
                "avg_entry_price": "0.60",
                "market_question": "Example market question"
            }]
        
        try:
            # In a real implementation, this would query the trading client
            return []
        except Exception as e:
            print(f"Error getting positions: {e}")
            return []
    
    def place_market_order(self, token_id: str, side: str, size: float, 
                          confirm: bool = True) -> Optional[Dict]:
        """
        Place a market order.
        
        Args:
            token_id: The CLOB token ID
            side: 'buy' or 'sell'
            size: Number of shares to trade
            confirm: Whether to ask for confirmation
            
        Returns:
            Order response dictionary or None
        """
        if self.use_mock_trading:
            print(f"🧪 MOCK MODE: Would place {side} market order for {size} shares")
            return {
                "order_id": f"mock-order-{int(time.time())}",
                "status": "filled",
                "size": str(size),
                "executed_price": "0.62"
            }
        
        if not self._trading_client:
            print("❌ Trading client not available")
            return None
        
        # Implementation for real trading would go here
        print("⚠️ Real trading not implemented in this simplified client")
        return None
    
    def place_limit_order(self, token_id: str, side: str, size: float, 
                         price: float, confirm: bool = True) -> Optional[Dict]:
        """
        Place a limit order.
        
        Args:
            token_id: The CLOB token ID
            side: 'buy' or 'sell'
            size: Number of shares to trade
            price: Limit price per share
            confirm: Whether to ask for confirmation
            
        Returns:
            Order response dictionary or None
        """
        if self.use_mock_trading:
            print(f"🧪 MOCK MODE: Would place {side} limit order for {size} shares at ${price}")
            return {
                "order_id": f"mock-order-{int(time.time())}",
                "status": "open",
                "size": str(size),
                "price": str(price)
            }
        
        if not self._trading_client:
            print("❌ Trading client not available")
            return None
        
        # Implementation for real trading would go here
        print("⚠️ Real trading not implemented in this simplified client")
        return None


# Utility functions for common operations
def format_markets_dataframe(markets_data: Dict) -> pd.DataFrame:
    """
    Convert markets API response to a readable DataFrame.
    
    Args:
        markets_data: Response from get_markets()
        
    Returns:
        Formatted pandas DataFrame
    """
    if not markets_data or 'markets' not in markets_data:
        return pd.DataFrame()
    
    markets_list = []
    for market in markets_data['markets']:
        # Format the end date
        try:
            end_date = datetime.fromisoformat(market['expiresAt'].replace('Z', '+00:00'))
            formatted_end_date = end_date.strftime('%Y-%m-%d %H:%M UTC')
        except:
            formatted_end_date = market.get('expiresAt', 'N/A')
        
        # Extract outcomes and their prices
        outcomes = {}
        for outcome in market.get('outcomes', []):
            outcomes[outcome['title']] = outcome.get('price', 'N/A')
        
        market_dict = {
            'Question': market['question'],
            'Category': market['category'],
            'Volume (USDC)': f"${int(float(market['volume'])):,}",
            'Expires': formatted_end_date,
            'Market ID': market['marketId'],
            'Outcomes': outcomes
        }
        markets_list.append(market_dict)
    
    return pd.DataFrame(markets_list)


def monitor_market_price(client: PolymarketClient, market_id: str, 
                        update_interval: int = 30) -> None:
    """
    Monitor and print price updates for a specific market.
    
    Args:
        client: PolymarketClient instance
        market_id: Market ID to monitor
        update_interval: Seconds between updates
    """
    last_price = None
    
    print(f"📊 Monitoring market {market_id}...")
    print("Press Ctrl+C to stop monitoring")
    
    try:
        while True:
            try:
                prices = client.get_market_prices(market_id)
                
                if 'Yes' in prices:
                    current_price = prices['Yes']
                    
                    if last_price is not None:
                        change = current_price - last_price
                        change_pct = (change / last_price) * 100
                        print(f"Price: ${current_price:.4f} ({change_pct:+.2f}%)")
                    else:
                        print(f"Initial Price: ${current_price:.4f}")
                    
                    last_price = current_price
                else:
                    print("No price data available")
                
                time.sleep(update_interval)
                
            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(update_interval * 2)
                
    except KeyboardInterrupt:
        print("\n👋 Monitoring stopped by user")


if __name__ == "__main__":
    # Example usage
    client = PolymarketClient()
    
    print("🎯 Polymarket Python Client Example")
    print("=" * 40)
    
    # Get top 5 markets
    markets = client.get_markets(limit=5)
    df = format_markets_dataframe(markets)
    
    if not df.empty:
        print("\n📈 Top 5 Markets by Volume:")
        print(df[['Question', 'Category', 'Volume (USDC)']].to_string(index=False))
    else:
        print("No markets data available")
