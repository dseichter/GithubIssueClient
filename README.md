# GithubIssueClient

Create really simple a new task in your GitHub repositories with the GitHub Issue Client.

![pep8](https://github.com/dseichter/GithubIssueClient/actions/workflows/pep8.yml/badge.svg)
![trivy](https://github.com/dseichter/GithubIssueClient/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_GithubIssueClient&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_GithubIssueClient)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=dseichter_GithubIssueClient)

## About

With my **GitHub Issue Client** you can easily and quickly create new tasks within your GitHub repositories. You can access all your available repositories and always get the latest data to create new tasks. All you need is to provide your username and the corresponding Personal Access Token. You create this in your Github profile. Are you using **GitHub Enterprise**? No problem, just provide your instance URL.

![GitHub Issue Client](/images/githubissueclient.png "GitHub Issue Client")

## Installation and configuration of GitHub Issue Client

Download the [latest release](https://github.com/dseichter/GithubIssueClient/releases) and save the file in a directory of your choice. In this directory the program creates its configuration file automatically. Depending on how many different GitHub accounts you use, create another subdirectory each with a copy of the executable.

When you start the application for the first time, it checks whether you have already specified a user name and a personal access token (PAT). If this is not the case, enter your own data on the configuration tab. We reload your repositories every time you start the program. This way the program will always show you the latest data. In addition you have the possibility to reload the list of your repositories at any time also over the button again.

![GitHub Issue Client - Configuration](/images/githubissueclient_configuration.png "GitHub Issue Client - Configuration")

# Contributing

If you want to contribute by fixing an issue, add a new function or just optimize something, a simple instruction how to start development.

## Start development

Create and activate an environment by running the following command:

```python -m venv .venv```

```.venv/Scripts/activate```

Install the required dependencies

```pip install -r src/requirements.txt```

The application has been migrated from wxPython to PySide6 for better cross-platform compatibility and modern Qt features.

To run the PySide6 version:

```python src/githubissueclient.py```

## 📄 License

GPL 3.0 — see [LICENSE](LICENSE) file at the root of the repository for details.

## Icons
 
GitHubIssueClient uses [Google Material Symbols](https://fonts.google.com/icons) within its code for UI icons.  
Material Symbols are licensed under the [Apache License 2.0](https://github.com/google/material-design-icons/blob/master/LICENSE) and are free for use in open source projects.
