import settings
from github import Github

# Authentication is defined via github.Auth
from github import Auth


# load all repositories from the user
def get_repos():
    # get the config
    config = settings.read_config()
    # check if we should use github or ghe
    if config['use_github']:
        g = Github(config['personal_access_token'])
    else:
        g = Github(config['personal_access_token'], base_url=config['ghe_url'])
    # get the user
    user = g.get_user()
    # get all repos
    print(user.get_repos())
    for repo in user.get_repos():
        print(repo.full_name)
    return user.get_repos()


def get_labels(repo):
    print(repo.get_labels())
    for label in repo.get_labels():
        print(label.name)


def get_milestones(repo):
    print(repo.get_milestones())
    for milestone in repo.get_milestones():
        print(milestone.title)


def get_assignees(repo):
    print(repo.get_assignees())
    for assignee in repo.get_assignees():
        print(assignee.login)


def create_issue(repo, title, body, assignee, milestone, labels):
    print(repo.create_issue(title, body, assignee, milestone, labels))
