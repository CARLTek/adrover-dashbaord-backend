from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from .models import AdRecord, AdAnalytics
from datetime import datetime
from django.utils import timezone



class AddAnalyticsData(APIView):
    def post(self, request):
        try:
            data = json.loads(request.data)
            print(data)

            ad_id = data.get("ad id")
            timestamp = data.get("time")  # Example: "12:41, 19-02-2025"
            total_persons = data.get("total persons")
            person_data = data.get("person data", {})

            # Convert timestamp to Django DateTimeField format
            timestamp_obj = datetime.strptime(timestamp, "%H:%M, %d-%m-%Y")
            # Convert to timezone-aware datetime
            timestamp_obj = timezone.make_aware(timestamp_obj)


            # Create AdRecord entry
            ad_record, created = AdRecord.objects.get_or_create(
                ad_id=ad_id,
                defaults={"timestamp": timestamp_obj, "total_persons": total_persons},
            )

            # Create Person entries
            for person_id, person_info in person_data.items():
                AdAnalytics.objects.create(
                    ad_record=ad_record,
                    person_id=int(person_id),
                    counted=person_info.get("counted", False),
                    age=person_info.get("age"),
                    gender=person_info.get("gender"),
                )

            return JsonResponse({"status": "success", "message": "Data added successfully"})
        except Exception as e:
                print(e)
                print(e.__traceback__.tb_lineno)
                return HttpResponse(f"Invalid data format {e} line number {e.__traceback__.tb_lineno}", status=400)


class GetAnalyticsData(APIView):
    def get(self, request):
        # branch_id    = request.query_params.get('shop_id')
        return HttpResponse("Welcome to the Analytics Data API! GET api")