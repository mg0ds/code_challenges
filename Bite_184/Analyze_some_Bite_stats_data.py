from csv import DictReader
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def __init__(self, data=DATA):
        with open(data) as csv_file:
            self.rows = [row for row in csv_file]
            #print(self.rows)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        bite_list = []
        for row in self.rows:
            bite, user, completed = row.split(",")
            bite_list.append(bite)
        return len(set(bite_list))-1
            

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        bite_list = []
        for row in self.rows:
            bite, user, completed = row.split(",")
            if completed == "True\n":
                bite_list.append(bite)
        return len(set(bite_list))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        user_list = []
        for row in self.rows:
            bite, user, completed = row.split(",")
            user_list.append(user)
        return len(set(user_list))-1

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        user_list = []
        for row in self.rows:
            bite, user, completed = row.split(",")
            if completed == "True\n":
                user_list.append(user)
        return len(set(user_list))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        bite_count = {}
        for row in self.rows:
            bite, user, completed = row.split(",")
            if completed == "True\n":
                if bite_count.get(bite) == None:
                    bite_count[bite] = 1
                else:
                    bite_count[bite] += 1
        #print(bite_count)
        return max(bite_count, key=bite_count.get)

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        user_list = {}
        for row in self.rows:
            bite, user, completed = row.split(",")
            if completed == "True\n":
                if user_list.get(user) == None:
                    user_list[user] = 1
                else:
                    user_list[user] += 1
        #print(bite_count)
        return max(user_list, key=user_list.get)
