from django.db import connection


def get_database_size():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT pg_size_pretty(
                pg_database_size(current_database())
            );
            """
        )

        size = cursor.fetchone()[0]

    return size