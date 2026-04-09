from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
import os
import time

try:
    import google.genai as genai
except ImportError:
    genai = None


request_times = []
MAX_REQUESTS_PER_MINUTE = 10


def home(request):
    return render(request, 'home.html')


def check_rate_limit():
    global request_times
    current_time = time.time()

    request_times = [t for t in request_times if current_time - t < 60]

    if len(request_times) >= MAX_REQUESTS_PER_MINUTE:
        return False, f"Rate limit exceeded. Maximum {MAX_REQUESTS_PER_MINUTE} requests per minute."

    request_times.append(current_time)
    return True, None


@require_http_methods(["POST"])
def chat_bot(request):
    try:

        allowed, error_msg = check_rate_limit()
        if not allowed:
            return JsonResponse({'error': error_msg}, status=429)

        data = json.loads(request.body)
        message = data.get('message', '').strip()

        if not message:
            return JsonResponse({'error': 'Message cannot be empty'}, status=400)

        from django.conf import settings
        api_key = settings.GOOGLE_API_KEY

        if not api_key:
            return JsonResponse({'error': 'Google AI API key not configured'}, status=500)

        if not genai:
            return JsonResponse({'error': 'Google GenAI library not installed'}, status=500)


        client = genai.Client(api_key=api_key)

        system_prompt = "You are a helpful medical assistant for Swift Care, Always greet with the appropriate time of day when interacting with users. You are working within a healthcare application and should provide clear, accurate, and concise medical information while reminding users to consult healthcare professionals for serious concerns with keeping india 's healthcare facilities in  mind."


        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=[
                    {
                        "role": "user",
                        "parts": [{"text": f"{system_prompt}\n\nUser question: {message}"}]
                    }
                ],
                config={
                    "temperature": 0.7,
                    "max_output_tokens": 500
                }
            )

            reply = response.text
            return JsonResponse({'reply': reply})

        except Exception as api_error:
            error_str = str(api_error)

            if '429' in error_str or 'RESOURCE_EXHAUSTED' in error_str or 'quota' in error_str.lower():
                return JsonResponse({
                    'error': 'Google API quota exceeded. Please try again in a few minutes or upgrade your plan at https://ai.google.dev'
                }, status=429)

            raise api_error

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error: {str(e)}'}, status=500)
