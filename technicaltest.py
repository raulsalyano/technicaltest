import requests

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_answered_unanswered(data):
    answered = 0
    unanswered = 0
    for item in data['items']:
        if 'is_answered' in item:
            if item['is_answered']:
                answered += 1
            else:
                unanswered += 1
    return answered, unanswered

def get_least_viewed_answer(data):
    least_views = float('inf')
    least_viewed_answer = None
    for item in data['items']:
        if 'view_count' in item:
            if item['view_count'] < least_views:
                least_views = item['view_count']
                least_viewed_answer = item
    return least_viewed_answer

def get_oldest_and_newest_answer(data):
    oldest_answer = min(data['items'], key=lambda x: x['creation_date'])
    newest_answer = max(data['items'], key=lambda x: x['creation_date'])
    return oldest_answer, newest_answer

def get_highest_reputation_owner_response(data):
    highest_reputation_owner = max(data['items'], key=lambda x: x['owner']['reputation'])
    return highest_reputation_owner

def print_results(answered, unanswered, least_viewed_answer, oldest_answer, newest_answer, highest_reputation_owner):
    print("Number of answered responses:", answered)
    print("Number of unanswered responses:", unanswered)
    print("Answer with the fewest number of views:")
    print("   Title:", least_viewed_answer['title'])
    print("   Views:", least_viewed_answer['view_count'])
    print("Oldest answer:")
    print("   Title:", oldest_answer['title'])
    print("   Creation Date:", oldest_answer['creation_date'])
    print("Newest answer:")
    print("   Title:", newest_answer['title'])
    print("   Creation Date:", newest_answer['creation_date'])
    print("Response from the owner with the highest reputation:")
    print("   Owner Name:", highest_reputation_owner['owner']['display_name'])
    print("   Reputation:", highest_reputation_owner['owner']['reputation'])
    print("   Answer:", highest_reputation_owner['title'])

def main():
    url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data = fetch_data(url)
    answered, unanswered = get_answered_unanswered(data)
    least_viewed_answer = get_least_viewed_answer(data)
    oldest_answer, newest_answer = get_oldest_and_newest_answer(data)
    highest_reputation_owner = get_highest_reputation_owner_response(data)
    print_results(answered, unanswered, least_viewed_answer, oldest_answer, newest_answer, highest_reputation_owner)

if __name__ == "__main__":
    main()
