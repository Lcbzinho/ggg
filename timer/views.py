import asyncio
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
async def countdown(request):
	seconds_param = request.GET.get("seconds", "5")
	try:
		seconds = max(0, int(seconds_param))
	except ValueError:
		seconds = 5

	for _ in range(seconds):
		await asyncio.sleep(1)

	return JsonResponse({"elapsed_seconds": seconds, "message": "Contagem concluída"})

# Create your views here.
