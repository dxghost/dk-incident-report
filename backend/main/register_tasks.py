if __name__ == "__main__":
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reporter.settings')
    import django
    django.setup()
    
    from django_q.tasks import schedule
    from django_q.models import Schedule
    
    schedule(
        "reports.tasks.fetch_logs",
        hook="reports.models.store_multiple_reports",
        schedule_type=Schedule.CRON,
        cron="*/1 * * * *",
    )
