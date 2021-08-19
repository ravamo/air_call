import time

import dateutil.parser
import requests
import pandas as pd
from sqlalchemy import create_engine
from requests import ReadTimeout, HTTPError, Timeout, ConnectionError



class airCallScraping:

    def __init__(self):
        self.list_repos_git = []
        self.access_token = ' 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'
        self.sqlEngine = create_engine('mysql+pymysql://root:my-secret-pw@localhost/aircall', pool_recycle=3600)
        self.dbConnection = self.sqlEngine.connect()

    def get_repos(self, url):
        headers = {}
        try:
            r = requests.get(url=url, headers=headers, timeout=2)
            print(r.status_code)
            print(r.json())
            if r.ok:
                time.sleep(15)
                return r
            elif r.status_code == 403:
                print("ERROR")
                pass
            else:
                return None
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
                return f'Bad Response: {e}'

    def get_repo_list(self, response):
        for d in response.json():
            self.list_repos_git.append(d.get('full_name').split("/")[1])
        return self.list_repos_git

    def get_repo_commit(self, response):
        repository = []
        user = []
        date_commit = []
        print(response.json())
        # json = self.get_repos(self.commit)
        for d in response:  # json.json():
            user.append((d['commit']['author']['name']))
            date_commit.append(dateutil.parser.parse(d['commit']['author']['date']).strftime('%Y-%m-%d'))
            repository.append((d['commit']['url'].split('/')[5]))
        self.commit = pd.DataFrame()
        self.commit['date_commit'] = date_commit
        self.commit['repository'] = repository
        self.commit['user'] = user
        self.commit = self.commit.sort_values(by=['repository', 'user']).drop_duplicates('user', keep='last')
        print(self.commit.head())
        return False

    def set_factable(self):
        # create a delta
        self.commit.to_sql('delta_commit', self.dbConnection, if_exists='replace', index=False);
        self.sqlEngine.execute(
            "INSERT INTO fact_commit (date_commit,repository,user) "
            "SELECT date(s.date_commit) as date_commit, s.repository, s.user "
            "FROM delta_commit s "
            "LEFT OUTER JOIN aircall.fact_commit a "
            "ON a.repository = s.repository "
            "AND a.user = s.user "
            "WHERE a.user IS NULL;")
        self.dbConnection.close()

    def get_user(self):
        frame = pd.read_sql(" select repository,date_commit,count(user) as new_contributor from fact_commit  group by 1,2 order by 2 asc;", self.dbConnection)
        pd.set_option('display.expand_frame_repr', False)
        #print( frame.to_json(orient="records"))
        return frame.to_json(orient="records")

    def get_user_range(self, init, end):
        frame = pd.read_sql(f" select repository,date_commit,count(user) as new_contributor from fact_commit where date_commit "
                            f" where date_commit BETWEEN '{init}' and '{end}' group by 1,2 order by 2 asc;",
                            self.dbConnection)
        pd.set_option('display.expand_frame_repr', False)
        frame.to_json(orient="records")
        return frame.to_json(orient="records")

    def integration(self, date_init, date_end):
        # get all repository
        for page_num in range(1,3):
            self.list_repos_git.append(self.get_repo_list((self.get_repos(f'https://api.github.com/orgs/facebook/repos?per_page=100&page={page_num}'))))
        for repos in self.list_repos_git:
            print(repos)
            next = True
            index = 0
            while next == True:
                print("GOL")
                url = f"https://api.github.com/repos/facebook/{repos}/commits?page={page_num}&until={date_init}&since={date_end}"
                print(url)
                print(self.get_repo_commit(self.get_repos(url)))
                index=index+1


if __name__ == "__main__":
    obj1 = airCallScraping()
    #obj1.integration('2021-08-17T20:10:54Z','2021-08-16T20:10:54Z')
    #print(obj1.get_repos('https://api.github.com/orgs/facebook/repos?per_page=100&page=1'))
    #obj1.get_repo_list(obj1.get_repos('https://35aa0611-a748-4786-8e12-ed652a127d11.mock.pstmn.io/repos').json())
    #obj1.get_repo_commit(obj1.get_repos(
    #    'https://35aa0611-a748-4786-8e12-ed652a127d11.mock.pstmn.io/repos/facebook/hhvm/commits?page=1&until=2021-08-17T20:10:54Z&since=2021-08-16T20:10:54Z').json())
    #obj1.set_factable()
    obj1.get_user()
    # print(obj1.get_repo_commit())
    # print(obj1.get_repos('https://35aa0611-a748-4786-8e12-ed652a127d11.mock.pstmn.io/repos').json())
