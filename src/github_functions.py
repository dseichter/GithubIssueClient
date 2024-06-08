import settings
from github import Github


def github_connection():
    # get the config
    config = settings.read_config()
    # check if we should use github or ghe
    if config['use_github']:
        return Github(config['personal_access_token'])
    else:
        return Github(config['personal_access_token'], base_url=config['ghe_url'])


# load all repositories from the user
def get_repos():
    # check if we should use github or ghe
    g = github_connection()
    # get the user
    user = g.get_user()
    # get all repos
    return user.get_repos()


# load one single repo
def get_repo(repo):
    # check if we should use github or ghe
    g = github_connection()
    # get all repos
    return g.get_repo(repo)


def get_labels(repo):
    g = github_connection()
    # load all labels from the repository
    repo = g.get_repo(repo)
    return repo.get_labels()


def get_milestones(repo):
    g = github_connection()
    # load all labels from the repository
    repo = g.get_repo(repo)
    return repo.get_milestones(state='open')


def get_assignees(repo):
    g = github_connection()
    # load all labels from the repository
    repo = g.get_repo(repo)
    return repo.get_assignees()


def create_issue(repo='', title='', body='', labels=[], assignee='NotSet', milestone=None):
    print(repo)
    print(title)
    print(body)
    print(assignee)
    print(milestone)
    print(labels)

    # create the issue
    g = github_connection()
    repo = g.get_repo(repo)
    return repo.create_issue(title=title, body=body, assignee=assignee, milestone=milestone, labels=labels)
