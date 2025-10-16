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
                score_overall DECIMAL(5,2) DEFAULT 0.00,
                score_skills DECIMAL(5,2) DEFAULT 0.00,
                score_experience DECIMAL(5,2) DEFAULT 0.00,
                score_education DECIMAL(5,2) DEFAULT 0.00,
                summary LONGTEXT,
                updated_at DATETIME NOT NULL,
                created_at DATETIME NOT NULL
            ) ENGINE=INNODB;
		"""

        if not Db.ExecuteQuery(query, None, True):
            return False

        Db.ExecuteQuery("ALTER TABLE template ADD INDEX id (id);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX updated_at (updated_at);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX created_at (created_at);", None, True)
        #####################################################################################################

        return True