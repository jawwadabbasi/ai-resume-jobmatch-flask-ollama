import inspect
import json
from werkzeug.datastructures import FileStorage

from includes.common import Common
from includes.db import Db
from services.logger import Logger
from v1.parser import Parser
from v1.analysis import Analysis
from v1.handler import Handler
from v1.wrapper import Wrapper

class Resume:

	def Analyse(job_description,resume):

		api_data = {}
		api_data['ApiHttpResponse'] = 500
		api_data['ApiMessages'] = []
		api_data['ApiResult'] = []

		try:
			job_description = str(job_description).strip()

		except:
			api_data['ApiHttpResponse'] = 400
			api_data['ApiMessages'] += ['INFO - Invalid arguments']

			return api_data

		if not isinstance(resume,FileStorage):
			api_data['ApiHttpResponse'] = 400
			api_data['ApiMessages'] += ['INFO - Expected a PDF file for resume upload']

			return api_data
		
		if not resume.filename.lower().endswith(".pdf"):
			api_data['ApiHttpResponse'] = 400
			api_data['ApiMessages'] += ['INFO - Only PDF resumes are supported']

			return api_data
		
		try:
			r = resume.read()
			resume_text = Parser.FromPdf(r)

		except Exception as e:
			Logger.CreateExceptionLog(inspect.stack()[0][3],str(e),f'ERROR - Failed to read resume')

			api_data['ApiHttpResponse'] = 400
			api_data['ApiMessages'] += ['INFO - Invalid resume']

			return api_data
		
		metrics = Analysis.Run(resume_text, job_description)
		
		if not metrics:
			api_data['ApiHttpResponse'] = 500
			api_data['ApiMessages'] += ['ERROR - Failed to get metrics']

			return api_data

		query = """
			INSERT INTO analyses
			SET resume_text = %s,
				jd_text = %s,
				meta = %s,
				date = NOW()
		"""

		inputs = (
			resume_text,
            job_description,
            json.dumps(Handler.JsonSafe(metrics))
		)

		result = Db.ExecuteQuery(query,inputs,True)

		if not result:
			api_data['ApiHttpResponse'] = 500
			api_data['ApiMessages'] += ['ERROR - Could not store analysis']

			return api_data

		api_data['ApiHttpResponse'] = 201
		api_data['ApiMessages'] += ['Request processed successfully']
		api_data["ApiResult"] = [Handler.JsonSafe(metrics)]

		return api_data