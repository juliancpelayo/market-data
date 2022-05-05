import sys
import json

def main():
    market_data = {}

    if sys.stdin.readline() == 'BEGIN\n':
        for line in iter(sys.stdin.readline, b''):
            if line == 'END\n' : break

            transaction = json.loads(line)
            m_id = transaction["market"]
            if m_id in market_data:
                market_data[m_id]["total_price"] += transaction["price"]
                market_data[m_id]["transactions"] += 1
                if transaction["is_buy"] : market_data[m_id]["total_buys"] += 1
                market_data[m_id]["total_volume"] += transaction["volume"]
            else:
                market_data[m_id] = {
                    "total_price": transaction["price"],
                    "transactions": 1,
                    "total_buys": 1 if transaction["is_buy"] else 0,
                    "total_volume": transaction["volume"]
                }

        for key, data in market_data.items():
            total_volume = data["total_volume"]
            mean_price = data["total_price"] / data["transactions"]
            mean_volume = total_volume / data["transactions"]
            vwap = (mean_volume * mean_price) / mean_volume
            percentage_buy = 0 if data["total_buys"] == 0 else data["total_buys"] / data["transactions"]

            market = {
                "market": key,
                "total_volume": f'{total_volume:.2f}',
                "mean_price": f'{mean_price:.2f}',
                "mean_volume": f'{mean_volume:.3f}',
                "volume_weighted_average_price": f'{vwap:.1f}',
                "percentage_buy": f'{percentage_buy:.2f}'
            }

            output = json.dumps(market) + "\n"
            sys.stdout.write(output)


if __name__ == '__main__':
    main()
