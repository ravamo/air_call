import unittest
from unittest.mock import patch
import pandas as pd
from pandas._testing import assert_frame_equal

from src.airCall import airCallScraping



class MyTestCase(unittest.TestCase):

    def test_get_repo_commit(self):
        fake_json = [{
            "sha": "25755504a382dab7616a209e066ff8231a110c7b",
            "node_id": "MDY6Q29tbWl0NDU1NjAwOjI1NzU1NTA0YTM4MmRhYjc2MTZhMjA5ZTA2NmZmODIzMWExMTBjN2I=",
            "commit": {
                "author": {
                    "name": "Arnab De",
                    "email": "arnabde@fb.com",
                    "date": "2021-08-17T19:02:19Z"
                },
                "committer": {
                    "name": "Facebook GitHub Bot",
                    "email": "facebook-github-bot@users.noreply.github.com",
                    "date": "2021-08-17T19:04:04Z"
                },
                "message": "Generalize class_get_class_name for lazy classes\n\nSummary: We need this builtin for (lazy) class to string conversion.\n\nReviewed By: paulbiss\n\nDifferential Revision: D30313198\n\nfbshipit-source-id: 607f3b799972386072776c241be1c51ee6f9b4aa",
                "tree": {
                    "sha": "e04c39cde9af4b08406172c4ea828cccd6322788",
                    "url": "https://api.github.com/repos/facebook/hhvm/git/trees/e04c39cde9af4b08406172c4ea828cccd6322788"
                },
                "url": "https://api.github.com/repos/facebook/hhvm/git/commits/25755504a382dab7616a209e066ff8231a110c7b",
                "comment_count": 0,
                "verification": {
                    "verified": 'false',
                    "reason": "unsigned",
                    "signature": 'null',
                    "payload": 'null'
                }
            },
            "url": "https://api.github.com/repos/facebook/hhvm/commits/25755504a382dab7616a209e066ff8231a110c7b",
            "html_url": "https://github.com/facebook/hhvm/commit/25755504a382dab7616a209e066ff8231a110c7b",
            "comments_url": "https://api.github.com/repos/facebook/hhvm/commits/25755504a382dab7616a209e066ff8231a110c7b/comments",
            "author": {
                "login": "arnabde03",
                "id": 4754688,
                "node_id": "MDQ6VXNlcjQ3NTQ2ODg=",
                "avatar_url": "https://avatars.githubusercontent.com/u/4754688?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/arnabde03",
                "html_url": "https://github.com/arnabde03",
                "followers_url": "https://api.github.com/users/arnabde03/followers",
                "following_url": "https://api.github.com/users/arnabde03/following{/other_user}",
                "gists_url": "https://api.github.com/users/arnabde03/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/arnabde03/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/arnabde03/subscriptions",
                "organizations_url": "https://api.github.com/users/arnabde03/orgs",
                "repos_url": "https://api.github.com/users/arnabde03/repos",
                "events_url": "https://api.github.com/users/arnabde03/events{/privacy}",
                "received_events_url": "https://api.github.com/users/arnabde03/received_events",
                "type": "User",
                "site_admin": 'false'
            },
            "committer": {
                "login": "facebook-github-bot",
                "id": 6422482,
                "node_id": "MDQ6VXNlcjY0MjI0ODI=",
                "avatar_url": "https://avatars.githubusercontent.com/u/6422482?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/facebook-github-bot",
                "html_url": "https://github.com/facebook-github-bot",
                "followers_url": "https://api.github.com/users/facebook-github-bot/followers",
                "following_url": "https://api.github.com/users/facebook-github-bot/following{/other_user}",
                "gists_url": "https://api.github.com/users/facebook-github-bot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/facebook-github-bot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/facebook-github-bot/subscriptions",
                "organizations_url": "https://api.github.com/users/facebook-github-bot/orgs",
                "repos_url": "https://api.github.com/users/facebook-github-bot/repos",
                "events_url": "https://api.github.com/users/facebook-github-bot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/facebook-github-bot/received_events",
                "type": "User",
                "site_admin": 'false'
            },
            "parents": [
                {
                    "sha": "6d9d519c7760373f9324418c9895f328a7cb5550",
                    "url": "https://api.github.com/repos/facebook/hhvm/commits/6d9d519c7760373f9324418c9895f328a7cb5550",
                    "html_url": "https://github.com/facebook/hhvm/commit/6d9d519c7760373f9324418c9895f328a7cb5550"
                }
            ]
        }]

        df1 = pd.DataFrame({'date_commit': ['2021-08-17'], 'repository': ['hhvm'], 'user': ['Arnab De'] })
        df2 = airCallScraping().get_repo_commit(fake_json)
        assert_frame_equal(df1, df2)

    def test_get_repos(self):
        fake_json = [{
            "id": 455600,
            "node_id": "MDEwOlJlcG9zaXRvcnk0NTU2MDA=",
            "name": "hhvm",
            "full_name": "facebook/hhvm",
            "private": 'false',
            "owner": {
                "login": "facebook",
                "id": 69631,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjY5NjMx",
                "avatar_url": "https://avatars.githubusercontent.com/u/69631?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/facebook",
                "html_url": "https://github.com/facebook",
                "followers_url": "https://api.github.com/users/facebook/followers",
                "following_url": "https://api.github.com/users/facebook/following{/other_user}",
                "gists_url": "https://api.github.com/users/facebook/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/facebook/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/facebook/subscriptions",
                "organizations_url": "https://api.github.com/users/facebook/orgs",
                "repos_url": "https://api.github.com/users/facebook/repos",
                "events_url": "https://api.github.com/users/facebook/events{/privacy}",
                "received_events_url": "https://api.github.com/users/facebook/received_events",
                "type": "Organization",
                "site_admin": 'false'
            },
            "html_url": "https://github.com/facebook/hhvm",
            "description": "A virtual machine for executing programs written in Hack.",
            "fork": 'false',
            "url": "https://api.github.com/repos/facebook/hhvm",
            "forks_url": "https://api.github.com/repos/facebook/hhvm/forks",
            "keys_url": "https://api.github.com/repos/facebook/hhvm/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/facebook/hhvm/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/facebook/hhvm/teams",
            "hooks_url": "https://api.github.com/repos/facebook/hhvm/hooks",
            "issue_events_url": "https://api.github.com/repos/facebook/hhvm/issues/events{/number}",
            "events_url": "https://api.github.com/repos/facebook/hhvm/events",
            "assignees_url": "https://api.github.com/repos/facebook/hhvm/assignees{/user}",
            "branches_url": "https://api.github.com/repos/facebook/hhvm/branches{/branch}",
            "tags_url": "https://api.github.com/repos/facebook/hhvm/tags",
            "blobs_url": "https://api.github.com/repos/facebook/hhvm/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/facebook/hhvm/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/facebook/hhvm/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/facebook/hhvm/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/facebook/hhvm/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/facebook/hhvm/languages",
            "stargazers_url": "https://api.github.com/repos/facebook/hhvm/stargazers",
            "contributors_url": "https://api.github.com/repos/facebook/hhvm/contributors",
            "subscribers_url": "https://api.github.com/repos/facebook/hhvm/subscribers",
            "subscription_url": "https://api.github.com/repos/facebook/hhvm/subscription",
            "commits_url": "https://api.github.com/repos/facebook/hhvm/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/facebook/hhvm/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/facebook/hhvm/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/facebook/hhvm/issues/comments{/number}",
            "contents_url": "https://api.github.com/repos/facebook/hhvm/contents/{+path}",
            "compare_url": "https://api.github.com/repos/facebook/hhvm/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/facebook/hhvm/merges",
            "archive_url": "https://api.github.com/repos/facebook/hhvm/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/facebook/hhvm/downloads",
            "issues_url": "https://api.github.com/repos/facebook/hhvm/issues{/number}",
            "pulls_url": "https://api.github.com/repos/facebook/hhvm/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/facebook/hhvm/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/facebook/hhvm/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/facebook/hhvm/labels{/name}",
            "releases_url": "https://api.github.com/repos/facebook/hhvm/releases{/id}",
            "deployments_url": "https://api.github.com/repos/facebook/hhvm/deployments",
            "created_at": "2010-01-02T01:17:06Z",
            "updated_at": "2021-08-17T12:51:36Z",
            "pushed_at": "2021-08-17T10:54:24Z",
            "git_url": "git://github.com/facebook/hhvm.git",
            "ssh_url": "git@github.com:facebook/hhvm.git",
            "clone_url": "https://github.com/facebook/hhvm.git",
            "svn_url": "https://github.com/facebook/hhvm",
            "homepage": "https://hhvm.com",
            "size": 489826,
            "stargazers_count": 17029,
            "watchers_count": 17029,
            "language": "C++",
            "has_issues": 'true',
            "has_projects": 'false',
            "has_downloads": 'false',
            "has_wiki": 'true',
            "has_pages": 'false',
            "forks_count": 2953,
            "mirror_url": 'null',
            "archived": 'false',
            "disabled": 'false',
            "open_issues_count": 636,
            "license": {
                "key": "other",
                "name": "Other",
                "spdx_id": "NOASSERTION",
                "url": 'null',
                "node_id": "MDc6TGljZW5zZTA="
            },
            "forks": 2953,
            "open_issues": 636,
            "watchers": 17029,
            "default_branch": "master",
            "permissions": {
                "admin": 'false',
                "maintain": 'false',
                "push": 'false',
                "triage": 'false',
                "pull": 'true'
            }
        }]

        with patch('src.airCall.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = airCallScraping()
            response = obj.get_repos('https://35aa0611-a748-4786-8e12-ed652a127d11.mock.pstmn.io/repos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)

    def test_get_repos(self):
        fake_json = [{"message":"API rate limit exceeded for 195.53.117.231. (But here\'s the good news: Authenticated requests get a higher"
        "rate limit. Check out the documentation for more"
        "details.)","documentation_url":"https://docs.github.com//rest//overview//resources-in-the-rest-api#rate-limiting"}]
        with patch('src.airCall.requests.get') as mock_get:
            mock_get.return_value.status_code = 403
            mock_get.return_value.json.return_value = fake_json

            obj = airCallScraping()
            response = obj.get_repos('https://35aa0611-a748-4786-8e12-ed652a127d11.mock.pstmn.io/repos/facebook/hhvm/commits?page=1&until=2021-08-17T20:10:54Z&since=2021-08-16T20:10:54Z')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), fake_json)

    def test_get_repo_list(self):
        fake_json = [{
            "id": 455600,
            "node_id": "MDEwOlJlcG9zaXRvcnk0NTU2MDA=",
            "name": "hhvm",
            "full_name": "facebook/hhvm",
            "private": 'false',
            "owner": {
                "login": "facebook",
                "id": 69631,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjY5NjMx",
                "avatar_url": "https://avatars.githubusercontent.com/u/69631?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/facebook",
                "html_url": "https://github.com/facebook",
                "followers_url": "https://api.github.com/users/facebook/followers",
                "following_url": "https://api.github.com/users/facebook/following{/other_user}",
                "gists_url": "https://api.github.com/users/facebook/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/facebook/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/facebook/subscriptions",
                "organizations_url": "https://api.github.com/users/facebook/orgs",
                "repos_url": "https://api.github.com/users/facebook/repos",
                "events_url": "https://api.github.com/users/facebook/events{/privacy}",
                "received_events_url": "https://api.github.com/users/facebook/received_events",
                "type": "Organization",
                "site_admin": 'false'
            },
            "html_url": "https://github.com/facebook/hhvm",
            "description": "A virtual machine for executing programs written in Hack.",
            "fork": 'false',
            "url": "https://api.github.com/repos/facebook/hhvm",
            "forks_url": "https://api.github.com/repos/facebook/hhvm/forks",
            "keys_url": "https://api.github.com/repos/facebook/hhvm/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/facebook/hhvm/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/facebook/hhvm/teams",
            "hooks_url": "https://api.github.com/repos/facebook/hhvm/hooks",
            "issue_events_url": "https://api.github.com/repos/facebook/hhvm/issues/events{/number}",
            "events_url": "https://api.github.com/repos/facebook/hhvm/events",
            "assignees_url": "https://api.github.com/repos/facebook/hhvm/assignees{/user}",
            "branches_url": "https://api.github.com/repos/facebook/hhvm/branches{/branch}",
            "tags_url": "https://api.github.com/repos/facebook/hhvm/tags",
            "blobs_url": "https://api.github.com/repos/facebook/hhvm/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/facebook/hhvm/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/facebook/hhvm/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/facebook/hhvm/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/facebook/hhvm/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/facebook/hhvm/languages",
            "stargazers_url": "https://api.github.com/repos/facebook/hhvm/stargazers",
            "contributors_url": "https://api.github.com/repos/facebook/hhvm/contributors",
            "subscribers_url": "https://api.github.com/repos/facebook/hhvm/subscribers",
            "subscription_url": "https://api.github.com/repos/facebook/hhvm/subscription",
            "commits_url": "https://api.github.com/repos/facebook/hhvm/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/facebook/hhvm/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/facebook/hhvm/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/facebook/hhvm/issues/comments{/number}",
            "contents_url": "https://api.github.com/repos/facebook/hhvm/contents/{+path}",
            "compare_url": "https://api.github.com/repos/facebook/hhvm/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/facebook/hhvm/merges",
            "archive_url": "https://api.github.com/repos/facebook/hhvm/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/facebook/hhvm/downloads",
            "issues_url": "https://api.github.com/repos/facebook/hhvm/issues{/number}",
            "pulls_url": "https://api.github.com/repos/facebook/hhvm/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/facebook/hhvm/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/facebook/hhvm/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/facebook/hhvm/labels{/name}",
            "releases_url": "https://api.github.com/repos/facebook/hhvm/releases{/id}",
            "deployments_url": "https://api.github.com/repos/facebook/hhvm/deployments",
            "created_at": "2010-01-02T01:17:06Z",
            "updated_at": "2021-08-17T12:51:36Z",
            "pushed_at": "2021-08-17T10:54:24Z",
            "git_url": "git://github.com/facebook/hhvm.git",
            "ssh_url": "git@github.com:facebook/hhvm.git",
            "clone_url": "https://github.com/facebook/hhvm.git",
            "svn_url": "https://github.com/facebook/hhvm",
            "homepage": "https://hhvm.com",
            "size": 489826,
            "stargazers_count": 17029,
            "watchers_count": 17029,
            "language": "C++",
            "has_issues": 'true',
            "has_projects": 'false',
            "has_downloads": 'false',
            "has_wiki": 'true',
            "has_pages": 'false',
            "forks_count": 2953,
            "mirror_url": 'null',
            "archived": 'false',
            "disabled": 'false',
            "open_issues_count": 636,
            "license": {
                "key": "other",
                "name": "Other",
                "spdx_id": "NOASSERTION",
                "url": 'null',
                "node_id": "MDc6TGljZW5zZTA="
            },
            "forks": 2953,
            "open_issues": 636,
            "watchers": 17029,
            "default_branch": "master",
            "permissions": {
                "admin": 'false',
                "maintain": 'false',
                "push": 'false',
                "triage": 'false',
                "pull": 'true'
            }
        }]
        self.assertListEqual(airCallScraping().get_repo_list(fake_json), ['hhvm'])


if __name__ == '__main__':
    unittest.main()
