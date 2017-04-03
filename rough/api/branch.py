from sanic.response import json
from . import api


@api.route('/branches', methods=['GET'])
async def get_branches(request):
    