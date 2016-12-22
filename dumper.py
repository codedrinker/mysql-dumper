import os
from optparse import OptionParser
from datetime import *
import time

import web

urls = (
    '/dump', 'dump'
)

app = web.application(urls, globals())


class dump:
    def GET(self):
        input = web.input()
        if input.password == "mysql-dumper":
            os.system("dumping...")
            os.system("echo $MYSQL_DUMPER_PATH")
            os.system("echo $MYSQL_DUMPER_HOST")
            os.system("echo $MYSQL_DUMPER_USER")
            os.system("echo $MYSQL_DUMPER_PASSWORD")
            os.system("echo $MYSQL_DUMPER_DATABASE")

            os.system("echo \"mysqldump -h$MYSQL_DUMPER_HOST -u$MYSQL_DUMPER_USER -p$MYSQL_DUMPER_PASSWORD $MYSQL_DUMPER_DATABASE > $MYSQL_DUMPER_PATH/$MYSQL_DUMPER_DATABASE.sql\"")
            os.system("mysqldump -h$MYSQL_DUMPER_HOST -u$MYSQL_DUMPER_USER -p$MYSQL_DUMPER_PASSWORD $MYSQL_DUMPER_DATABASE > $MYSQL_DUMPER_PATH/$MYSQL_DUMPER_DATABASE.sql")
            
            os.system("dumped")
            return "ok"
        return "Authorization Failed."


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--mysql-dump-dir", type="string", dest="path", default="~", help="Directory used as dump sql.")
    parser.add_option("--mysql-host", type="string", dest="host", default="localhost", help="MySQL host.")
    parser.add_option("--mysql-user", type="string", dest="user", default="test", help="MySQL user.")
    parser.add_option("--mysql-password", type="string", dest="password", default="test", help="MySQL password.")
    parser.add_option("--mysql-database", type="string", dest="database", default="test", help="MySQL database.")

    (options, args) = parser.parse_args()

    os.environ['MYSQL_DUMPER_PATH'] = options.path
    os.environ['MYSQL_DUMPER_HOST'] = options.host
    os.environ['MYSQL_DUMPER_USER'] = options.user
    os.environ['MYSQL_DUMPER_PASSWORD'] = options.password
    os.environ['MYSQL_DUMPER_DATABASE'] = options.database

    app.run()
