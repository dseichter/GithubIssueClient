# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import logging

import urllib3
from packaging.version import InvalidVersion, parse

VERSION = "v2025-12-16"
UPDATEURL = 'https://api.github.com/repos/dseichter/GithubIssueClient/releases/latest'
RELEASES = 'https://github.com/dseichter/GithubIssueClient/releases'
NAME = 'GithubIssueClient'
LICENCE = 'GPL-3.0'
logger = logging.getLogger(__name__)


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', UPDATEURL)
        releases = json.loads(r.data.decode('utf-8'))
        # Find the latest stable (not prerelease) release
        for release in releases:
            if not release.get('prerelease', False):
                latest_version = release.get('tag_name')
                return parse(latest_version) > parse(VERSION)
        return False  # No stable release found
    except (
        urllib3.exceptions.HTTPError,
        json.JSONDecodeError,
        UnicodeDecodeError,
        InvalidVersion,
        TypeError,
    ):
        logger.exception("Error checking for new release")
        return False
