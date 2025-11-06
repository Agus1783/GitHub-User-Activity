import sys
import requests
from rich import print as rich_print

"""
function url to get api from user latest activity (events)
"""
def get_latest_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        activity = response.json()
        latest_activity = activity
        rich_print(f"Latest events / activity for [bold yellow]{username}[/bold yellow]:")
        for activity in latest_activity:
            match activity['type']:
                case 'IssuecommentEvent':
                    rich_print(f"- :smiley: commented on issue {activity['payload']['issue']['number']}")
                case 'PushEvent':
                    rich_print(f"- :smiley: pushed to {activity['repo']['name']}")
                case 'IssueEvent':
                    rich_print(f"- :smiley: created issue {activity['payload']['issue']['number']}")
                case 'WatchEvent':
                    rich_print(f"- :smiley: starred {activity['repo']['name']}")
                case 'PullRequestEvent':
                    rich_print(f"- :smiley: created pull request {activity['payload']['pull_request']['number']}")
                case 'PullRequestReviewEvent':
                    rich_print(f"- :smiley: reviewed pull request {activity['payload']['pull_request']['number']}")
                case 'PullRequestReviewCommentEvent':
                    rich_print(f"- :smiley: commented on pull request {activity['payload']['pull_request']['number']}")
                case 'CreateEvent':
                    rich_print(f"- :smiley: created {activity['payload']['ref_type']} {activity['payload']['ref']}")
                case _:
                    rich_print(f"- :smiley: {activity['type']}")
    else :
        rich_print(f"Error fetching events activity for {username}: {response.status_code}")
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_activity(sys.argv[1])
    else:
        print("Please provide a GitHub username as a command line argument.")
                    
                    