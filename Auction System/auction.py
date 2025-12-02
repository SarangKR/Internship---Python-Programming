from users import load_data, save_data

def create_auction_item(seller, item_name, starting_bid):
    data = load_data()
    auction_item = {
        "seller": seller,
        "item_name": item_name,
        "highest_bid": starting_bid,
        "highest_bidder": None
    }
    data['auctions'].append(auction_item)
    save_data(data)
    return "Auction item created."

def place_bid(bidder, item_name, bid_amount):
    data = load_data()
    for auction in data['auctions']:
        if auction['item_name'] == item_name:
            if bid_amount > auction['highest_bid']:
                auction['highest_bid'] = bid_amount
                auction['highest_bidder'] = bidder
                save_data(data)
                return "Bid placed successfully."
            else:
                return "Bid must be higher than the current highest bid."
    return "Auction item not found."

