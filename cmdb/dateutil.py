__author__ = 'lenovo'
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date, datetime
import json
import sys

if __name__ == '__main__':
    td = datetime.today()
    print json.dumps(td, cls=DjangoJSONEncoder)