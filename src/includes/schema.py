import settings

from includes.db import Db

class Schema:

    def CreateDatabase():

        query = f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci"

        return Db.ExecuteQuery(query, None, True, True)

    def CreateTables():

        #####################################################################################################
        query = """
			CREATE TABLE IF NOT EXISTS analyses (
                id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                resume_text LONGTEXT NOT NULL,
                jd_text LONGTEXT NOT NULL,
                meta JSON NOT NULL,
                date DATETIME NOT NULL
            ) ENGINE=INNODB;
		"""

        if not Db.ExecuteQuery(query, None, True):
            return False

        Db.ExecuteQuery("ALTER TABLE analyses ADD INDEX id (id);", None, True)
        Db.ExecuteQuery("ALTER TABLE analyses ADD INDEX date (date);", None, True)
        #####################################################################################################

        return True