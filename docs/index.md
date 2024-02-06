# Untrade SDK

## Installation
Execute the git clone command:
```
git clone https://github.com/ztuntrade/untrade-sdk.git && cd untrade-sdk
```

Install the package using pip3:
```
pip3 install .
```


## Initialization
To start using the Untrade API, first initialize the client:

```python
from untrade.client import Client
client = Client()
```

## Module Functions

### Create New Order

To create a new order, use the following function:

```python
client.create_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    market="COIN-M",
    quantity=100,
    leverage=10,
    target=45000,
    stop_loss=35000
)
```

#### Parameters

- `symbol` (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
- `side` (string): 'BUY' or 'SELL'.
- `type` (string): 'LIMIT' or 'MARKET'.
- `market` (string): 'SPOT', 'COIN-M', or 'USD-M'.
- `quantity` (float, optional): Trade quantity.
- `leverage` (int, optional): Leverage for the trade (for non-SPOT markets).
- `target` (float, optional): Target price.
- `stop_loss` (float, optional): Stop loss price.
- `price` (float, optional): Entry price (for LIMIT orders).
- `position` (float, optional): Position size.

**Important Note:** Specify either `position` or `quantity`. Providing both or neither triggers an error.

### Close Order

Closes an existing trading order.

```python
client.close_order(
    symbol="BTCUSDT",
    side="SELL",
    type="MARKET",
    market="COIN-M",
    quantity=100,
    parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8"
)
```
#### Parameters
- `symbol` (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
- `side` (string): 'BUY' or 'SELL'.
- `type` (string): 'LIMIT' or 'MARKET'.
- `market` (string): 'SPOT', 'COIN-M', or 'USD-M'.
- `quantity` (float, optional): Trade quantity.
- `price` (float, optional): Entry price (for LIMIT orders).
- `parent_order_id` (string): The ID of the parent order being closed.

### Target Order

```python
client.create_target_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    market="COIN-M",
    quantity=100,
    parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8"
)
```
#### Parameters
- `symbol` (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
- `side` (string): 'BUY' or 'SELL'.
- `type` (string): 'LIMIT' or 'MARKET'.
- `market` (string): 'SPOT', 'COIN-M', or 'USD-M'.
- `quantity` (float, optional): Trade quantity.
- `price` (float, optional): Entry price (for LIMIT orders).
- `parent_order_id` (string): The ID of the parent order being closed.


### Stop-Loss Order

```python
client.create_stoploss_order(
    symbol="BTCUSDT",
    side="SELL",
    type="MARKET",
    market="COIN-M",
    quantity=100,
    parent_order_id="68b195ec-150e-47e1-8e01-694b719acdd8"
)
```

#### Parameters
- `symbol` (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
- `side` (string): 'BUY' or 'SELL'.
- `type` (string): 'LIMIT' or 'MARKET'.
- `market` (string): 'SPOT', 'COIN-M', or 'USD-M'.
- `quantity` (float, optional): Trade quantity.
- `price` (float, optional): Entry price (for LIMIT orders).
- `parent_order_id` (string): The ID of the parent order being closed.


# Backtest

Use the following method to initiate a backtest:

```python
client.backtest(file_path="/your/path")
```

## File Requirements

**Format:** CSV (Comma-Separated Values)

**Content Structure:** The CSV file must include the following headers in the exact order:

- Index (int)
- datetime (datetime) : Format YYYY-MM-DD HH:MM:SS
- open (float)
- high (float)
- low (float)
- close (float)
- volume (float)
- signals (int)

Each row in the file should represent a different time point in the dataset.

## Important Note

- If you are willing to open a long trade and cut it: then your entry is `1` and exit is `-1`.
- If you are willing to open a short trade and cut it: then your entry is `-1` and exit is `1`.
- When there is no signal - mark the timestamps with `0`. 
- In between entry (`1` or `-1`) and exit (`1` or `-1`) of a trade, mark the timestamps with `0`. 


### Example CSV

```
Index,datetime,open,high,low,close,volume,signals
0,2022-02-01 05:30:00,38466.9,38627.35,38276.43,38342.36,1058.42599,0
```

## Error Codes

- `4001`: Position not needed if quantity provided
- `4002`: Leverage mandatory for Futures (USD-M, COIN-M)
- `4003`: Leverage not for SPOT orders
- `4004`: Specify Quantity or Position
- `4005`: Price needed for LIMIT orders
- `4006`: Target price > Entry price
- `4007`: Stop-Loss price > Entry price
- `4008`: Only .csv files accepted


